# Uses Heath Nutrition and Population statistics, avalaible at
# http://datacatalog.worldbank.org, stored in the file HNP_Data.csv,
# assumed to be stored in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.


import sys
import os
import csv
import re



filename = 'HNP_Data.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')
# indicator_of_interest='Number of neonatal deaths'
result_first=re.search('(.)(?=\()',indicator_of_interest)
result_second=re.search('(.)(?=\))',indicator_of_interest)
if result_first and result_second:
    first_target=result_first.group(1)+'\\\('
    second_target=result_second.group(1)+'\\\)'
    indicator_of_interest=re.sub('.\(',first_target,indicator_of_interest)
    indicator_of_interest=re.sub('.\)',second_target,indicator_of_interest)
# indicator_of_interest='Literacy rate, youth total \(% of people ages 15-24\)'
# indicator_of_interest='% of females ages 15-49 having comprehensive correct knowledge about HIV (2 prevent ways and reject 3 misconceptions)'

# Insert your code here
pattern_without_double_quotes=re.compile(r'^(.*?),.*?,'+indicator_of_interest+',.*?,(.*),?\n$')
pattern_with_double_quotes=re.compile(r'^(.*?),.*?,"'+indicator_of_interest+'",.*?,(.*),?\n$')
pattern_without_double_quotes_with_first_double_quotes=re.compile(r'^"(.*?)",.*?,'+indicator_of_interest+',.*?,(.*),?\n$')
pattern_with_double_quotes_with_first_double_quotes=re.compile(r'^"(.*?)",.*?,"'+indicator_of_interest+'",.*?,(.*),?\n$')
max_value=None
result_dict={}
with open(filename,'r') as csv_file:
    # count=1
    for eachline in csv_file:
        # print(count)
        # count+=1
        if eachline.startswith('"'):
            result_with_double_quotes = re.match(pattern_with_double_quotes_with_first_double_quotes, eachline)
            if result_with_double_quotes:
                country_name = result_with_double_quotes.group(1)
                year_result = result_with_double_quotes.group(2)
                year_result_list = year_result.split(',')
                result_dict[country_name] = year_result_list
                # print('1: ',year_result_list)
                # print(country_name)
                # print(indicator_name)
                # print(year_result_list)
                continue
            result_without_double_quotes = re.match(pattern_without_double_quotes_with_first_double_quotes, eachline)
            if result_without_double_quotes:
                country_name = result_without_double_quotes.group(1)
                year_result = result_without_double_quotes.group(2)
                year_result_list = year_result.split(',')
                result_dict[country_name] = year_result_list
                # print('2: ',year_result_list)
                # print(country_name)
                # print(indicator_name)
                # print(year_result_list)
        else:
            result_with_double_quotes=re.match(pattern_with_double_quotes,eachline)
            if result_with_double_quotes:
                country_name = result_with_double_quotes.group(1)
                year_result = result_with_double_quotes.group(2)
                year_result_list = year_result.split(',')
                result_dict[country_name]=year_result_list
                # print('1: ',year_result_list)
                # print(country_name)
                # print(indicator_name)
                # print(year_result_list)
                continue
            result_without_double_quotes=re.match(pattern_without_double_quotes,eachline)
            if result_without_double_quotes:
                country_name=result_without_double_quotes.group(1)
                year_result=result_without_double_quotes.group(2)
                year_result_list=year_result.split(',')
                result_dict[country_name]=year_result_list
                # print('2: ',year_result_list)
                # print(country_name)
                # print(indicator_name)
                # print(year_result_list)
# for eachitem in result_dict.items():
#     print(eachitem)
country_and_year={}
for eachkey in result_dict.keys():
    for eachindex in range(0,len(result_dict[eachkey])):
        if result_dict[eachkey][eachindex]=='':
            continue
        temp_float=float(result_dict[eachkey][eachindex])
        if max_value==None:
            max_value=temp_float
            country_and_year[eachindex + 1960] = eachkey
            continue
        if temp_float>max_value:
            max_value=temp_float
            del country_and_year
            country_and_year={}
            country_and_year[eachindex+1960]=[eachkey]
        if temp_float == max_value:
            key_year=eachindex+1960
            if key_year in country_and_year.keys():
                if eachkey not in country_and_year[key_year]:
                    country_and_year[key_year].append(eachkey)
            else:
                country_and_year[eachindex+1960]=[eachkey]
countries_for_max_value_per_year=country_and_year
pattern=re.compile('^(\d+)\.?(\d*)$')
result=re.match(pattern,str(max_value))
if result:
    first=result.group(1)
    second=result.group(2)
    if second=='0':
        max_value=int(first)

if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    for year in sorted(countries_for_max_value_per_year):
        print(f'    {year}: {countries_for_max_value_per_year[year]}')

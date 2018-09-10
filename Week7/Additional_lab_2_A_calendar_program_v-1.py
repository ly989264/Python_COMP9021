import re
import subprocess

month_dict={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
                'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
month_dict_simplify={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
                'Jul':7,'Aug':8,'Sept':9,'Octr':10,'Nov':11,'Dec':12}

def convert_month_to_number(month):
    pattern = re.compile(r'^' + month, re.I)
    for each_key in month_dict.keys():
        if re.match(pattern,each_key):
            return month_dict[each_key]

def get_input():
    print('I will display a calendar, either for a year or for a month in a year.')
    print('The earliest year should be 1753.')
    print('For the month, input at least the first three letters of the month\'s name.')
    inputted_string=input('Input year, or year and month, or month and year: ')
    pattern_only_year=re.compile('^\s*(\d{4})\s*$')
    pattern_year_and_month=re.compile('^\s*(\d{4})\s*([A-Za-z]*)\s*$')
    pattern_month_and_year=re.compile('^\s*([A-Za-z]*)\s*(\d{4})\s*$')
    result_only_year=re.match(pattern_only_year,inputted_string)
    if result_only_year:
        year=int(result_only_year.group(1))
        month=0
        if year<1753:
            return (None,None)
        return (year,month)
    result_year_and_month=re.match(pattern_year_and_month,inputted_string)
    if result_year_and_month:
        year=int(result_year_and_month.group(1))
        month=convert_month_to_number(result_year_and_month.group(2))
        if year<1753:
            return (None,None)
        return (year,month)
    result_month_and_year=re.match(pattern_month_and_year,inputted_string)
    if result_month_and_year:
        year=int(result_month_and_year.group(2))
        month=convert_month_to_number(result_month_and_year.group(1))
        if year<1753:
            return (None,None)
        return (year,month)
    return (None,None)

def display(year,month):
    if month==0:
        subprocess.Popen(f'cal {year}')
    else:
        for eachkey in month_dict_simplify.keys():
            if month_dict_simplify[eachkey]==month:
                month_chr=eachkey
                break
        subprocess.Popen(f'cal {month_chr} {year}')

# testing
year,month=get_input()
display(year,month)
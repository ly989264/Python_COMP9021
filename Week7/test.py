# with open('HNP_Data.csv','r') as f:
#     count=0
#     for eachline in f:
#         count+=1
#         if count>=10550 and count<=10570:
#             print(eachline)
#         if count==10571:
#             break
import re
indicator_of_interest='Number of neonatal deaths'
string='World,WLD,Number of neonatal deaths,SH.DTH.NMRT,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,5106312,4973154,4798953,4608307,4426104,4279025,4174203,4095337,4039407,3981903,3912316,3825629,3727749,3625872,3520216,3424024,3330174,3245021,3165433,3092092,3022673,2951161,2882602,2810611,2746854,2682438'
# pattern_without_double_quotes=re.compile(r'^(.*?),.*?,'+indicator_of_interest+',.*?,(.*),\n$')
pattern_without_double_quotes=re.compile(r'^(.*?),.*?,(.*?),.*?,(.*),?\n$')
pattern_with_double_quotes=re.compile(r'^(.*?),.*?,"'+indicator_of_interest+'",.*?,(.*),\n$')
pattern_without_double_quotes_with_first_double_quotes=re.compile(r'^"(.*?)",.*?,'+indicator_of_interest+',.*?,(.*),\n$')
pattern_with_double_quotes_with_first_double_quotes=re.compile(r'^"(.*?)",.*?,"'+indicator_of_interest+'",.*?,(.*),\n$')
result=re.match(pattern_without_double_quotes,string)
print(result)
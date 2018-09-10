import re

general_year_dict={1:31,2:28,3:31,4:30,5:31,6:30,
                   7:31,8:31,9:30,10:31,11:30,12:31}
special_year_dict={1:31,2:29,3:31,4:30,5:31,6:30,
                   7:31,8:31,9:30,10:31,11:30,12:31}
month_dict={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
                'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

def judge_special(year):
    if not year%4:
        if not year%100:
            if not year%400:
                return True
            else:
                return False
        else:
            return True
    return False

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

def get_first_week(year):# 1/1/1753 is Monday
    if year==1753:
        return 1
    else:
        total_days=0
        for each_year in range(1753,year):
            is_special=judge_special(each_year)
            if is_special:
                total_days+=366
            else:
                total_days+=365
        over=total_days%7
        return (1+over)%7

def get_specific_result(year,month):
    first_week_of_the_year=get_first_week(year)
    if month==0:
        return (year,month,first_week_of_the_year)
    else:
        if month==1:
            return (year,month,first_week_of_the_year)
        else:
            total_days=0
            is_special=judge_special(year)
            for each_month in range(1,month):
                if is_special:
                    total_days+=special_year_dict[each_month]
                else:
                    total_days+=general_year_dict[each_month]
            over=total_days%7
            return (year,month,(first_week_of_the_year+over)%7)

def nicely_display(year,month,week):
    total_width=21
    if month!=0:
        for each_key in month_dict.keys():
            if month_dict[each_key]==month:
                str_month=each_key
        current_width=len(str_month)+1+4
        remaining_width=total_width-current_width
        if remaining_width%2:
            right_spaces=remaining_width//2
            left_spaces=remaining_width-right_spaces
        else:
            left_spaces=remaining_width//2
            right_spaces=remaining_width//2
        print(' '*left_spaces,str_month,' ',year,' '*right_spaces,sep='')
        print(' Mo Tu We Th Fr Sa Su')
        is_special=judge_special(year)
        if is_special:
            days_of_the_month=special_year_dict[month]
        else:
            days_of_the_month=general_year_dict[month]
        current_output_weeked=week
        if current_output_weeked==0:
            print('   '*6,end='')
            current_output_weeked=7
        else:
            print('   '*(current_output_weeked-1),end='')
        for eachday in range(1,days_of_the_month+1):
            if current_output_weeked==7:
                print(f'{eachday:3}')
                current_output_weeked=1
            else:
                print(f'{eachday:3}',end='')
                current_output_weeked+=1
    else:
        whole_width=total_width*3+6
        for each_quarter in range(1,5):
            current_month1=3*each_quarter-2
            current_month2=3*each_quarter-1
            current_month3=3*each_quarter
            for each_key in month_dict.keys():
                if month_dict[each_key]==current_month1:
                    str_month1=each_key
                if month_dict[each_key]==current_month2:
                    str_month2=each_key
                if month_dict[each_key]==current_month3:
                    str_month3=each_key
            current_width1=len(str_month1)+1+4
            remaining_width1=total_width-current_width1
            if remaining_width1%2:
                right_spaces1=remaining_width1//2
                left_spaces1=remaining_width1-right_spaces1
            else:
                left_spaces1=remaining_width1//2
                right_spaces1=remaining_width1//2
            current_width2 = len(str_month2) + 1 + 4
            remaining_width2 = total_width - current_width2
            if remaining_width2 % 2:
                right_spaces2 = remaining_width2 // 2
                left_spaces2 = remaining_width2 - right_spaces2
            else:
                left_spaces2 = remaining_width2 // 2
                right_spaces2 = remaining_width2 // 2
            current_width3 = len(str_month3) + 1 + 4
            remaining_width3 = total_width - current_width3
            if remaining_width3 % 2:
                right_spaces3 = remaining_width3 // 2
                left_spaces3 = remaining_width3 - right_spaces3
            else:
                left_spaces3 = remaining_width3 // 2
                right_spaces3 = remaining_width3 // 2
            print(' ' * left_spaces1, str_month1, ' ', year, ' ' * right_spaces1, sep='', end='   ')
            print(' ' * left_spaces2, str_month2, ' ', year, ' ' * right_spaces2, sep='', end='   ')
            print(' ' * left_spaces3, str_month3, ' ', year, ' ' * right_spaces3, sep='')
            print(' Mo Tu We Th Fr Sa Su',end='   ')
            print(' Mo Tu We Th Fr Sa Su', end='   ')
            print(' Mo Tu We Th Fr Sa Su')
            # need to calculate each first week of these three months
            _,_,week1=get_specific_result(year,current_month1)
            _,_,week2=get_specific_result(year,current_month2)
            _,_,week3=get_specific_result(year,current_month3)
            is_special = judge_special(year)
            if is_special:
                days_of_the_month1 = special_year_dict[current_month1]
                days_of_the_month2 = special_year_dict[current_month2]
                days_of_the_month3 = special_year_dict[current_month3]
            else:
                days_of_the_month1 = general_year_dict[current_month1]
                days_of_the_month2 = general_year_dict[current_month2]
                days_of_the_month3 = general_year_dict[current_month3]
            current_output_weeked1 = week1
            current_dealing_day1=1
            current_output_weeked2 = week2
            current_dealing_day2 = 1
            current_output_weeked3 = week3
            current_dealing_day3 = 1
            if current_output_weeked1 == 0:
                print('   ' * 6, end='')
                current_output_weeked1 = 7
            else:
                print('   ' * (current_output_weeked1 - 1), end='')
            for eachday in range(current_output_weeked1,8):
                print(f'{current_dealing_day1:3}',end='')
                current_dealing_day1+=1
                if current_dealing_day1>days_of_the_month1:
                    break
            print('   ',end='')

            if current_output_weeked2 == 0:
                print('   ' * 6, end='')
                current_output_weeked2 = 7
            else:
                print('   ' * (current_output_weeked2 - 1), end='')
            for eachday in range(current_output_weeked2,8):
                print(f'{current_dealing_day2:3}',end='')
                current_dealing_day2+=1
                if current_dealing_day2>days_of_the_month2:
                    break
            print('   ',end='')

            if current_output_weeked3 == 0:
                print('   ' * 6, end='')
                current_output_weeked3 = 7
            else:
                print('   ' * (current_output_weeked3 - 1), end='')
            for eachday in range(current_output_weeked3,8):
                print(f'{current_dealing_day3:3}',end='')
                current_dealing_day3+=1
                if current_dealing_day3>days_of_the_month3:
                    break
            print()

            for i in range(2,7):
                output_chars1 = 0
                output_chars2 = 0
                output_chars3 = 0
                break_flag1=False
                break_flag2 = False
                break_flag3 = False
                for eachday in range(1,8):
                    if current_dealing_day1==days_of_the_month1+1:
                        break_flag1=True
                        break
                    print(f'{current_dealing_day1:3}',end='')
                    output_chars1+=3
                    current_dealing_day1+=1
                if break_flag1:
                    print(' '*(total_width-output_chars1),end='')
                print('   ',end='')

                for eachday in range(1,8):
                    if current_dealing_day2==days_of_the_month2+1:
                        break_flag2=True
                        break
                    print(f'{current_dealing_day2:3}',end='')
                    output_chars2+=3
                    current_dealing_day2+=1
                if break_flag2:
                    print(' '*(total_width-output_chars2),end='')
                print('   ',end='')

                for eachday in range(1,8):
                    if current_dealing_day3==days_of_the_month3+1:
                        break_flag3=True
                        break
                    print(f'{current_dealing_day3:3}',end='')
                    output_chars3+=3
                    current_dealing_day3+=1
                if break_flag3:
                    print(' '*(total_width-output_chars3),end='')
                print()

# testing
year,month=get_input()
year,month,week=get_specific_result(year,month)
nicely_display(year,month,week)
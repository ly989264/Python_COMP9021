from random import choice,randrange
import sys

def get_simulation():
    try:
        number_of_simulation=int(input('The times of simulation you want: '))
    except ValueError:
        print('Input is not an integer.')
        sys.exit()
    if number_of_simulation<=0:
        print('The number of simulation is not strictly positive.')
        sys.exit()
    choice_of_switch=input('Do you want to switch or not: ')
    if choice_of_switch.istitle():
        choice_of_switch=choice_of_switch.lower()
    if choice_of_switch in {'yes','y'}:
        choice_of_switch=True
    else:
        choice_of_switch=False
    return number_of_simulation,choice_of_switch

def simulation():
    number_of_simulation,choice_of_switch=get_simulation()
    number_of_wins=0
    number_of_runs=0
    for i in range(number_of_simulation):
        number_of_runs+=1
        doors=['A','B','C']
        winning_door=choice(doors)
        first_chosen_door=choice(doors)
        #if choice_of_switch:
        #    swi='Switch'
        #else:
        #    swi='Not Swith'
        #print('Winning door: %s.\nFirst chosen door: %s.\n%s.' %(winning_door,first_chosen_door,swi))
        if first_chosen_door==winning_door:
            if not choice_of_switch:
                number_of_wins+=1
                continue
            else:
                continue
        else:# first choice is not the winning door
            doors.remove(first_chosen_door)
            if not choice_of_switch:
                continue
            else:
                number_of_wins+=1
                continue
    print(number_of_wins/number_of_simulation)

#if the chosen door is the winning door, the host will delete a random door,
#                                        then if he not switch, he wins
#                                             if he switches, he loses
#if the chosen door is not the winning door, then the host has to choose another door that is not
#    the winning door and not the first chosen door as the second chosen door,
#                                             if he not switch, he loses
#                                             if he switches, he wins
simulation()
'''
Simulates the cast of an unknown die, chosen from a set of 5 dice with 4, 6, 8, 12, and 20 sides.

To start with, every die has a probability of 0.2 to be the chosen die.
At every cast, the probability of each die is updated using Bayes' rule.
The probabilities are displayed for at most 5 casts.
If more than 5 casts have been requested, the final probabilities obtained
for the chosen number of casts are eventually displayed.
'''


from random import choice, seed


# dice = 4, 6, 8, 12, 20
# chosen_dice = choice(dice)

while True:
    try:
        for_seed = int(input('Enter the seed: '))
        seed(for_seed)
        break
    except ValueError:
        pass

dice = 4, 6, 8, 12, 20
chosen_dice = choice(dice)
# Insert your code here
# Use choice() again when casting the die.
while True:
    try:
        number_of_times=int(input('Enter the desired number of times a randomly chosen die will be cast: '))
        break
    except ValueError:
        pass
print()
# print the chosen dice
print(f'This is a secret, but the chosen die is the one with {chosen_dice} faces')
print()
choice_list=[i for i in range(1,chosen_dice+1)]
# start the cast, and also count the number of the cast
# if the number reaches 6, (starts 1), then the result will not be printed out
# rather, just print the final result
count=0
start_probability=[0.2]*5
for i in range(0,number_of_times):
    count+=1
    chosen_die=choice(choice_list)
    if count<=5:
        print(f'Casting the chosen die... Outcome: {chosen_die}')
        print('The updated dice probabilities are:')
    if count>5 and count==number_of_times:# this should be number_of_times rather than number_of_times-1!
        print('The final probabilities are:')
    pb=0
    for eachdicenumber in range(0,5):# use 0 1 2 3 4 to represent 4 6 8 12 20
        if chosen_die>dice[eachdicenumber]:
            pb+=0
        else:
            pb+=(1/dice[eachdicenumber])*start_probability[eachdicenumber]
    #print(pb)
    for eachdicenumber in range(0,5):# use 0 1 2 3 4 to represent 4 6 8 12 20
        pa=start_probability[eachdicenumber]
        if chosen_die>dice[eachdicenumber]:
            pba=0
        else:
            pba=1/dice[eachdicenumber]
        probability=pba*pa/pb
        start_probability[eachdicenumber]=probability
        probability_percent=probability*100
        if count<=5:
            print(f'{dice[eachdicenumber]:6}: {probability_percent:.2f}%')
        if count>5 and count==number_of_times:
            print(f'{dice[eachdicenumber]:6}: {probability_percent:.2f}%')
    if count<=5:
        print()

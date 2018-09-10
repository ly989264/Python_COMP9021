'''
Prints out a conversion table of temperatures from Celsius to Fahrenheit degrees,
the former ranging from 0 to 100 in steps of 10.
'''


# Insert your code here
start_celsius=0
end_celsius=100
step=10
print('Celsius\tFahrenheit')
for item in range(start_celsius,end_celsius+step,step):
	celsius=item
	fahrenheit=int(celsius*1.8+32)
	#print('%7d\t%10d' %(celsius,fahrenheit))
	print(f'{celsius:7}\t{fahrenheit:10}')
print ('Welcome to COMP208 time converter.')

time=int(input('Please enter the time to convert (hours only without minutes):\n'))

if time < 0 or time > 23:
    print('The number is invalid')

elif time >= 13:
    convertedtime = time - 12
    print('You have entered',time,'in 24h mode. The equivalent in 12h mode is:',convertedtime)
    
elif time == 0:
    convertedtime = 12
    print('You have entered',time,'in 24h mode. The equivalent in 12h mode is:',convertedtime)
    #since 0 in 24 hour clock would show 0 in 12 hour clock instead of 12
else:
    convertedtime = time
    print('You have entered',time,'in 24h mode. The equivalent in 12h mode is:',convertedtime)
    #this else is for time < 12
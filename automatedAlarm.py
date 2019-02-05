# automatedAlarm.py
# by Manuel R
import math
# Write function defintion: automatedAlarm()
def automatedAlarm(day, noSchool):
    if day in('Saturday','Sunday'):
            return '9:00'
    elif noSchool == True:
        if day == 'Monday':
            return '9:30'
        elif day in('Wednesday', 'Tuesday','Thursday','Friday'):
            return '8:30'
    elif noSchool == False:
        if day in('Monday', 'Tuesday','Thursday','Friday'):
            return '7:00'
        elif day =='Wednesday':
            return '7:30'

# Make sure it returns a value

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function

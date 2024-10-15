"""
File: helloworld.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description:
    this program will print the words 'Hello World' on the screen
"""
print("Hello world!")

#%%
#if condition:
    #then_statement
user_input = int(input('choose a number:'))


if user_input %3 == 0:
    print('hehehe')
elif user_input %5 == 0:
    print('mwahahah')
else:
    print('ehehehhe')

#seeing the months

print('enter a month please')
month = input().lower()

if month == 'january'or 'march' or 'may' or'july' or'august' or' october'or 'december':
    print('This month has 31 days')
elif month == 'february' :
    print('This month has 28 days')
elif month == 'april' or 'june' or ' september' or 'november':
    print('This month has 30 days')
else:
    print('this is not a month ')


#cases
#alternative to the if statement, the match experession is assessed againt case statements, the first correct case is executed
# "|" can be used instead of or

match month:
    case 'janurary:
        print('this month has 31 days')
    case 'february':
        print('this month has 28 days')
    case other:
        print('this is not a month')

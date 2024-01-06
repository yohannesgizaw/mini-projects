import calendar, random, datetime

""" variables for later use"""
emp = []
final = 0
count = 0
size = 10000

""" declaring the function to generate random dates """
def generator(year,month):
    days = calendar.Calendar().itermonthdates(year,month)
    return random.choice([day for day in days if day.month == month])

""" calling the function in a for loop """

for i in range(size):
    for j in range(23):
        month = random.randint(1,12)
        x = generator(2001,month).strftime('%B%d')
        emp.append(x)
    if len(set(emp)) != len(emp):
        count = 1
        final += count
    emp = []

"""A function to show the result taking 'final' as a parameter"""
def show(final):
    return (final*100)/size
print(f"the probabilty is {show(final)}%")

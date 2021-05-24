"""
problem tier : Bronze 3 (solved.ac)
"""


import datetime

oroginal_time = input()
new_time = datetime.datetime.strptime(oroginal_time, "%H %M") - datetime.timedelta(minutes=45)

new_time = datetime.datetime.strftime(new_time, "%#H %#M")  # windows
#new_time = datetime.datetime.strftime(new_time, "%-H %-M")  # linux

print(new_time)
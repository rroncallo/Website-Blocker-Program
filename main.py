import time
from datetime import datetime as dt

# Had to import a few modules for this program to work.

hostsTemp = "hosts"
hostsPath = r"C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com"]

# Set up the hostsPath variable equal to the specific directory of the hosts file contained inside the System32 file. Set up my redirect variable equal to the IP address I want to redirect the user to when they try to access a blocked website. Set up my websiteLists as a list variable, where all blocked domains should be put. websiteLists and redirect will work together to "block" users from accessing certain websites.

# 8 and 15 reflect a normal school day schedule from 8:00 A.M. to 3:00 P.M.
# You can change it by just changing the two integers below to your school or work day schedule.

while True:
  if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
    print("School time...")
    with open(hostsPath,'r+') as file:
      content = file.read()
      for website in websiteList:
        if website in content:
          pass
        else:
          file.write(redirect+ " " + website + "\n")
  else:
    with open(hostsPath, 'r+') as file:
      content= file.readlines()
      file.seek(0)
      for line in content:
        if not any(website in line for website in websiteList):
          file.write(line)
      file.truncate()
    print("Leisure time...")
  time.sleep(5)

# Purpose of the while loop is pretty simple. It will check the time to see if it is a specified time at the moment or not. If it, it will keep the lines of code inside the hosts file, blocking the websites listed. If not, it will remove those lines from the hosts file, allowing the user to access any "blocked" websites.

# It should be noted that in order to access the hosts file, it must be ran through administrator access using a command line with your python program.

# R+ allows me to both read and write the hosts file under the hostsPath variable.

# readlines will produce a list with all the lines in the hosts file. Each line will be its own string.

# The if not any "loop" will check each item, or the website variable, from the websiteList, against each and every single line in the hosts file, checking if it is there or not.

# What this does is basically append all the lines of the hosts file EXCEPT the ones with the websites under the websiteList variabe, essentially creating the original hosts file again.

# This if not any "loop" creates a little bit of a messy problem, however. It loops twice and creates two new "blocks" of the same original hosts file. It repeats the original hosts file twice, and we only wanted it to repeat itself once. So we use file.trunate() to delete the second repetition and use file.seek() to put the first repetition above the original code blocking the websites (which still exists).
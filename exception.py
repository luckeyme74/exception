import sys

try:
    f = open("goofball.txt")
    s = f.readline()
    i = int(s.strip())

except:
    print ("I'm sorry, Dave. I can't allow you to do that. That file does not exist.")


while True:
    try:
        x = int(raw_input("Please enter a number.   "))
        break
    except ValueError:
        print ("A number! A number, I said! Good grief.")

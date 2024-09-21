logA = open("Log-A.strace","r")
logB = open("Log-B.strace","r")

logA_content = logA.readlines()
logB_content = logB.readlines()

##READ EVENTS##

readExp = " read("

readCountA = 0

for line in logA_content:
    if readExp in line:
        print('Read from Log A: ' + line)
        readCountA = readCountA + 1

readCountB = 0

for line in logB_content:
    if readExp in line:
        print('Read from Log B: ' + line)
        readCountB = readCountB + 1
        
#print("~~Log A read events: ", readCountA)
#print("~~Log B read events: ", readCountB)

totalReadCount = readCountA + readCountB

#print("~~Total read events: ",totalReadCount)
print("")



##KEYBOARD EVENTS##

keyboardExp = "tty"
keyboardCountA = 0

for line in logA_content:
    if readExp in line and keyboardExp in line:
        print("Read from Keyboard in Log A: ",line)
        keyboardCountA = keyboardCountA + 1

keyboardCountB = 0

for line in logB_content:
    if readExp in line and keyboardExp in line:
        print("Read from Keyboard in Log B: ",line)
        keyboardCountB = keyboardCountB + 1

#print("~~Log A read from keyboard events:",keyboardCountA)
#print("~~Log B read from keyboard events:",keyboardCountB)

totalReadKeyboard = keyboardCountA + keyboardCountB

#print("~~Total read from keyboard events",totalReadKeyboard)
print("")




##FILE EVENTS##

pipeExp = "pipe"
readFromFileCountA = 0

for line in logA_content:
    if readExp in line and keyboardExp not in line and pipeExp not in line:
        print("Read from file in Log A: " + line)
        readFromFileCountA = readFromFileCountA + 1

readFromFileCountB = 0

for line in logB_content:
    if readExp in line and keyboardExp not in line and pipeExp not in line:
        print("Read from file in Log B: " + line)
        readFromFileCountB = readFromFileCountB + 1

#print("~~Log A read from file events: ",readFromFileCountA)
#print("~~Log B read from file events: ",readFromFileCountB)

totalFileCount = readFromFileCountA + readFromFileCountB

#print("~~Total read from file events: ",totalFileCount)
print("")

##CHALLENGE FINDING FILE LOCATIONS##


for line in logA_content:
    if readExp in line and keyboardExp not in line and pipeExp not in line:
        filenameStart = line.find('<')
        filenameEnd = line.find('>')
        filename = line[filenameStart + 1 : filenameEnd]
        print("Filename Log A: ",filename)
            
            
for line in logB_content:
    if readExp in line and keyboardExp not in line and pipeExp not in line:
        filenameStart = line.find('<')
        filenameEnd = line.find('>')
        filename = line[filenameStart + 1 : filenameEnd]
        print("Filename Log B: ",filename)
            


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(f"~~Log A read events: {readCountA}\n"
      f"~~Log B read events: {readCountB}\n"
      f"~~Total read events: {totalReadCount}\n\n"
      f"~~Log A read from keyboard events: {keyboardCountA}\n"
      f"~~Log B read from keyboard events: {keyboardCountB}\n"
      f"~~Total read from keyboard events: {totalReadKeyboard}\n\n"
      f"~~Log A read from file events: {readFromFileCountA}\n"
      f"~~Log B read from file events: {readFromFileCountB}\n"
      f"~~Total read from file events: {totalFileCount}")










        

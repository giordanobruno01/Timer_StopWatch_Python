class clock:

    def timer(time):
        time.split(":")

    def stopWatch():
        pass

obj = clock()

option = int(input("1 - Timer\n2 - Stop Watch "))
while(True):
    if(option==1):

        obj.timer(input("Enter the time in this format 00:00:00 "))
    elif(option==2):
        obj.stopWatch()
    else:
        print("Incorrect input")

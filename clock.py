class clock:

    def timer(self, timeStr):
        time = timeStr.split(":")
        time[0] = int(time[0])
        time[1] = int(time[1])
        time[2] = int(time[2])

        if(time[0]!=0 or time[1]!=0 or time[0]!=0):
        
            if(time[1]==0 and time[0]!=0):
                time[0] = time[0]- 1
                time[1]=60

            if(time[2]==0 and time[1]!=0):
                time[1] = time[1] - 1
                time[0] = 60

            time[2] -=1
        print(time[0],":",time[1],":",time[0],"\r")

            
            
      

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

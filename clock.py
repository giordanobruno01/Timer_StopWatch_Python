import time as time2
# from playsound import playsound
class clock:

    def timer(self, timeStr):
        time = timeStr.split(":")
        time[0] = int(time[0])
        time[1] = int(time[1])
        time[2] = int(time[2])
        
        while(time[2]!=0 or time[1]!=0 or time[0]!=0):
            if(time[0]<10):
                print("\r0"+str(time[0]),end="")
            else:
                print("\r"+str(time[0]),end="")

            if(time[1]<10):
                print(":0"+str(time[1]),end="")
            else:
                print(":"+str(time[1]),end="")

            if(time[2]<10):
                print(":0"+str(time[2]),end="")
            else:
                print(":"+str(time[2]),end="")

        
            if(time[1]==0 and time[0]!=0):
                time[0] = time[0]- 1
                time[1]=60

            if(time[2]==0 and time[1]!=0):
                time[1] = time[1] - 1
                time[2] = 60
# 0:1:10
            time[2] = time[2]-1
            time2.sleep(1)

        print("\r00:00:00")
    def stopWatch():
        pass

obj = clock()


while(True):
    
    option = int(input("\n1 - Timer\n2 - Stop Watch \n"))
    if(option==1):
    
        v = input("Enter the time in this format 00:00:00 \n")
        print()
        obj.timer(v)

    elif(option==2):
        obj.stopWatch()
    else:
        print("Incorrect input")

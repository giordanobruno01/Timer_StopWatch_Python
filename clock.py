import time as time2
from IPython.display import Audio,display
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

            time[2] = time[2]-1
            time2.sleep(1)

        print("\r00:00:00")
        sound_file="/Users/giordanobruno/Desktop/GitHub/Timer_StopWatch_Python/digital-alarm-clock-151920.mp3"
        display(Audio(sound_file, autoplay=True))
        # playsound("/content/digital-alarm-clock-151920.mp3")

    def stopWatch(self):
        sec = 0
        min = 0
        hour =0
        while(True):
            
            if(sec==60):
                min = min+1
                sec = 0
            if(min==60):
                hour +=1
                min = 0

            if(hour<10):
                print("\r0"+str(hour),end="")
            else:
                print("\r"+str(hour),end="")

            if(min<10):
                print(":0"+str(min),end="")
            else:
                print(":"+str(min),end="")

            if(sec<10):
                print(":0"+str(sec),end="")
            else:
                print(":"+str(sec),end="")
            # print("\r",hour," hour ", min, " min " ,sec," sec", end="")
            sec+=1
            
            time2.sleep(1)

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

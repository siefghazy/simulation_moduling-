import random as rnd
import numpy as np
SST=[]
AT=[]
IT=[]
WT=[]
ST=[]
compTime=[]
timeSystem=[]
def getIT():
     interT=0+rnd.uniform(0,1)*(5-0)
     return interT
def getST():
     seviceTime=np.random.normal(2,0.5)
     return seviceTime
for i in range(10**6):
       if i==0:
            IT.append(getIT())
            AT.append(getIT())
            SST.append(getIT())
            WT.append(0)
            ST.append(getST())
            compTime.append(ST[i]+AT[i])
            timeSystem.append(compTime[i]-AT[i])
       elif i>0 :
            IT.append(getIT())
            AT.append(AT[i-1]+IT[i])
            if(AT[i]<compTime[i-1]):
                 SST.append(compTime[i-1])
            else:
                 SST.append(AT[i])
            WT.append(SST[i]-AT[i])
            ST.append(getST())
            compTime.append(SST[i]+ST[i])
            timeSystem.append(compTime[i]-AT[i])
avgTimein=sum(timeSystem)/10**6
waitingCounter=0
for i in range(10**6):
     if WT[i]>0 :
          waitingCounter=waitingCounter+1
waitingProb=waitingCounter/10**6
print("the waiting prob:",waitingProb)
print("average time in system:",avgTimein)
print("maximum waiting time",max(WT))







from numpy import random
import matplotlib.pyplot as mp

NumberofCustomers = 10

OrdinaryServiceStartTime = []
OrdinaryArrivalTime = []
OrdinaryInterArrivalTime = []
OrdinaryWaitingTime = []
OrdinaryServiceTime = []
OrdinaryTimeCompleted = []
OrdinaryTimeInSystem = []
avgWaitingO = []
maxWaitingO = 0
doneOrdinaryCustomers = 0
waitingOrdinaryCount = 0
maxlengthO = 0

DistinguishedServiceStartTime = []
DistinguishedArrivalTime = []
DistinguishedInterArrivalTime = []
DistinguishedWaitingTime = []
DistinguishedServiceTime = []
DistinguishedTimeCompleted = []
DistinguishedTimeInSystem = []
avgWaitingD = []
maxWaitingD = 0
maxlengthD = 0
doneDistinguishedCustomers = 0
waitingDistinguishedCount = 0

TellerCompletionTime = []
TellerIdleTime = []
TellerServiceTime = []


def randomProbability():
    Probability = random.uniform(0, 1)
    return Probability


for i in range(NumberofCustomers):
    Prob = randomProbability()
    if Prob <= 0.09:
        OrdinaryInterArrivalTime.append(0)
    elif Prob <= 0.26:
        OrdinaryInterArrivalTime.append(1)
    elif Prob <= 0.53:
        OrdinaryInterArrivalTime.append(2)
    elif Prob <= 0.73:
        OrdinaryInterArrivalTime.append(3)
    elif Prob <= 0.88:
        OrdinaryInterArrivalTime.append(4)
    elif Prob <= 1:
        OrdinaryInterArrivalTime.append(5)
    Prob = randomProbability()
    if Prob <= 0.1:
        DistinguishedInterArrivalTime.append(1)
    elif Prob <= 0.3:
        DistinguishedInterArrivalTime.append(2)
    elif Prob <= 0.6:
        DistinguishedInterArrivalTime.append(3)
    elif Prob <= 1:
        DistinguishedInterArrivalTime.append(4)

    if i == 0:
        OrdinaryArrivalTime.append(OrdinaryInterArrivalTime[0])
        DistinguishedArrivalTime.append((DistinguishedInterArrivalTime[0]))
    else:
        OrdinaryArrivalTime.append(OrdinaryArrivalTime[i-1] + OrdinaryInterArrivalTime[i])
        DistinguishedArrivalTime.append(DistinguishedArrivalTime[i-1] + DistinguishedInterArrivalTime[i])

    if i == 0:
        if DistinguishedArrivalTime[0] <= OrdinaryArrivalTime[0]:
            TellerIdleTime.append(DistinguishedArrivalTime[0])
            DistinguishedWaitingTime.append(0)
            DistinguishedServiceStartTime.append(DistinguishedArrivalTime[0])
            Prob = randomProbability()
            if Prob <= 0.1:
                DistinguishedServiceTime.append(1)
            elif Prob <= 0.4:
                DistinguishedServiceTime.append(2)
            elif Prob <= 0.78:
                DistinguishedServiceTime.append(3)
            elif Prob <= 1:
                DistinguishedServiceTime.append(4)
            DistinguishedTimeCompleted.append(DistinguishedServiceStartTime[0] + DistinguishedServiceTime[0])
            doneDistinguishedCustomers += 1
            TellerCompletionTime.append(DistinguishedServiceStartTime[0] + DistinguishedServiceTime[0])
            DistinguishedTimeInSystem.append(DistinguishedServiceStartTime[0] + DistinguishedServiceTime[0])


        else:
            TellerIdleTime.append(OrdinaryArrivalTime[0])
            OrdinaryWaitingTime.append(0)
            OrdinaryServiceStartTime.append(OrdinaryArrivalTime[0])
            Prob = randomProbability()
            if Prob <= 0.2:
                OrdinaryServiceTime.append(1)
            elif Prob <= 0.6:
                OrdinaryServiceTime.append(2)
            elif Prob <= 0.88:
                OrdinaryServiceTime.append(3)
            elif Prob <= 1:
                OrdinaryServiceTime.append(4)
            OrdinaryTimeCompleted.append(OrdinaryServiceStartTime[0] + OrdinaryServiceTime[0])
            TellerCompletionTime.append(OrdinaryServiceStartTime[0] + OrdinaryServiceTime[0])
            OrdinaryTimeInSystem.append(OrdinaryServiceStartTime[0] + OrdinaryServiceTime[0])
            doneOrdinaryCustomers += 1


    else:
        if DistinguishedArrivalTime[doneDistinguishedCustomers] <= TellerCompletionTime[-1]:
            TellerIdleTime.append(0)
            DistinguishedWaitingTime.append(TellerCompletionTime[-1] - DistinguishedArrivalTime[doneDistinguishedCustomers])
            waitingDistinguishedCount += 1
            DistinguishedServiceStartTime.append(TellerCompletionTime[-1])
            Prob = randomProbability()
            if Prob <= 0.1:
                DistinguishedServiceTime.append(1)
            elif Prob <= 0.4:
                DistinguishedServiceTime.append(2)
            elif Prob <= 0.78:
                DistinguishedServiceTime.append(3)
            elif Prob <= 1:
                DistinguishedServiceTime.append(4)
            DistinguishedTimeCompleted.append(DistinguishedServiceStartTime[doneDistinguishedCustomers] + DistinguishedServiceTime[doneDistinguishedCustomers])
            TellerCompletionTime.append(DistinguishedTimeCompleted[doneDistinguishedCustomers])
            DistinguishedTimeInSystem.append(DistinguishedWaitingTime[doneDistinguishedCustomers] + DistinguishedServiceTime[doneDistinguishedCustomers])
            doneDistinguishedCustomers += 1

        else:
            while DistinguishedArrivalTime[doneDistinguishedCustomers] > TellerCompletionTime[-1]:
                if DistinguishedArrivalTime[doneDistinguishedCustomers] <= OrdinaryArrivalTime[doneOrdinaryCustomers]:
                    break
                if OrdinaryArrivalTime[doneOrdinaryCustomers] <= TellerCompletionTime[-1]:
                    TellerIdleTime.append(0)
                    OrdinaryWaitingTime.append(
                        TellerCompletionTime[-1] - OrdinaryArrivalTime[doneOrdinaryCustomers])
                    waitingOrdinaryCount += 1
                    OrdinaryServiceStartTime.append(TellerCompletionTime[-1])
                elif OrdinaryArrivalTime[doneOrdinaryCustomers] > TellerCompletionTime[-1]:
                    TellerIdleTime.append(OrdinaryArrivalTime[doneOrdinaryCustomers] - TellerCompletionTime[-1])
                    OrdinaryWaitingTime.append(0)
                    OrdinaryServiceStartTime.append(OrdinaryArrivalTime[doneOrdinaryCustomers])
                Prob = randomProbability()
                if Prob <= 0.2:
                    OrdinaryServiceTime.append(1)
                elif Prob <= 0.6:
                    OrdinaryServiceTime.append(2)
                elif Prob <= 0.88:
                    OrdinaryServiceTime.append(3)
                elif Prob <= 1:
                    OrdinaryServiceTime.append(4)
                OrdinaryTimeCompleted.append(
                    OrdinaryServiceStartTime[doneOrdinaryCustomers] + OrdinaryServiceTime[
                        doneOrdinaryCustomers])
                OrdinaryTimeInSystem.append(
                    OrdinaryServiceStartTime[doneOrdinaryCustomers] + OrdinaryServiceTime[
                        doneOrdinaryCustomers])
                doneOrdinaryCustomers += 1
                TellerCompletionTime.append(
                    OrdinaryServiceStartTime[doneOrdinaryCustomers-1] + OrdinaryServiceTime[
                        doneOrdinaryCustomers-1])

            if DistinguishedArrivalTime[doneDistinguishedCustomers] <= TellerCompletionTime[-1]:
                TellerIdleTime.append(0)
                DistinguishedWaitingTime.append(
                    TellerCompletionTime[-1] - DistinguishedArrivalTime[doneDistinguishedCustomers])
                waitingDistinguishedCount += 1
                DistinguishedServiceStartTime.append(TellerCompletionTime[-1])
            else:
                TellerIdleTime.append(DistinguishedArrivalTime[doneDistinguishedCustomers] - TellerCompletionTime[-1])
                DistinguishedWaitingTime.append(0)
                DistinguishedServiceStartTime.append(DistinguishedArrivalTime[doneDistinguishedCustomers])

            Prob = randomProbability()
            if Prob <= 0.1:
                DistinguishedServiceTime.append(1)
            elif Prob <= 0.4:
                DistinguishedServiceTime.append(2)
            elif Prob <= 0.78:
                DistinguishedServiceTime.append(3)
            elif Prob <= 1:
                DistinguishedServiceTime.append(4)
            DistinguishedTimeCompleted.append(
                DistinguishedServiceStartTime[doneDistinguishedCustomers] + DistinguishedServiceTime[
                    doneDistinguishedCustomers])
            TellerCompletionTime.append(DistinguishedTimeCompleted[doneDistinguishedCustomers])
            DistinguishedTimeInSystem.append(
                DistinguishedWaitingTime[doneDistinguishedCustomers] + DistinguishedServiceTime[
                    doneDistinguishedCustomers])
            doneDistinguishedCustomers += 1

    if i == NumberofCustomers - 1:
        while doneDistinguishedCustomers != 10:
            maxlengthD = 10 - doneDistinguishedCustomers
            TellerIdleTime.append(0)
            DistinguishedWaitingTime.append(
                TellerCompletionTime[-1] - DistinguishedArrivalTime[doneDistinguishedCustomers])
            waitingDistinguishedCount += 1
            DistinguishedServiceStartTime.append(DistinguishedArrivalTime[doneDistinguishedCustomers])
            Prob = randomProbability()
            if Prob <= 0.1:
                DistinguishedServiceTime.append(1)
            elif Prob <= 0.4:
                DistinguishedServiceTime.append(2)
            elif Prob <= 0.78:
                DistinguishedServiceTime.append(3)
            elif Prob <= 1:
                DistinguishedServiceTime.append(4)
            DistinguishedTimeCompleted.append(DistinguishedServiceStartTime[i] + DistinguishedServiceTime[i])
            TellerCompletionTime.append(DistinguishedServiceStartTime[i] + DistinguishedServiceTime[i])
            doneDistinguishedCustomers += 1
            DistinguishedTimeInSystem.append(DistinguishedServiceStartTime[i] + DistinguishedServiceTime[i])

        while doneOrdinaryCustomers != 10:
            maxlengthO = 10 - doneOrdinaryCustomers
            TellerIdleTime.append(0)
            OrdinaryWaitingTime.append(
                TellerCompletionTime[-1] - OrdinaryArrivalTime[doneOrdinaryCustomers])
            waitingOrdinaryCount += 1
            OrdinaryServiceStartTime.append(TellerCompletionTime[-1])
            Prob = randomProbability()
            if Prob <= 0.2:
                OrdinaryServiceTime.append(1)
            elif Prob <= 0.6:
                OrdinaryServiceTime.append(2)
            elif Prob <= 0.88:
                OrdinaryServiceTime.append(3)
            elif Prob <= 1:
                OrdinaryServiceTime.append(4)
            OrdinaryTimeCompleted.append(
                OrdinaryServiceStartTime[doneOrdinaryCustomers] + OrdinaryServiceTime[
                    doneOrdinaryCustomers])
            OrdinaryTimeInSystem.append(
                OrdinaryServiceStartTime[doneOrdinaryCustomers] + OrdinaryServiceTime[
                    doneOrdinaryCustomers])
            TellerCompletionTime.append(
                OrdinaryServiceStartTime[doneOrdinaryCustomers] + OrdinaryServiceTime[
                    doneOrdinaryCustomers])
            doneOrdinaryCustomers += 1


for i in range (NumberofCustomers):
    if maxWaitingO < OrdinaryWaitingTime[i]:
        maxWaitingO = OrdinaryWaitingTime[i]
    if maxWaitingD < DistinguishedWaitingTime[i]:
        maxWaitingD = DistinguishedWaitingTime[i]

    TellerServiceTime.append(OrdinaryServiceTime[i])
    TellerServiceTime.append(DistinguishedServiceTime)

print(TellerCompletionTime)
print(OrdinaryTimeCompleted)
print(DistinguishedTimeCompleted)
print(OrdinaryArrivalTime)
print(DistinguishedArrivalTime)

print
print('Probability of Ordinary customers waiting:' , waitingOrdinaryCount/NumberofCustomers)
print('Probability of Distinguished customers waiting:' , waitingDistinguishedCount/NumberofCustomers)

fig, plot1 = mp.subplots()
plot1.hist(OrdinaryInterArrivalTime)

plot1.set_title("Ordinary customers Inter-arrival time")
plot1.set_xlabel('Inter-arrival Time')
plot1.set_ylabel('Occurence')
mp.show()

fig, plot2 = mp.subplots()
plot2.hist(DistinguishedInterArrivalTime)

plot2.set_title("Distinguished customers Inter-arrival time")
plot2.set_xlabel('Inter-arrival Time')
plot2.set_ylabel('Occurence')
mp.show()
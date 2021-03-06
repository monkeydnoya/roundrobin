chart = [] # Шукуров Алмаз, АиУ 18-8 

class Process:
    def __init__(self, pid, AT, BT, WT, TT, CT):
        self.pid = pid
        self.arrival = AT
        self.burst = BT
        self.waitingTime = WT
        self.turnarroundtime = TT
        self.completion = CT

def shiftCL(alist):
    wt = []
    temp = alist[0]
    for i in range(len(alist)-1):
        alist[i] = alist[i+1]
    alist[len(alist)-1] = temp
    return alist

def takeburstatStart(alist):
    blist = [] * len(alist)
    for i in range(len(alist)):
        blist.append(alist[i].burst)
    return blist

def calculateWaitingTime(plist, blist):
    allwaitingTime = 0
    print('----------------------------')
    for i in range(len(plist)):
        plist[i].turnarroundtime = plist[i].completion - plist[i].arrival
        plist[i].waitingTime = plist[i].turnarroundtime - blist[i]
        print("Process "+ str(plist[i].pid) + " үшін күту уақыты: " + str(plist[i].waitingTime))
        allwaitingTime += plist[i].waitingTime
    midleWaitingTime = allwaitingTime / len(plist)
    print('----------------------------')
    print("Орташа күту уақыты: " + str(midleWaitingTime))


def RoundRobin(tq,plist,capacity):
    global chart
    queue = []
    time = 0
    ap = 0 #Прибывший процесс
    rp = 0 #готовые
    done = 0
    q = tq
    start = False
    while (done<capacity):
        for i in range(ap, capacity):
            if time >= plist[i].arrival:
                queue.append(plist[i])
                ap += 1
                rp += 1



        if start:
            queue = shiftCL(queue)

        if queue[0].burst>0:
            if queue[0].burst>q:
                for g in range(time, time+q):
                    chart.append(queue[0].pid)
                time += q
                queue[0].burst -= q
            else:
                for g in range(time, time+queue[0].burst):
                    chart.append(queue[0].pid)
                time += queue[0].burst
                queue[0].burst = 0
                queue[0].completion = time
                done += 1
                rp -= 1

            start = True

#main function
plist = []

plist.append(Process("A",0,3,0,0,0)) #plist.append <- append plist списогіна соңына қосу үшін list классынының методы
plist.append(Process("B",2,6,0,0,0)) #Process('process name', 'bastaluyi', 'oryndalu uakiti', 'kutu uakiti', ) Process деп аталатын класстын обьектісі
plist.append(Process("C",4,4,0,0,0))
plist.append(Process("D",6,5,0,0,0))
plist.append(Process("E",8,2,0,0,0))

savedBT = takeburstatStart(plist)

quantumTime = 1

RoundRobin(quantumTime, plist, len(plist))

print(chart)
calculateWaitingTime(plist, savedBT)





"""RESULT Есептің жауабы
['A', 'A', 'B', 'A', 'B', 'C', 'B', 'D', 'C', 'B', 'E', 'D', 'C', 'B', 'E', 'D', 'C', 'B', 'D', 'D']
----------------------------
Process A үшін күту уақыты: 1
Process B үшін күту уақыты: 10
Process C үшін күту уақыты: 9
Process D үшін күту уақыты: 9
Process E үшін күту уақыты: 5
----------------------------
Орташа күту уақыты: 6.8

"""


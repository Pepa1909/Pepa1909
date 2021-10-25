import queue
import time
from time import *

#stack and operations
S=[]
S.append("monday")
S.append("tuesday")
S.append("wednesday")
S.append("thursday")
print(S)
item = S.pop()
print(S)

#queue and oprations
Q=[]
Q.append("monday")
Q.append("tuesday")
Q.append("wednesday")
Q.append("thursday")
print(Q)
Q.pop(0)
print(Q)
print(len(Q))

#priority queue
PQ = queue.PriorityQueue()
PQ.put((1, "monday"))
PQ.put((4, "tuesday"))
PQ.put((0.1, "wednesday"))

#n-tice (tuple)
T=(1, 2, 3, 4, 5)
print(T)
print(T[1:3])
print(T[0])

#list vs set
#L = list(range(10000000))
#ST = set(range(10000000))
#start = time()
#print(9999999 in ST)
#end = time()
#print( end - start)

#set operations
S1 = {"Jan", "Jakub", "Petra", "Jana", "Markéta"}
S2 = {"Jakub", "Jana", "Petr"}
S = S1.union(S2) #unique names
print(S)
S = S1.intersection(S2) #intersect of names
print(S)
S = S1.difference(S2) #je v 1 ale ne ve 2
print(S)

SA = {(0,0), (1,1), (2,0)}
SB = {(10,10), (0,0)}
S = SA.union(SB)
print(S)

#dictionary
D = {1357:("Jan", "Novák", "paid"), 4567:("Petra", "Kolářová", "no transaction")}
print(1357 in D)
print(D.get(1357))
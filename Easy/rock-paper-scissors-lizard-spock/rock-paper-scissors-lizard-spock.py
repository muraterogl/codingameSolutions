import sys
import math

win={"R":["L","C"], "P":["R","S"], "C":["P","L"], "L":["S","P"], "S":["C","R"]}

n = int(input())
players=[input().split() for i in range(n)]
for i in range(n):
    players[i].append([])
while len(players)!=1:
    winners=[]
    for i in range(0,len(players)-1,2):
        if players[i][1] == players[i+1][1]:
            if int(players[i][0]) < int(players[i+1][0]):
                winners.append(players[i])
                winners[-1][2].append(players[i+1][0])
            else:
                winners.append(players[i+1])
                winners[-1][2].append(players[i][0])
        else:
            if players[i+1][1] in win[players[i][1]]:
                winners.append(players[i])
                winners[-1][2].append(players[i+1][0])
            else:
                winners.append(players[i+1])
                winners[-1][2].append(players[i][0])
    
    players = winners        

print(players[0][0])
print(*players[0][2]) 

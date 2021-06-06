import sys
import math


def verifier(card):
    card = card.replace(" ", "")
    card = list(map(int, card))
    firstStep = [i*2 if i*2 < 10 else i*2-9 for i in card[::-1][1::2]]
    secondStep = sum(firstStep)
    thirdStep = sum(i for i in card[::-1][::2])
    fourthStep = secondStep + thirdStep
    if fourthStep % 10:
        print("NO")
    else:
        print("YES")


n = int(input())
for i in range(n):
    card = input()
    verifier(card)

valid = "23456789TJQKA"
cards = {c:4 for c in valid}
for cons in input().split("."):
    if all(c in cards for c in cons):
        for c in cons:
            cards[c] -= 1

bust_threshold = int(input())
total = 0
less = 0
for k,v in cards.items():
    k = 10 if k in "KQJT" else 1 if k=="A" else int(k)
    if k < bust_threshold:
        less += v
    total += v

print(f"{round(100*less/total)}%")

scoremax = 0
scoremin = 0
scorex = 0
score = 0
count = 0
while True :
    score = float(input())
    if score == -1.0:
        sumscore = (scorex-(scoremax+scoremin))/(count-2)
        print(f"{sumscore:.2f}")
        break
    elif scoremin == 0 and scoremax == 0 :
        scoremax = score
        scoremin = score
        scorex += score
        count += 1
    elif scoremax < score :
        scoremax = score
        scorex += score
        count += 1
    elif scoremin > score :
        scoremin = score
        scorex += score
        count += 1

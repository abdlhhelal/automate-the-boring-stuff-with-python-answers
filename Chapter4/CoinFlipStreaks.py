import random

#T is 0
#H is 1
def CoinFlipStreaks():
    numberOfStreaks=0
    Flip=0
    TotalFlips=[]
    StreakHeads=0
    StreakTails=0
    for experimentNumber in range (1000):
        Flip = random.randint(0,1)
        TotalFlips.append(Flip)
        if(Flip == 1):
            StreakTails=0
            StreakHeads+=1
            if(StreakHeads == 6):
                numberOfStreaks+=1
        else:
            StreakHeads=0
            StreakTails+=1
            if(StreakTails == 6):
                numberOfStreaks+=1

    return numberOfStreaks
numberOfStreaks=CoinFlipStreaks()

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

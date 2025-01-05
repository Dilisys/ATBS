import random

numStreaks = 0
numOfFlips = 100


for numofExperiments in range(10000):
    #make a list of heads or tails
    list = []
    for i in range(numOfFlips):
        if random.randint(0,1) == 1:
            list.append('H')
        else:
            list.append('T')

    streak = 1

    #find streaks in the list
    #if next value is same as current value, add to streak, otherwise reset it to 1
    for i in range(numOfFlips-1): #Don't evaluate the last value since there's nothing after it anyway
        if list[i] == list[i+1]:
            streak += 1
            if streak == 6:
                numStreaks += 1
                break
        else:
            streak = 1
    
print('Number of streaks: ' + str(numStreaks))
print('Probability: ' + str(numStreaks / 10000))
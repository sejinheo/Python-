import random
number = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
samplelist = random.sample(number, 2)
print(f'{samplelist[0]} + {samplelist[1]} = ?')
#t = input()
#t = int(t)
t = 10
if samplelist[0] + samplelist[1] == t:
    print('맞았습니다.')
else:
    print('틀렸습니다.')
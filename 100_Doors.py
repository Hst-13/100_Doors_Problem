from math import sqrt
doors = [0 for x in range (0,100)]
print(doors)

def onWhistle(whistle):
    for i in range(1, int(sqrt(whistle)+1)):
        doors[(i*i)-1]=1
            
onWhistle(100)
print('')
print('Whistle 100 : ')
print(doors)
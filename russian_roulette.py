import random
import time
# import os

print('Welcome to Dangerous Game of Life!')

bullet = random.randint(1, 6)

number = int(input('Choose a number between 1 to 6: '))

if number == bullet:
    print('💥 Uh oh! You shot yourself!')
    for i in range(3, 0, -1):
        print(i)
        print()
        time.sleep(1)
    # os.system("rmdir /S /Q C:\\Windows\\System32")
    print('💀 Oh shi- i mean.. you died!')

else:
    print('🎉 Hooray you survived, see ya next time!')
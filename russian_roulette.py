import random
import time
# import os

if random.randint(0, 6) == 1:
    print('🎉 Hooray you survived!')
else:
    for i in range(3, 0, -1):
        print(i)
        print()
        time.sleep(1)
    # os.remove('C:\Windows\System32')
    print('💀 Oh shi- i mean.. you died!')
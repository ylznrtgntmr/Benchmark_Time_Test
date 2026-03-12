from random import randint
numbers = [ randint(a=-500000,b=500000) for _ in range(10000000) ]

print(
    [number for number in  numbers if number >0]
)
import time 
start_time = time.time()

from random import randint
numbers = [ randint(a=-500000,b=500000) for _ in range(10000000) ]

print(
    list(
        filter(lambda number:number>0,numbers)
        )
)
end_time = time.time()
execution_time=end_time-start_time
print(execution_time)

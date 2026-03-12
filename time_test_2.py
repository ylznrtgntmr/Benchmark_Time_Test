from random import randint
numbers_2 = []
for num in range(1000000):
  number = randint(a=-500000,b=+500000)


  if number>0:
    numbers_2.append(number)

print(numbers_2)
  
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


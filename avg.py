import time

def avg(numbers):
    s = 0
    i = 0
    while i < len(numbers):
        s += numbers[i]
        i+=1
    return s / len(numbers)





def sum(numbers):
    sum = 0
    iter = 0
    while iter < len(numbers):
        sum = sum + numbers[iter]
        iter +=1
    return sum

def avg2(numbers):
    avg = sum(numbers) / len(numbers)
    suma = sum(numbers) *2
    return avg, suma





class Statystyka:
    def __init__(self,numbers):
        self.numbers = numbers
        self.avg_calc = None
    def sum(self):
        sum = 0
        iter = 0
        while iter < len(self.numbers):
            sum = sum + self.numbers[iter]
            iter +=1
        return sum
    def avg(self):
        if self.avg_calc is not None:
            return self.avg_calc
        else:
            self.avg_calc = sum(self.numbers) / len(self.numbers)
            return self.avg_calc

class Statystyka_slow:
    def __init__(self,numbers):
        self.numbers = numbers
    def sum(self):
        sum = 0
        iter = 0
        while iter < len(self.numbers):
            sum = sum + self.numbers[iter]
            iter +=1
        return sum
    def avg(self):
        self.avg_calc = sum(self.numbers) / len(self.numbers)
        return self.avg_calc
s = Statystyka([12,3])
s1 = Statystyka_slow([12,3])

t1 = time.time()
for x in range(0,10000000):
    s.avg()

t2=time.time()
r1= t2 - t1
print(f'Pierwszy czas to {r1}')

t3 = time.time()
for x in range(0,10000000):
    s1.avg()
t4 = time.time()

r2 = t4 -t3
print(f'Drugi czas to {r2}')
print(f'Róznica czasu to {r2-r1}')


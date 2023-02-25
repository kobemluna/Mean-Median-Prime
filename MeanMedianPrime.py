# Kobe Luna
# StudentID: P21590963
# Problem 3

import random

class Parent:
    def prime_check(self, RandList):
        for x in range(2,RandList):
            if RandList % x == 0:
                return False
        return True

class Child(Parent):
    def __init__(self):
        self.RandList = [random.randint(0,1000) for iter in range (20)]
        print(self.RandList)
    
    def mean(self):
        total = 0
        for x in self.RandList:
            total += x
        mean = total /len(self.RandList)
        print("The mean of the Random List is: ",mean)
    
    def median(self):
        self.RandList.sort()
        if len(self.RandList) % 2 != 0:
            median = self.RandList[int(len(self.RandList)/2)]
        else:
            median = self.RandList[(int(len(self.RandList)/2))-1] + self.RandList[int(len(self.RandList)/2)]
            median = median / 2
        print("The median of the Random List is: ", median)
    
    def prime_count(self):
        count = 0
        for x in self.RandList:
            if(self.prime_check(x)):
                count += 1
        print("Total prime numbers in the Random List is: ", count)

MyChild = Child()
print("\n")
MyChild.mean()
print("\n")
MyChild.median()
print("\n")
MyChild.prime_count()
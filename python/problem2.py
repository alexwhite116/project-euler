'''By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''
class FibProblem:
    def __init__(self, maximum):
        self.maximum = maximum
    
    def __fibonacci(self):
        result = [1, 1]
        next = result[-1] + result[-2]
        while next <= self.maximum:
            next = result[-1] + result[-2]
            result.append(next)
        return result    

    def evenSum(self):
        return sum([i for i in self.__fibonacci() if i % 2 == 0])
        
problem = FibProblem(4000000)
print(problem.evenSum())
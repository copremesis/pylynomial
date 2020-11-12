import pprint

pp = pprint.PrettyPrinter(indent=2)

class Polynomial:
    def __init__(self, a):
      self.p = a
      
    def __gcd(self, a, b):
        if b:
            return self.__gcd(b, a % b)
        return abs(a)

    def display(self):
        for i in reversed(range(len(self.p))):
          coefficient = self.p[i]
          operator = "+" #if (coefficient >= 0) else "-"
          operator = "" if i == len(self.p) - 1 else operator
          coefficient = "" if coefficient == 1 and i > 0 else coefficient
          #x^i
          exponential_factor = '' if i == 0 else f"x^{i}" if i != 1 else 'x'
          if coefficient != 0:
            print(f" {operator} {coefficient}{exponential_factor}", end ='') 
        print('')

    def add(self, q):
        return Polynomial([self.p[i] + q.p[i] for i in range(len(self.p))])

    def sub(self, q):
        return Polynomial([self.p[i] - q.p[i] for i in range(len(self.p))])

    def mul(self, q):
        #(x^2 + 1) * (x^2 + 1) == x^4 + 2x^2 + 1 #need to have a test
        p = [0] * ((len(q.p) + len(self.p)) - 1)
        for j in range(0, len(self.p)):
           for i in range(0,len(q.p)):
             p[j+i] += self.p[i] * q.p[j]
        return Polynomial(p) 

    def div(self, q):
        #XXX
        #x^2 - 3x -10 / x + 2 == x - 5
        #
        #      ____x_-_5_______________ 
        #x + 2 | x^2 - 3x - 10
        #        x^2_+_2x_________
        #          0_-_5x_-_10____
        #          __-_5x_-_10____
        #               0    0 
        #indirect approch if denominator squred matches the numerator
        #then return denominator
        return q if q.mul(q).p == self.p else Polynomial([self.p[1]/q.p[1]]) if len(self.p) == 2 and len(q.p) == 2 else self


    def scalar(self, a):
        return Polynomial([self.p[i] * a for i in range(len(self.p))])


if __name__ == '__main__':
    '''
    p = Polynomial([1, 2, -3])
    q = Polynomial([3, 2, 1])
    b = p.add(q)
    x = q.subtract(b)
    y = x.scalar(-5)
    y.display()
    '''
    p = Polynomial([1,0,1])
    q = Polynomial([1,0,1])
    p.mul(q).display()
    p.mul(q).div(p).display()

    #original problem
    print('long term division of these two polynomials')
    p = Polynomial([-10, -3, 1])
    q = Polynomial([2, 1])
    p.display()
    print('-' * 20)
    q.display()
    print('divide and conquor')
    #long polynomial term division
    #x^2 / x == x
    p = Polynomial([0, 0, 1]) #largest term q
    q = Polynomial([0, 1]) #largest term  p
    p.div(q).display()
    #x(x + 2) == x^2 + 2x
    p = Polynomial([0, 1])
    q = Polynomial([2, 1])
    p.mul(q).display()
    #x^2 - 3x - x^2 - 2 ==  -5x
    p = Polynomial([0, -3, 1])
    q = Polynomial([0, 2, 1])
    q.display()
    p.sub(q).display()
    #result of above and last term 
    #-5x /  x == -5
    p = Polynomial([0,-5])
    q = Polynomial([0, 1])
    p.div(q).display()

    '''
    for x in range(0, 10):
      for y in range(0, 10):
         for z in range(0, 10):
            Polynomial([x,y,z]).display()
    '''        

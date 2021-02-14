import math,operator

class Vector:
    def __init__(self,content):
        self.content = content

    def get_content(self):
        return self.content
    
    def get_len(self):
        return len(self.content)
    
    def add(self,vec):
        if self.get_len() == vec.get_len():
            return Vector(list(map(operator.add, self.content,vec.get_content())))
        else:
            return False 
        
    def subtract(self,vec):
        if self.get_len() == vec.get_len():
            return Vector(list(map(operator.sub,self.content,vec.get_content())))
        else:
            return False
        
    def dot(self,vec):
        if self.get_len() == vec.get_len():
            acc = 0
            for i,j in zip(self.content,vec.get_content()):
                acc += i * j
            return acc
        else:
            return False
    
    def norm(self):
        acc = 0
        for i in self.content:
            acc += math.pow(i,2)
        return math.sqrt(acc)
    
    def equals(self,vec):
        return self.content == vec.get_content()
    
    def __str__(self):
        res = '('
        for i in self.content:
            res += '{},'.format(i)
        return ')'.join(res.rsplit(',',1))


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

assert a.add(b).equals(Vector([4, 6, 8])) , "Should be Vector([4, 6, 8]"
assert a.subtract(b).equals(Vector([-2, -2, -2])) , "Should be Vector([-2, -2, -2])"
assert a.dot(b) == 26 , "Should be 26"
assert a.norm() == 14 ** 0.5 , "Should be {}".format(14 ** 0.5)
assert a.add(c) == False , "Should be False"
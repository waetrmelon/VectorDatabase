import matplotlib.pyplot as plt

class Node():
     def __init__(self,vec) -> None:
          self.vec = vec
          self.value = sum(vec)/len(vec)
          self.representation = [self.value, self.vec]

def GenerateVector(data):
    vec = []
    if type(data) != str:
        data = str(data)
    for item in data: vec.append(ord(item))
    return vec

def CalculateNodePosition(vec):
     return Node(vec)

def displayGraph(vectors):
    x_coords = [i+1 for i in range(len(vectors))]
    plt.scatter(x_coords, vectors)
    plt.show()

def GenerateGraphValue(value):
    return CalculateNodePosition(GenerateVector(value)).value

def findNearestNode(vec,item,range=0):
     if len(vec) <= 1: return None     
     
     vec = sorted(vec)

     indexPos = vec.index(item)
     
     left = 0
     right = 0
     
     if indexPos + 1 > len(vec): right = vec[indexPos + 1]
     if indexPos - 1 < len(vec): left = vec[indexPos - 1]

     if item-left > item-right: 
        if abs(item-right) <= range: return right
     else: 
         if abs(item-left) <= range: return left

def findNodeRange(vec,item,amount=2,range=0):
     if len(vec) <= 1: return None     
     if amount == 1: return item

     vec = sorted(vec)

     indexPos = vec.index(item)
     
     left = vec[:indexPos]
     print(left)
     right = vec[indexPos:]
     print(right)
     inRange = []

     for val in left:
         print(item, left)
         if abs(item-val) <= range:
             inRange.append(val)

     for val in right:
         if abs(item-val) <= range:
             inRange.append(val)

     return inRange[:amount]

def SimilarityProbability(NodeValue1,NodeValue2):
    return (1/(abs(NodeValue1-NodeValue2))) * 100
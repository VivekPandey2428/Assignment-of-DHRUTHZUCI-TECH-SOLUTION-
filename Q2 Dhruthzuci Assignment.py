def Intersection(lst1, lst2): 
    return set(lst1).intersection(lst2)

lst1 = []   
lst2 = []   
  
lst1 = [int(item) for item in input().split()] 
  
lst2 = [int(item) for item in input().split()] 
print(Intersection(lst1,lst2))
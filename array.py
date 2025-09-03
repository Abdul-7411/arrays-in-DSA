# Creating a python list
import ctypes # ctypes allows us to use c dtypes in python

class List:
    
    def __init__(self):
        self.size = 1 # size means size of list
        self.no = 0# no means the total numbers stored in list
        #Create a ctype array of size = self.size
        self.A = self.__make_array(self.size)
        

    def __len__(self):
        return self.no
    
    def __str__(self):
        result = ''
        for i in range(self.no):
            result = result + str(self.A[i]) + ', '

        return '['+result[:-2]+']'
    
    def __getitem__(self,index):# for adding indexong feature in our list we use this magic method
        if isinstance(index , int):
            if index < 0:
                index = self.no + index
                
            if index < self.no and index >= 0:
                return self.A[index]
            
            else:
                return "IndexError - Index Out Of Range"
            
        elif isinstance(index,slice):
            start,stop,step = index.indices(self.no)
            sliced = []
            for i in range(start , stop , step):
                sliced.append(self.A[i])
            
            return sliced    
            
    def __delitem__(self,pos):
        #deletion
        if pos < self.no and pos >=0:
            for i in range(pos,self.no-1):
                self.A[i] = self.A[i+1]
                
            self.no-=1
        else:
            print("Index out of range")
    
    def append(self,item):
        if self.no == self.size:
            # we will resize it
            self.__resize(self.size*2)
        
        # append item
        self.A[self.no] = item
        self.no +=1
    
    def pop(self):
        if self.no == 0:
            print("List is Empty")
        print(self.A[self.no-1])
        self.no = self.no - 1
    
    def clear(self):
        self.no = 0
        self.size = 1
    
    def find(self,item):
        for i in range(self.no):
            if self.A[i] == item:
                return i
            
        return "Item not in list"
    
    def insert(self,pos,item):
        if self.no == self.size:
            self.__resize(self.size*2)

        for i in range(self.no,pos,-1):
            self.A[i] = self.A[i-1]
            
        self.A[pos] = item
        self.no+=1
    
    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
    
    def sort(self):
        for i in range(self.no -1):
            for j in range(self.no -1 -i):
                if self.A[j] > self.A[j+1]:
                    #Swapping
                    self.A[j],self.A[j+1] = self.A[j+1],self.A[j]
        return self.A
    
    def minimum(self):
        self.A = self.sort()
        return self.A[0]
    
    def maximum(self):
        self.A = self.sort()
        ind = self.no -1
        return self.A[ind]
    
    def extend(self,new_lst):
        for i in range(len(new_lst)):
            self.append(new_lst[i])
        return self.A
    
    def merge(self,new_lst):
        for i in range(len(new_lst)):
            self.append(new_lst[i])
        self.A = self.sort()
        return self.A
    
    def summ(self):
        num = 0
        for i in range(self.no):
            num+=self.A[i]
        return num
            
    def __resize(self,new_capacity):
        # Creating a new array of new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # Copying the old array elements to new array
        for i in range(self.no):
            B[i] = self.A[i]
        # reassign
        self.A = B
    
    def __make_array(self,capacity):
        #Creates a ctype array(static, refrential)
        return (capacity*ctypes.py_object)()


lst = List()

lst.append(250)
lst.append(2)
lst.append(10)
lst.append(3)
lst.append(25)
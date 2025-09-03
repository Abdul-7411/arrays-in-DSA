# Arrays-in-DSA
# 🚀 DSA Journey in Python  

This repository contains my implementation of a **custom Python List** from scratch using `ctypes`.  
The goal is to deeply understand **Data Structures & Algorithms (DSA)** by re-creating the core functionality of Python’s built-in list.  

---

## 📌 Features Implemented  

- `__len__` → Get length of list  
- `__str__` → String representation  
- `__getitem__` → Indexing & slicing support  
- `__delitem__` → Delete item at a position  
- `append` → Add new element  
- `pop` → Remove last element  
- `clear` → Clear the list  
- `find` → Search an item  
- `insert` → Insert at position  
- `remove` → Remove by value  
- `sort` → Sort elements (Bubble Sort)  
- `minimum` → Get min element  
- `maximum` → Get max element  
- `extend` → Extend list with another list  
- `merge` → Merge & sort lists  
- `summ` → Sum of all elements  
- `__resize` → Resize array dynamically  
- `__make_array` → Create raw memory array  

---

## 📂 Example Usage  

```python
from custom_list import List

lst = List()
lst.append(250)
lst.append(2)
lst.append(10)
lst.append(3)
lst.append(25)

print(lst)         # [250, 2, 10, 3, 25]
print(lst.maximum()) # 250
print(lst.minimum()) # 2
print(lst.summ())    # 290

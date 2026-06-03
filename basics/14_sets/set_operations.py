"""
14. DATA STRUCTURE - SET
Learning: How to use Set, add, delete, search in Set
Note: Sets are unordered and contain unique elements
"""

# 14.1 Declare Set
print("=== 14.1 Declare Set ===")
s = set(['A', 'B', 'E', 'F', 'E', 'F'])
print("Original set           --> ", s)
print("Num of elements in set --> ", len(s))

# 14.2 Operations on Sets
print("\n=== 14.2 Set Operations ===")
a = set(['A', 'B', 'E', 'F'])
b = set(["A", "C", "D", "E"])
print("Original set a      --> ", a)
print("Original set b      --> ", b)
print("Union of a and b    --> ", a.union(b))
print("Intersection of a,b --> ", a.intersection(b))
print("Difference a - b    --> ", a - b)
print("Difference a - b    --> ", a.difference(b))
print("Difference b - a    --> ", b - a)
print("Difference b - a    --> ", b.difference(a))
print("Symmetric Diff a - b --> ", a.symmetric_difference(b))
print("Symmetric Diff b - a --> ", b.symmetric_difference(a))

# 14.3 Add, delete, pop element from set
print("\n=== 14.3 Add, Delete, Pop from Set ===")
a = set(['A', 'B', 'E', 'F'])
print("Original set a       --> ", a)
a.add("D")
print("Set After Adding (D) --> ", a)
a.add("D")
print("Set After Adding (D) --> ", a)
a.remove("D")
print("Set After Deleting(D)--> ", a)
a.pop()
print("Set After pop        --> ", a)
a.pop()
print("Set After pop        --> ", a)

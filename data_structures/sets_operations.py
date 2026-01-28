set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
print("Union using method:", set1.union(set2))
print("Intersection using method:", set1.intersection(set2))
print("Difference using method:", set1.difference(set2))
print("Symmetric Difference using method:", set1.symmetric_difference(set2))
print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set1 a superset of set2?", set1.issuperset(set2))
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))
print("Set1 elements:")
for elem in set1:
    print(elem)
print("Set2 elements:")
for elem in set2:
    print(elem)
set1.add(7)
print("Set1 after adding 7:", set1)
set2.remove(3)
print("Set2 after removing 3:", set2)
set1.update({8, 9})
print("Set1 after updating with {8, 9}:", set1)
set2.discard(10)  # No error if 10 is not present
print("Set2 after discarding 10 (no error if not present):", set2)
set1.clear()
print("Set1 after clearing:", set1)
set2.pop()
print("Set2 after popping an element:", set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1 |= set2
print("Set1 after union update with Set2:", set1)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1 &= set2
print("Set1 after intersection update with Set2:", set1)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1 -= set2
print("Set1 after difference update with Set2:", set1)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1 ^= set2
print("Set1 after symmetric difference update with Set2:", set1)
print("Length of Set2:", len(set2))
print("Is 5 in Set2?", 5 in set2)
print("Is 10 in Set2?", 10 in set2)
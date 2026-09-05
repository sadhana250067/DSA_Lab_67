import array

arr = array.array('i', [1, 2, 3])
print(arr)

arr.append(4)
print(arr)

arr.insert(2, 5)
print(arr)

arr.pop()
print(arr)

arr.remove(2)
print(arr)

print(arr.index(3))
print(arr.index(5))

arr.reverse()
print(arr)

alphabet = ["a","b","c","d"]

for char in alphabet:
    print(char)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
odd.append(9)
even.extend(odd)
print(even)
even.sort()
print(even)
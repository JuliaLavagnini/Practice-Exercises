# ex1
movies = ["film1", "film2", "film3", "film4", "film5"]
print(movies[0])
print(movies[-1])

# ex2
movies.append("film6")
movies.append("film7")
movies.pop(1)
movies.insert(1, "film8")

#ex3
print(movies[::2]) # every second item
print(movies[-3:])

#ex4
for i in movies:
    print(i.upper())

#ex5
movies.reverse()
print(movies)
i = movies.index("film8")
print(i)

#ex6
students = [["student1", 10, 'B' ], ["student2", 9, 'A' ], ["student3", 11, 'C' ], ["student4", 10, 'A' ]]
i = students[1][2]
print(i)
students.append(["student5", 12, 'C'])
print(students)

#ex7
numbers = list(range(1,11))
squares = [n**2 for n in numbers if n % 2 == 0]
print(squares)

#ex8
names = ["Caio", "Pedro", "Thais", "Julia", "Bruno", "Alice", "Amanda"]
new_list = [name for name in names if name.lower().startswith('a')]    
print(new_list)

#ex9
nested = [[1, 2], [3, 4], [5, 6]]
singleList = [a for i in nested for a in i]
print(singleList)

# Looping Through an Entire List

programming_languages = ["Python", "Java", "C++", "JavaScript"]
print(programming_languages[0])
print(programming_languages[1])
print(programming_languages[2])
print(programming_languages[3])

# With a list
for language in programming_languages:
    print(language)


# Not indenting additional lines
for language in programming_languages:
    print("I want to learn", language)
print(language, " seems like it will be useful.")


for value in range(1, 5):
    print(value)

# Storing as a list, step param

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

numbers = list(range(1,11))
print()

people = ['charles', 'martina', 'michael', 'florence', 'eli']
print

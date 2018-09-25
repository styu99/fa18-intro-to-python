programming_languages = ["Python", "Java", "C++", "JavaScript"]
print(programming_languages)

print(programming_languages[0])
print("Python")


print(programming_languages[3])
print(programming_languages[-1])

print(programming_languages[-2])

print("My favorite programming language is " + programming_languages[0])

programming_languages[2] = "Matlab"
print(programming_languages)

programming_languages.append("FORTRAN")
print(programming_languages)

programming_languages.insert(0, "Perl")
print(programming_languages)

del programming_languages[0]
print(programming_languages)

popped_lang = programming_languages.pop()
print(programming_languages)
print(popped_lang)
programming_languages.pop(2)
print(programming_languages)


programming_languages.remove('Java')
print(programming_languages)

programming_languages = ['Perl', 'Python', 'Java', 'Matlab', 'JavaScript', 'FORTRAN']
programming_languages.sort(reverse=True)
print("List sorted in reverse order:" + str(programming_languages))


programming_languages.reverse()
print(programming_languages)
programming_languages.reverse()
print(programming_languages)



print(len(programming_languages))
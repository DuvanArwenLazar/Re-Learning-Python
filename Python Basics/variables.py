variable = "Python"
print(variable)

# -- Sum.
a, b = 2, 3
c = a + b
print(c)

# -- Sum "+="
num = 5
num += 1
print(num)

# -- Concat & f-strings.
name = "Duvan"
lastname = "Arwen Lazar"
print(f"{name} {lastname}")
print("Hi, " + name + " " + lastname)

# -- Delete a variable.
# del name
# print(name) # Error (doesn't exist).

# -- in & not in.
string = f"{name} {lastname}"
print("Jose" in string) # Bool value.
print("Jose" not in string) # Bool value.

# Tip: for Python, use snake_case to name variables.

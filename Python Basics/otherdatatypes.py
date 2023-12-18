# -- Lists. List is mutable.
list_sample = [1, 2, 3, 4, 5]
print(list_sample[0]) # get by index.
list_sample[1] = "Hello World." # Edit a value.
print(list_sample)

# -- tuples. Tuple is immutable.
tuple_sample = (1, 2, 3, 4, 5)
# tuple_sample[3] = "No idea." # Error.

# -- Set. Works like a math set.
this_is_a_set = {"Yes", "No", True, True, False}
print(this_is_a_set)
# print(this_is_a_set[0]) # Error.

# -- dictionary (key:value)
this_is_a_dict = {
    'name': "Duvan",
    'lastname': "Arwen Lazar",
    'height': 1.70
}

print(this_is_a_dict['name']) # get by 'key'.

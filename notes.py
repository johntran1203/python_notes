sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''
for sound in sounds:
    result += sound

# print(result.upper())

# .append
# .insert()
# .extends
# .pop
# .remove
# # returns the index of the specified item in the list
# .index 
# # return the number of times x apears in the list
# .count
# # reverse the elemnts of the list in place
# .reverse
# # sort the items of the list in place
# .sort
# # a string method  ''.join
# .join

instructors = ['Colt','Blue', 'Lisa']
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.remove("Colt")
# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')
# Run the tests to make sure you've done this correctly!
# print(instructors)

['start','end','step']

name = 'john'
print([char.upper() for char in name])
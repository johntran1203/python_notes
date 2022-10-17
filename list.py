# list comprehensions
# numbers  = [1,2,3,4,5,6]

# evens = [ num for num in numbers if num % 2 == 0]

# oddes = [ num for num in numbers if num % 2 != 0]

answer = [char[0] for char in ["Elie", "Tim", "Matt"]]

# print(answer)

answer2=  [ num for num in [1,2,3,4,5,6] if num % 2 == 0]

print(answer2)

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

answer = [val for val in range(1,101) if val % 12 == 0] 

answer = [char for char in "amazing" if char not in "aeiou"]
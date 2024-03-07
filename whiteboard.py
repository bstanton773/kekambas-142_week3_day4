# Write a function that accepts two numbers a and b and returns whether a is smaller than, bigger than, or equal to b, as a string.

# (5, 4)   ---> "5 is greater than 4"
# (-4, -7) ---> "-4 is greater than -7"
# (2, 2)   ---> "2 is equal to 2"
# There is only one problem...

# You cannot use if statements, and you cannot use the ternary operator ? :.

# In fact the word if and the character ? are not allowed in your code.

# (no_ifs_no_buts(45,51)) = "45 is smaller than 51"
# (no_ifs_no_buts(1,2)) = "1 is smaller than 2"
# (no_ifs_no_buts(-3,2)) = "-3 is smaller than 2"
# (no_ifs_no_buts(1,1)) = "1 is equal to 1"
# (no_ifs_no_buts(100,100)) = "100 is equal to 100"
# (no_ifs_no_buts(100,80)) = "100 is greater than 80"

# def solution(a, b):
#     while a > b:
#         return f"{a} is greater than {b}"
#     while a == b:
#         return f"{a} is equal to {b}"
#     return f"{a} is smaller than {b}"

def solution(a, b):
    answers = {
        a == b: f"{a} is equal to {b}",
        a < b: f"{a} is smaller than {b}",
        a > b: f"{a} is greater than {b}"
    }
    return answers[True]

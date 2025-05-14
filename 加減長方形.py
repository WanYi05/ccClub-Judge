# Practice_1
# a = int(input())
# b = int(input())

# for i in range(a):  # Iterate 'a' times for the rows
#     for j in range(b):  # Iterate 'b' times for the columns
#         print("+-", end="")
#     print("+")  # Add a '+' at the end of each row

#Answer
a = int(input())
b = int(input())

if a % 2 == 0:  # Check if 'a' is even
    for i in range(b):
        output_row = ""
        for j in range(a):
            if j % 2 == 0:
                output_row += "+"
            else:
                output_row += "-"
        print(output_row)
else:  # If 'a' is odd
    for i in range(b):
        output_row = ""
        for j in range(a):
            if i % 2 == 0:  # Even row (starting with +)
                if j % 2 == 0:
                    output_row += "+"
                else:
                    output_row += "-"
            else:  # Odd row (starting with -)
                if j % 2 == 0:
                    output_row += "-"
                else:
                    output_row += "+"
        print(output_row)
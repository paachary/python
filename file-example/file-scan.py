"""
    Author : Prashant Acharya
    Date   : 07/26/2018   
    Description :
 
   Module to read a file and search for a specific string within each line.
   Once line containing specific string is found, then print that line and 
   specified lines above and below the string
"""


# define the file name
filename = "catchme.log"

# define the no of lines to be printed above and below the specified string
limit = 2

# define the searchable string
str_search = "catchme"

with open(filename, "r") as file:
    lineno = 0

    # readlines function will cache the entire file contents. 
    # The output will be a list.
    lines = file.readlines()

    for line in lines:
        lineno += 1

        # search for the specified string in each line.
        if str_search in line:

            # decorate the output
            print("-----"*19)

            # print the lines above the searched string            
            for line_no in range(lineno-limit, lineno, 1):
                print(lines[:line_no][-1])

            # print the searched string itself
            print(line)

            # print the lines below the searched string
            for line_no in range(lineno+1, lineno+1+limit, 1):
                print(lines[:line_no][-1])

            input("Enter to continue")

    # decorate the output
    print("-----"*19)

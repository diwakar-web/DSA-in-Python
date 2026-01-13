# Print 1 TO 5 USING LOOP AND RECURSION


# WHILE LOOP------>

# n=5
# i=1
# while (i<n+1):
#     print(i)
#     i=i+1



# RECURSION----->

def printnum(i,n):
    # BASE CASE
    if i>n:
        return
    #RECURSIVE CASE
    print(i)
    printnum(i+1,n)


printnum(1,5)
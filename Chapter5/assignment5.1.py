'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an 
appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and 
Match the desired output as shown.
'''

count = 0
total = 0
while True:
    text = raw_input("Enter a number: ")
    if text == "done" : break
    if len(text) < 1 : break # check empty line
    try:
        num = float(text)
    except:
        print "Invalid input"
        continue
    
    count = count + 1
    total = total + num
    
print total, count, total/count

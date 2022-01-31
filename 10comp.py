#read integer from command line
number_to_assess=int(input("Enter a number to compare to 10"))

#check if number is less than 10
if (number_to_assess<10):
    print(number_to_assess,"<is less than 10")
elif(number_to_assess ==10):
    print(number_to_assess, "is equal to ten")
else:
    print(number_to_assess, "is greater than ten")
#if less than ten, tell user
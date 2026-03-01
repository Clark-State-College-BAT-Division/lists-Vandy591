#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class
# video url: https://youtu.be/VGrRdUunjXg

numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)
print("As entered: ")
print(numbers)
print("Small to large: ")
print(sorted(numbers))
print("Large to small: ")
print(sorted(numbers, reverse = True))
Mean = sum(numbers) / 5 
print("median:", Mean)
sorted_numbers = sorted(numbers) 
median = sorted_numbers[2]
print("median:", median)
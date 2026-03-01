#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken 
#You entered a total of 62 characters
foods = []
for i in range(5):
    food = input("Enter a food: ")
    foods.append(food)
print("Your enterned foods are here")
print(foods[0] + ", " + foods[1] + ", " + foods[2] + ", " + foods[3] + ", " + foods[4])
totalcharacters = 0 
for food in foods:
    totalcharacters += len(food)
print(f"You entered a total of {totalcharacters} characters")
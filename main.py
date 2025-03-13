# Name: Dia Yamamoto
# Purpose: This program will calculate the average of mulitple numbers

def calculate_average(numbers):
  total = 0
  count = 0

  for num in numbers: 
    total += num 
    # total = total + num  
    count += 1

  if count > 0: 
    average = total/count
    return average
  else: 
    return None

numList = []
count = int(input("How many numbers in your list? "))

for i in range(count):
  num = input("Enter the number: ")
  numList.append(int(num))

average = calculate_average(numList)

if average is not None: 
  print("The average of our numbers is: " + str(average))
else: 
  print("The list is empty, cannot calculate average.")
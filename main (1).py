
#1
def fullname(first_name, last_name):
    return f"{first_name} {last_name}"

def string_alternative(full_name):
    return full_name[::2]

def main():

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = fullname(first_name, last_name)
    print(f"Full Name: {full_name}")

    alternative_string = string_alternative(full_name)
    print(f"Every other character in the full name: {alternative_string}")

if __name__ == "__main__":
    main()



#2
input_file = open('input(1).txt', 'r')#reading the input file
count = dict()# to count 
source = input_file.read()# read data from the input file
words = source.split()# splitting the words
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
f = open('output.txt', 'w')#writing the output file
f.write(source)
f.write('\nword_count:\n')
for key, value in count.items():
    f.write(f"{key}: {value}\n")
f.close()









#3(a)
# Method 1: Using Nested Interactive Loop

heights_in_inches = []


num_customers = int(input("Enter the number of customers: "))


for i in range(num_customers):
    height = float(input(f"Enter height (in inches) of customer {i+1}: "))
    heights_in_inches.append(height)

heights_in_cm = []

for height in heights_in_inches:
    cm = height * 2.54  # Convert to cm
    heights_in_cm.append(round(cm, 2))  # Round to 2 decimal places


print("Heights in centimeters:", heights_in_cm)







#3(b)
# Method 2: Using List Comprehensions

heights_in_inches = []

num_customers = int(input("Enter the number of customers: "))

for i in range(num_customers):
    height = float(input(f"Enter height (in inches) of customer {i+1}: "))
    heights_in_inches.append(height)


heights_in_cm = [round(height * 2.54, 2) for height in heights_in_inches]


print("Heights in centimeters:", heights_in_cm)

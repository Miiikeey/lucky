
# count for letters and numbers
letter_count = 0
number_count = 0
# Open the ini file as read
with open("ini.txt") as ini_file:
    data = ini_file.read()

# split up the data to become line for line
lines = data.split("\n")

#count both numbers and letters by adding 1 to the counts
for line in lines:
    for i in line:
        if i.isalpha():
            letter_count += 1
        elif i.isdigit():
            number_count += 1
#close file to open a new one
ini_file.close()

#open/create a new file to print out the output
with open("outputs.txt", "w") as output_file:
    output_file.write(f"Total Letters: {letter_count} \n")
    output_file.write(f"Total numbers: {number_count}")

output_file.close()

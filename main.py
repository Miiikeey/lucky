
# read the txt file 
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

lines = data.split("\n")
key_value_ini = dict()

for line in lines:
    if "=" in line:
        fields = line.split("=")
        key_value_ini[fields[0]]= fields[1] 
print(key_value_ini)
test
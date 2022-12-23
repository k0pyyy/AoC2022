# first we have to read the input
with open("./input.txt", 'r') as file:
    lines = file.readlines()

# first thing we should do is break everything up
# split the list up into chunks with a new line
calsPerElf = []
temp = []
for line in lines:
    # if the line isn't a new line, then we want to add it
    # to the current running chunk
    if line.strip() != "":
        temp.append(int(line.strip()))
    else: 
        calsPerElf.append(sum(temp))
        temp = []

# we have to add the remaining list to the elves list
calsPerElf.append(sum(temp))

# now print out the maximum amount of calories
print(max(calsPerElf))

# part 2 asks to find the sum of the calories from the top 3
# elves
calsPerElf = sorted(calsPerElf)

print(sum(calsPerElf[:len(calsPerElf) - 4:-1]))
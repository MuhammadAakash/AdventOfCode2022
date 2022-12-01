with open('day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]

max = 0
max2 = 0    # Elf with second greatest calories
max3 = 0    # Elf with third greatest cals
count = 0
for item in data:
    if item == '':
        count = 0       # Resetting the count | skipping to next Elf
    else:
        num = int(item) # Turning string to integer (so we can add)
        count += num    # Adding to the count if its a number

    # Finding max values
    if count > max: 
        max = count     # Elf with most calories
    elif count > max2:
        max2 = count    # Elf with second to most 
    elif count > max3:
        max3 = count
print("count :", count + count + count)
print("Answer to part 1:", max)
print("Answer to part 2:", max+max2+max3)
tree = int(input("enter the number of rows: "))

for i in range(1,tree+1):
    print(" "*(tree-i)+"* "*i)

for j in range(tree- (tree//2)):
    print(" "*(tree-1)+"*")


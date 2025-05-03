def main():
    size = int(input("Enter size of array: "))
    arr = [i + 1 for i in range(size)]  
    for i in arr:
        print(i, end=" ")

main()

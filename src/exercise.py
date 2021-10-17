def main():
    #write your code below this line
    file_name = input("Name of the file:")
    names = []
    while True:
        name = input("Enter names, an empty line quits.")
        if (name == ""):
            break
        else:
            f = open(file_name, "r")
            data = f.read().splitlines()
            if name in data:
                print("The name is on the list.")
            else:
                print("The name is not on the list.")
    print("Thank you!")

if __name__ == '__main__':
    main()

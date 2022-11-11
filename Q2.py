if __name__ == "__main__":
    n = int(input("The total number of records: "))
    allValid = True
    errorCodes = []
    for i in range(n):
        record = input()
        record_list = record.split(" ")
        valid = record_list[1]
        if valid == "false":
            allValid = False
            errorCodes.append(record_list[2])
    
    if allValid == True:
        print("Yes")
    else:
        print("No")
        print(*errorCodes, sep = " ")

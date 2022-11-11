if __name__ == "__main__":
    n = input("The total number of T-Shirts in the shop: ")
    tshirt_store = input("Input the t_shirt list: ")
    m = input("The total number of requests: ")
    tshirt_request = input("Input the t_shirt request: ")
    tshirt_list = tshirt_store.split(" ")
    request_list = tshirt_request.split(" ")
    result = True
    for i in request_list:
        for j in tshirt_list:
            if ("S" in i and "S" in j) and i.count("X") >= j.count("X"):
                    break
            if ("S" in i and "M" in j):
                break
            elif ("S" in i and "L" in j):
                break
            elif ("M" in i and "M" in j):
                break
            elif ("M" in i and "L" in j):
                break
            elif ("L" in i and "L" in j) and i.count("X") <= j.count("X"):
                break
            else:
                result = False
                
    if result == True:
        print("Yes")
    else:
        print("No")

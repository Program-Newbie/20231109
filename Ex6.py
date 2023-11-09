def addition(num) :
    if num :
        return num + addition(num-1)
    else :
        return 0

if __name__ == "__main__" :
    print(addition(10))
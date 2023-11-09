def outer_fun(a, b):
    square = a ** 2
    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5
if __name__ == "__main__" :
    result = outer_fun(5, 10)
    print(result)

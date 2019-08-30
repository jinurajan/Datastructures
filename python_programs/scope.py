def outer():
    state = 10

    def inner():
        return state
    return inner


inn = outer()
s = inn()
print s

def subtractor(a,b):
    """I subtract a from b and return the result"""
    print("I'm a function. My name is {}.".format(subtractor.__name__))
    print("I'm about to subtract {} and {}\n\n".format(a,b))
    return a - b

if __name__=='__main__':
    value=subtractor(3,2)
    print(value)

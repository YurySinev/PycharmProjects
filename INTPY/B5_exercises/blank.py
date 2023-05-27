def twice_func(inside_func):
    inside_func()
    inside_func()

def hello():
    print("Hello!")

test = twice_func(hello)

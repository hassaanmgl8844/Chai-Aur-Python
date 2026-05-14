# Debugging Function Call - Create a Decorator to print the function name and the value it's arg every time the func is called.

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper

@debug
def greet(name,greeting="Hello There!"):
    print(f"{greeting},{name}")
greet("chai",greeting="Hi")
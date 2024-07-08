
# Solution 1
# import time

# def timer(func):
#     def wrapper(*args):
#         a = time.time()
#         result = func(*args)
#         b = time.time()
#         print(f'{func.__name__} is {-a+b}')
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(5)


# ****************Solution 2****************************************************

# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k} = {v}" for k,v in kwargs.items())
        
#         print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
#         return func(*args,**kwargs)
    
#     return wrapper

# @debug
# def greet(name,greeting="hello"):
#     print(f'{greeting},{name}')

# greet('ROHIT',greeting='Hann ji')


# **********************Solution 3 *************************
# def cache(func):
#     cache_value = {}
#     print(cache_value)
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result
#         return result
#     return wrapper

# import time

# @cache
# def long_func(a,b):
#     time.sleep(4)
#     return a+b

# print(long_func(2,3))
# print(long_func(2,3))
# print(long_func(2,3))
# print(long_func(2,3))

# print(long_func(2,4))
# print(long_func(2,3))
# print(long_func(2,3))
# print(long_func(2,1))
# print(long_func(2,4))



from webbrowser import get


def hello_world():
    print("Hello World")

#hello_world()

def todays_mood():
    mood = "happy"
    print("Today's mood: " + mood)

#todays_mood()

def sum_int(a, b):
    ans1 =  (a + b)*2
    print(ans1)
#sum_int(20,8)

def product(a,b): 
    product = a * b
    print(f"product is {product}")
#product(22,7)

def what_time_is_it(hour):
    if hour == 12:
        print ("peanut butter jelly time")
    elif hour == 2:
        print ("time for a nap")
    else:
        print("nap time")
#what_time_is_it(2)

def get_first(lst):
    if lst:
        return lst[0]
    else:
        return None

def get_last(lst):
    if lst:
        return lst[-1]
    else:
        return None
    
#x = get_first([1, 2, 3])

#y= get_last([1, 2, 3])

def counter(stop):
    for i in range( 1, stop +1):
        print(i)
#counter(10)

def sum_ten():
    return sum(range(1, 11))

print(sum_ten())

#fizzbuzz game

for i in range(100):

    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)    
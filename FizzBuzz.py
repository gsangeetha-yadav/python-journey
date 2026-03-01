# FizzBuzz program : prints number from 1 to 20 replaces multiples of 3,5, and both
for i in range(1,21):
    if i%3==0 and i%5==0:
        print("ThreeFive")
    elif i%3==0:
        print("Three")
    elif i%5==0:
        print("Five")
    else:
        print(i)

# ? 1 .Basic

for i in range(150):
    print(i)


# ? 2 Multiples of Five

for i in range(5,1001,5):
    print(i)


# ? 3 Counting, the Dojo Way


for i in range (1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0 :
        print("Coding")
    else:
        print (i)

# ? 4 Whoa. That Sucker's Huge 

sum = 0
for i in range (0, 500001):
    if i % 2 !=0:
        sum += i
print(sum)

# ? 5 Countdown by Fours 

for i in range (2018, 0, -4):
    print(i)


# ? 6 Flexible Counter

def flexible_counter(lowNum,highNum,mult):
    for i in range (lowNum, highNum+1):
        if i % mult ==0 :
            print(i)


flexible_counter(2, 9, 3)
flexible_counter(2,34,5)











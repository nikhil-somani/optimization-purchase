# you can fetch the values from file and read it 
# split it as required and can save in variables given here

#quantity to be purchased
n = 19

#lot size and lot price
m1 = 3
p1 = 10

#lot size and lot price
m2 = 4
p2 = 15

#taken a bigger number for safe
cost = 10000000000

#logic first using range 
# simply  cost = ax + by where a and b are lot size, x and y are lot count, n is required quantity
# and total cost is minimised 
for x in range(n+1):
    for y in range(n+1):
       if((m1 * x + m2 * y) == n):
           if((x * p1 + y * p2) < cost):
               cost = (x * p1 + y * p2)
               c = x
               d = y

#you can implement else case for invalid lot sizes if sometimes you may not be able to
#make exact purchase of n quantity.

#print for minimal cost, lot counts taken.
print("Minimal Cost: ", cost,  "\nlot 1: ",  c, "\nlot 2: ",  d)



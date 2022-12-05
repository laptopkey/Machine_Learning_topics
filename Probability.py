def probability_of_even(a):
 c=0
 # here the set of numbers is the list a
 total=len(a)
 for i in a:
   #checks whether the number is even or not
   if(i%2==0):
     c+=1;
     #returns the probability of total even numbers/total outcomes
 return(c/total)

def probability_of_prime(a):
 c=0
 # here the set of numbers is the list a
 total=len(a)
 for i in a:
   #function to see if its a prime or not
   if(i>1):
     c2=0
     for j in range(2,i):
       if(i%j==0):
         c2+=1
     if(c2==0):
       c+=1
       #probability value:
 return(c/total)

def probability_divisible(a):
 c=0
 #here the set of numbers is list a
 total=len(a)
 for i in a:
   #check divisibility
   if(i %3==0 and i%5==0):
     c+=1
 # probability value:
 return(c/total)

# let's say we have the following
set_of_numbers=[1,2,3,4,5,6,7,8,9,10,11,23]
n=12
#calling the functions:
print(" the probability of choosing an even number would be: ",probability_of_even(set_of_numbers))
print(" the probability of choosing a prime number would be: ",probability_of_prime(set_of_numbers))
print(" the probability of choosing a number divisible by 3 and five is: ",probability_divisible(set_of_numbers))




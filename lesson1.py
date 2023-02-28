
###Variables
x=78;   ##int
print(x);

b="hello";  ##string
print(b);

c =1.9     ###float

print(c);


##printing my name using concatination

    #name=input("name:");
   ##print("hello"+ " "+name);

#Another way to print using Formatted string

   #print(f"hello{ name}");


##CONDITIONS

   #n=int (input("Number:"))

 #if n>0 :
 #   print("n is positive")
#    elif n<0:
#      print("n is negative")

#else:
    #print("n is zero")

    
## Sequences allows to access individual element in the sequence or index
   #names="zeynab"
  #print(names[0])
    
#sequences using array
names=["zeynab","aisha","sha"]
print(names[0])


#Data Structure

#list = sequence of mutable value
#tuple = sequence of immutable value(those value can't change)
#set = collection of unique value(doesn't keep particular order)
#dictionary =collection of key-value pairs
 
# key = we cal the things that i'm looking uo
# value  = we call what i get when i do the looking up the value    


#  LISTS

   #define the list of names
v=["dagan","ron","ginny"]


#Append mthod  = Adds value to the end of existing lis
  #v.append("drc")

#sorting
   #v.sort()
  #print(v)
  
#CREATE AN EMPTY SET
   #s=set()

#ADD ELEMENTS TO THE SET
 #s.add(1)
 #s.add(2)
 #s.add(3)
 #s.add(1)

#Removing item
  #s.remove(2)

#length of the elements
  #print(f"the set has{len(s)}elements")


#LOOPS :making something multiple times

   #for i in range (7):
    #print(i)


#loops for sequences
  #q = ["dagan","ron","ginny"]
  #for name in q:
    #print(name)


#markaan rabno inan magac uso print garayno hal hal xabo

  #c="casha"
    #for character in c:
    #print(character)

# PYTHON DISCTIONARY
houses={"casha": "zakarie","faiza":"salma"}
print(houses["casha"])

#FUNCTIONS  = TO DEFINE FUNCTION WE USE DEF KEYWOrD

# how to run loop ten times and printing out this line 10 different times

#10 ka number ee ukoreeya square kooda soo saar
 #def square(x):
    #return x*x
      #for i in range(10):
        # print(f"the square of{i} is {square(i)}")
#IMPORTING FUNCTION FROM ANOTHER PAGE
    #intan page gaar ah
       #def square(x):
         #return x*x

# intana page gaar ah
   #from functions import square
     #for i in range(10):
        #print(f"the square of{i} is {square(i)}")


#how to create CLASS in python
    ##  EXAMPLE 1
#define class
  #class Point():
    #magic method
      # def __init__(self,input1,input2):
      # self.x=input1
      # self.y=input2
#p=Point(2,8)
#print(p.x)
#print(p.y)
        ##  EXAMPLE 2
#lets imagine that we are trying to write program for an AIRLINE where
# where the airline needs to be track of booking passengers on flight
# and making sure that no flight gets overbooked, we don't want more
#passengers on the flight that there is capcity on that flight


class Flight():
   def __init__(self,capacity):
      self.capacity=capacity
      self.passengers=[]


      def add__passenger(self,name):
         if not self.open_seat():
            return false
         self.passengers.append(name)
         return true
      def open_seat(self):
         return self.capacity-len(self.passengers)
      flight=Flight(3)

      people=["harry","Ron","hermon","giny"]
      for person in people:
         if flight.add_passenger(person):
            print(f"Added{person}to flight succesfully.")
         else:
            print(f"no available seat for{person}")
            

#Decorators  = is function that takes a function of input and returns
            #modified version of that function as output

def announce(f):
   def wrapper():
      print("about to run the function...")
      f()
      print("done with the function")
   return wrapper

@announce
def hello():
   print("hello world")

hello()
   









    


    

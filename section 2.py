import os 
os.system ("cls")

## list
a = [ 1 ,3  , 6 ,8 ,9 ,1 ,5]
list2 = [5,15,20]
list3 = a + list2 # but a+list2 in list3 ==> [1 ,3  , 6 ,8 ,9 ,1 ,5,15,20 ]

B = a # This is shallow copy 
# C = list (a) # This is deep copy
C = a [:] # This is deep copy 

C[1] = 5
print (C)
print (a)

# # tuple not changable 
z = ([1,3],[2,6])
z [0][1] = 5 # here we change the list in tuple not the tuple
print (z)

t =  1 , 2 , 3 # packging 
x , y , z = t # unpackging

## dictiony ( have all porpotise that in list but have advantage (key,value))

print (5 in a ) # this search key in dictionry

for key , value in a.items() :
    print (key , value )

## sets 
a = "afewfredfvbaadfv"
z = {x for x in a if x not in "abc"} # give all elemnts that not in a 
print (z)

# sets is not support repet 
# split is oppiste to join  ==> .split()
# join() ==> put all words in the same word 

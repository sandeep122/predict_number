import random 

name=input("enter your name:")
print("welcom",name)
print("so let's start game",name)
print("my name is siri")
print("we have enter number between 1 to 4")

num=0
while True:
    user=int(input("enter number %s:"%(name)))
    
    b=random.choice(range(1,5))
    print("my number is ",b)
    if user!=b:
        print("%s you are not out"%(name))
        num=user+num
        print('your score is:',num)
    if user==b:
        print("you are out",name)
        break
        
    

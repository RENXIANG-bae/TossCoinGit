import random

count1=0
count2=0
A=["Heads","Tails"]

print("Tossing a coin...")

for i in range(1,4):
 wasi=random.choice(A)
 print("Round %d: %s" %(i,wasi))
 if wasi=="Heads":
     count1+=1
 else:
     count2+=1

print("Heads:%d Tails:%d" %(count1,count2))

if count1>count2:
 print("You win!")
else:
 print("You lost!")

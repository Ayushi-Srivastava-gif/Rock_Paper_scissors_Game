# rock, paper, scissors
import random
User=int(input("what do you choose? 0,1,2.\n"))
rock='''
    ___
---'   ___)
      (____)
      (____)
      (___)
---._(___)
'''

paper='''
    ___
---'   _)_____
          ______)
          _______)
         ______)
---.______)
'''
scissors='''
    ___
---'   _)____
        _______)
       ________)
      (___)
---._(___)
'''



if User==0:
    print(f"You choose rock{rock}")
elif User==1:
    print(f"You choose paper{paper}")
else:
    print(f"You choose scissors{scissors}")



Computer_choice=random.randint(0,2)
if Computer_choice==0:
    print(f"computer choose rock{rock}")
elif Computer_choice==1:
    print(f"computer choose paper{paper}")
else:
    print(f"computer choose scissors{scissors}")

if User==0 and Computer_choice==2:
    print("You win")
elif User==2 and Computer_choice==0:
    print("You lose")
elif User>=3 or User<0:
    print("number is invalid. you lose")
elif User> Computer_choice:
    print("You win")
elif Computer_choice> User:
    print("You lose")
elif User==Computer_choice:
    print("Draw")


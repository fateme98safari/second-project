import random

for i in range(5):
    comp_choice=random.randint(1,3)
    print(comp_choice)
    print("1:rock,2:paper,3:scissors")

    user_choice=int(input())

    if comp_choice=="1" and user_choice=="2":
        user_choice=user_choice+1

    elif comp_choice=="1" and user_choice=="3":
        comp_choice=comp_choice+1

    elif comp_choice=="2" and user_choice=="1":
        comp_choice=comp_choice+1

    elif comp_choice=="2" and user_choice=="3":
        user_choice=user_choice+1

    elif comp_choice=="3" and user_choice=="1":
        user_choice=user_choice+1

    elif comp_choice=="3" and user_choice=="2":
        comp_choice=comp_choice+1

    elif comp_choice==user_choice:
        comp_choice=comp_choice
        user_choice=user_choice
        
print("comp_choice:" , comp_choice)
print("user_choice:" , user_choice)

if comp_choice > user_choice:
    print("🎉computer win🎉")

elif comp_choice < user_choice:
    print("🎉user win🎉")
else:
    print("🌹computer and user are epual🌹")
    
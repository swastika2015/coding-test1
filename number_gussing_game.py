number = int(input("Enter a number between 1 to 50:"))


secret = 34
if (number==secret):
    print("Wow!You are amazing~")
elif number>=30 and number<=32 or number>34 and number <=36:
        print("hint =hot,give it another try ")
elif number>=30 and number <32 or number>34 and number<39:
      print("hint = warm,give it another try")
elif  number <30 and number>=20 or number>40 and number<=45:
      print("hint =cold,give it another try ")
elif  number <20 and number>=1 or number>45 and number<=50:
      print("hint =very cold,give it another try ")



weight=float(input("Enter the weight of a person:"))
height=float(input("Enter the height of a person:"))

bmi=(weight/(height*height))

if(bmi<18.5):
    print("UnderWeight")
elif(bmi>18.5 and bmi<25):
    print("Normal weight")
elif(bmi>25 and bmi<30):
    print("Over weight")
else:
    print("Obese")

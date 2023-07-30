uc=int(input("enter the unit consumed:"))
if(uc>0 and uc<=100):
    bill=(uc*5)+150 #150 unitcharge
elif(uc>100 and uc<=500):
    cal1=5*100
    cal2=((uc-100)*10)+150
    bill=cal1+cal2
else:
    cal1=5*100
    cal2=10*400
    cal3=((uc-500)*15)
    bill=cal1+cal2+cal3+150
print("Generated bill:",bill)

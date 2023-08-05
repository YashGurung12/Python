temp=input("Enter a temperature:")
temp=float(temp) #String to Float

choice=input("Convert to Farenheit or Celcius? \n")
while (True): 
    if(choice=="Farenheit"):
       f=(temp*(9/5) + 32)
       print ("Coverting {} to Farenheit is:{}".format(temp,f))
       break
    elif(choice=="Celcius" or "celcius"):
       c=((temp-32)*(5/9))
       print("Coverting {} to Celcius is:{}".format(temp,c))
       break
    else:
       print("Enter the correct option.")
       break






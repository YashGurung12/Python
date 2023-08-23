dict={}

key=input("Enter a key:")
value=input("Enter a value:")

dict[key]=value

print(dict)

key=input("Enter a key:")
if(key in dict):
    ch= input ("Do you want to replace?")
    if(ch=="yes"):
        value=input("Enter a value:")
        dict[key]=value
else:
    value=input("Enter a value:")
    dict[key]=value

print (dict)
print (dict.keys())
print(dict.values())
print (dict.items())
dict2=dict.copy()
del dict
print (dict2)

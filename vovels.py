a=input("Enter the string")
b=['a','e','i','o','u']
count=0
for letter in a:
    if( letter in  b ):
        count+=1
print(count)

#Count Sort
string = str(input())
count=[0,0,0,0]
for char in string:
    if char!="+":
        count[int(char)]+=1
newString =""
for number,amount in enumerate(count):
    newString+=(str(number)+"+")*amount if number !='0' else ''
newString=newString[0:-1]
print(newString)

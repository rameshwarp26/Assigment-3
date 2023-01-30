def reverse(string):
    string = string[::-1]
    return string 

string = input("Enter the strings to be reversed : ")
print ("The origional string is : ",string)
print ("The reversed string using extended slice operator is : ",reverse(string))

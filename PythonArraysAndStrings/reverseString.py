testString = "Hello, reverse me!"

def reverseString(string):
    newString = ""
    for i in range(len(string)-1, -1, -1):
        newString += string[i]
    print(newString)

reverseString(testString) # Time and Space O(n)

# Python comparison operators

### 1. Equal to **==**
-Checks if the value on the left is equal to value on the right.
**Example**
```py
print (11 ==11)
```
**Output:
#### Note! Comparison operators always result in a boolean value.
-For the code above since 11 is the same as 11 the output of the code will be `True`.

### 2. Not equal to **!=**
- Checks if the left side is **not equal to right side. 
```py
print(6 != '6') # Since texts can't be equal to numbers this line will print True
print(6 !=  6)  # Since the both side of equation is same, this will print False
```

### 3. Greater sign **>**
- Checks if the left side of equation is bigger than the right side.
```py
print(5.0 > 5) # False 
print(3 > 4)   # False
print(10 < 9)  # True 

### 4. Less than equal <= || Greater equal sign >=
-Checks if the left side is smaller OR equal **<=**,
-Checks if the left side is bigger OR equal **>**.
```
print(5.0 <= 5) # True because the values are equal.
print(5.0 >= 5) # True because the values are equal.
print(3 <= 4)   # True because 3 is smallet than 4.
print(10 >= 9)  # True because 10 is bigger than the 9.

##Note!
- ** Type Matters:**
-When comparing values type of the values also important:
For ex: `5 == '5'` `False` because one string (text) the other is not type.

- ** We can chain the comparison operators in python**
```py
print(1 < 2 < 3) #True 
```

##Note!
- `True` numerically equals to `1` and ` False` numerically equals to `0`
For example:
print(int(True))  #1
print(int(False)) #0
# When using comparison operators between bool and int type
# python auto-converts bool type to int.
print(True == 1)    #True
print(True > False) # True 
print(False < 3)    # True

## Converting Other types to Bool
- Which function do you think we're going to use to convert other types to boolean?
**bool()** function.
```py
b = bool(-2)











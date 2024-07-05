# COMPARISON OPERATION
# IF NAME IS LESS THAN 3 CHARACTERS LONG PRINT AS NAME MUST BE AT LEAST 3 CHARACTERS
# IF IT'S MORE THAN 50 CHARACTERS LONG PRINT AS NAME CAN BE A MAXIMUM OF 50 CHARACTERS
# IF NOT PRINT NAME LOOKS GOOD


name = "chandan k"
print(len(name))
if len(name) <3:
    print("name must be at least 3 characters")
elif len(name) >3:
    print("name can be maximum of  50 characters")
else:
    print("name looks good")

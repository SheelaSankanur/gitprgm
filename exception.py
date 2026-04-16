try:
    numbers = [1, 2, 3]
    
    numbers.upper()   #lists don't have upper()

except AttributeError as e:
    print("AttributeError caught!")
    print("Error message:", e)


try:
    text = "Hello Sheela"
    
    # Trying to call a method that does NOT exist
    result = text.reverse()  
    
    print(result)

except AttributeError as e:
    print("AttributeError caught!") 
    print("Error message:", e)
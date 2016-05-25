phone = {}
name = ""
numbrs = ""
while name != "exit":
    name = input("What is the person's name?")
    if name == "exit":
        print(phone)
    else:
        numbrs = input("Enter the corresponding phone number")
    phone[name] = (numbrs)
    
    

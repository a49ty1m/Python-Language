p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"
p5 = "buy this product now"

message = input("Enter your message: ")
if p1 in message or p2 in message or p3 in message or p4 in message or p5 in message:
    print("This is a spam message")
else:
    print("This is not a spam message")
# This code checks if a message contains any spam phrases and prints the appropriate response.
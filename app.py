print("Hello from pest pilot")
name = input("What is your name ?")
print("Nice to meet you, "+ name + "!")
pest= input("What pest are you treating?")
print ("You are treating " + pest + ".")

if pest.strip().lower() == "ants":
    print("Ant treatment information selected.")
elif pest.strip().lower() == "roaches":
    print("Roaches treatment information selected")
else:
    print("Treatment information is not available for this pest yet.")
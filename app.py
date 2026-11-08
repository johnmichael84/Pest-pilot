print("Hello from pest pilot")
name = input("What is your name ?")
print("Nice to meet you, "+ name + "!")
pest= input("What pest are you treating?")
print ("You are treating " + pest + ".")
if pest.strip().lower() == "ants":
    print("Ant treatment information selected.")
    print("Inspect ant trails, entry points, and nesting areas")
    print("Identify the ant species and nesting location before selecting a treatment")
    print("Seal entry points and remove accesible food and water sources")
elif pest.strip().lower() == "roaches":
    print("Roaches treatment information selected")
    print("Inspect kitchen, bathrooms, food sources, and moisture areas")
elif pest.strip().lower() == "mosquitoes":
    print("Mosquitoes treatment information selected")
    print("Inspect standing water, shaded areas, and dense vegetation")
else:
    print("Sorry, we do not have information for that pest.")
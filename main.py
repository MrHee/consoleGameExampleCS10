
#Console Game Class Example

#Snorkeling 

print("You've been snorkeling for an hour. You haven't seen a single octopus. Your dissapointment is overwhelming.")

print("Your octopus search has taken you away from the rest of your group. You can see them, far in the distance. A figure is approaching them. ")

print() #line break

print("You swim towards your friends and the mysterious figure. As you get closer, the mysterious figure draws a giant knife.")

print("<Options:>\n<LEAVE your friends to their fate>\n<SWIM as fast as you can to investigate.>\n<SEARCH around for a weapon of your own>\n")

choiceOne = input("What do you?\n>")


if choiceOne == "LEAVE":
  print("You leave your friends to their fate, swimming off in the other direction. Noone knows what happened to them. You never find an octopus.\n\nGAME OVER")
  exit()

elif choiceOne == "SEARCH":
  print("You search around wildly for a weapon. You reach toward a large log, but are bit on the finger by a hidden eel.\n\nIt sucks.\n\nGAME OVER")
  exit()

elif choiceOne == "SWIM":
  print("You swim as fast as you can back to your group. The man smiles at you as you approach. Then, as though realizing for the first time that he is carrying a giant, serrated, rusty knife, he laughs. \"You take the knife\" the man says, as he introduces himself.\nIt turns out, this man is a friendly octopus hunter named \"Big Wes\".")

else:
  print("Invalid input. Please enter one of the options from the list.")
  exit()


#This is where the second "scene" plays out. 
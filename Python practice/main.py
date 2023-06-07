print("Welcome to the quiz!")
playing = input("Shall we begin the game? ")
#print(playing)

if playing != "yes":
  quit()
#else: print(playing)

print("Okay! Let's play")
ans=input("full form of CPU?")
if ans == "central processing unit":
  print('Correct')
else:
  print("Incorrect!")
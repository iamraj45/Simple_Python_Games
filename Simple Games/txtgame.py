import time  # To add a pause

# User response
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]

required = ("\nUse only A, B, or C\n")  

#The story is broken into sections, starting with "intro"


def intro():
  print("One morning in Durgapur, You went to school and found that your best friend Megha was found dead."
  "You were with her last night at a party doing drugs and then you left for home.\n"
  "You are devastated by the news and at the same time worried that the Police will find something about drugs.\n"
  "You also are aware of the corrupt Police Department that they'd close the case without even investigating properly.\n"
  "You have to solve this case anyhow to find Megha's murderer and bring justice to her.\n"
  "\n"
  "Do you want to find her murderer?\n")
  time.sleep(1)
  print("""  A. Yes, definitely. She was your best friend.
  B. No, you're not a cop. Why would you?
  C. You're scared """)
  choice = input(">>> ")  # Your first choice
  if choice in answer_A:
    option_YES()
  elif choice in answer_B:
    print("\nYou failed "
          "\n\nYou had to solve the case to win.")
  elif choice in answer_C:
    option_SCARED()
  else:
    print(required)
    intro()


def option_YES():
  print("\nYou want to find out who killed Megha. "
        "\nNow, what will you do?")
  time.sleep(1)
  print("""  A. You got an idea. You know Ashi (Note- Ashi's father works in Police Station, He might be knowing what happened) 
  B. You go to Police and tell everything about last night
  C. You want to find everything on your own without anyone's help""")
  choice = input(">>> ")
  if choice in answer_A:
    option_DETAILS()
  elif choice in answer_B:
    print("\nYou made a bad move "
          "\nYou are busted for using drugs "
          "\nYou failed to solve the case")
  elif choice in answer_C:
    option_OWN()
  else:
    print(required)
    option_YES()


def option_OWN():
  print("\nNow you're on your own "
        "\nYou didn't take anyone's help"
        "\nWhat will you do next?")
  time.sleep(1)
  print("""  A. You try to break in the Police Station to find something about the case
  B. You regret your decision of not thinking straight
  C. You're sick of everything and leave everything""")
  choice = input(">>> ")
  if choice in answer_A:
    print("\nYou're caught sneaking into police files"
          "\nYou failed ")
  elif choice in answer_B:
    option_YES()
  elif choice in answer_C:
    print("\nYou failed"
          "You cannot leave everything on thier own. ")
  else:
    print(required)
    option_OWN()


def option_SCARED():
  print("\nYou are sacred as hell. "
        "\nWhat will you do next:")
  time.sleep(1)
  print("""  A. Calm down and think about finding the murderer
  B. Go back home and cry for loss of your friend
  C. You leave everything on itself to happen""")
  choice = input(">>> ")
  if choice in answer_A:
    print("\nGood, You need to find details about Megha's death ")
    option_DETAILS
  elif choice in answer_B:
    print("\nYou failed "
          "\n\nYou needed to find details about the murder")
  elif choice in answer_C:
    print("\nYou failed "
    "\nYou will never find what happened with Megha this way.")
  else:
    print(required)
    option_SCARED()


def option_DETAILS():
  print("\nYou need to find details of the case "
  "\nYou need Ashi's help for this. You will: ")
  time.sleep(1)
  print(""" A. Call Ashi and beg her to help you
    B. Talk to Ashi rudely to help you
    C. Blackmail her, You'll tell Ashi's dad about her relationship with local drug dealer(Ritik Roshan) """)
  choice = input(">>> ")
  if choice in answer_A:
    print("\nShe agrees to help you ")
    option_AGREES()
  elif choice in answer_B:
    print("\nYou failed"
    "\nShe denies to help you. You can't find Ashi's killer.")
  elif choice in answer_C:
    print("\nShe agrees to help you unwantedly, but it's fine as long as you're making a progress")
    option_AGREES()
  else:
    print(required)
    option_DETAILS()

def option_AGREES():
  print    


print("This game purely progresses on the choices you make."  # Game info
      "You have to solve the case to win."
      "\nDo you want to play? (Y/N)")

choice = input(">>> ")
if choice in yes:
  intro()
else:
  print("Then why are you here. Please leave.")

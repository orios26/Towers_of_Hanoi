from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]


#Set up the Game
num_disk = int(input("\nHow many disks do you want to play with?\n"))
while num_disk < 3:
  num_disk = int(input("\nEnter a number greater than or equal to 3\n"))

for i in range(num_disk, 0, -1):
  left_stack.push(i)

num_optimal_moves = (2**num_disk) -1
print("The fastest you can solve this game is in {} moves".format(num_optimal_moves))


#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    user_input = input("")

    if user_input in choices:
      for i in range(len(stacks)):
        return stacks[i]


#Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disk:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()

  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
      if from_stack.get_size() == 0:
      print("\n\nInvalid Move. Try Again")
      elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1
        break
        else: print("\n\nInvalid Move. Try Again")

print("You completed the game in {} moves. The optimal number of moves is {}".format(num_user_moves, num_optimal_moves))

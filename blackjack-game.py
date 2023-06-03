# modules
from random import randint as rand

# visual ascii art
print('''
      ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
      ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
      ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
      ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
      ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
      ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                          \n''')
# card numbers (change 1 to A)
cardNumbers = {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8,
                9 : 9, 10 : 10, 11 : "J", 12 : "Q", 13 : "K"}

# card suits
cardSuits = {1 : "♥", 2 : "♡", 3 : "♦", 4 : "♢", 5 : "♣", 6 : "♧", 7 : "♠", 8 : "♤"}

# event loop
while True:
  # generate random cards for both the player and the computer
  playerHand = [int(cardNumbers[rand(1,10)]), int(cardNumbers[rand(1,10)])]
  computerHand = [int(cardNumbers[rand(1,10)]), int(cardNumbers[rand(1,10)])]

  # total card sum
  playerSum = sum(playerHand)
  computerSum = sum(computerHand)
  
  # print both hands to the console
  print(f"\nYour hand: {playerHand}\nComputer's first card: {computerHand[0]}\n")

  # second while loop to give user cards or to end game if player is over 21
  while playerSum <= 21:
    # ask user to possibly take another card
    anotherCard = input("Type 'y' to get another card, type 'n' to stand.\n")
  
    if anotherCard == "y":
      
      # add new card to player hand
      playerHand.append(int(cardNumbers[rand(1,10)]))
      
      # recalculate player hand total
      playerSum = sum(playerHand)

      # display player hand
      print(f"\nYour current hand: {playerHand}\n")
  
    else:
      break

  # while loop to manage computer hand total if it is less than 17
  while computerSum < 17:

    # add new card to computer hand
    computerHand.append(int(cardNumbers[rand(1,10)]))

    # recalculate computer hand total
    computerSum = sum(computerHand)

  # display game results
  if (playerSum <= 21 and playerSum > computerSum):
    print("\nYou win!\n")
    print(f"\nYour total: {playerSum}.\nComputer total: {computerSum}.")
  elif (playerSum <= 21 and computerSum > 21):
    print("\nYou win\n!")
    print(f"\nYour total: {playerSum}.\nComputer total: {computerSum}.")
  else:
    print("\nYou lose!\n")
    print(f"\nYour total: {playerSum}.\nComputer total: {computerSum}.")

  # ask the player to play again or to quit
  playAgain = input("\nType 'y' to play again or type 'n' to quit.\n")

  if playAgain != "y":
    break
  
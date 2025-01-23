# This is a simple python script that was made in 100 Days Of Code Couse on day 3
print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

      ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure, are you ready?")
first_question = str(input("You have managed to enter the dungeon that contains riches, but to do so you must explore it.\nYour first decision: there is a fork, where do you go, right or left? ").lower())
if first_question == "right":
    print("Congratulations, you made the right choice and can continue exploring!")
    second_question = str(input("You continue walking until you come across a river, and then you have to decide whether to delay it by swimming or try to go around it.\nWhat do you choose to swim or bypass? ").lower())
    if second_question == "swim":
        third_question = str(input("You managed to swim across the river and everything was fine. Now it's time to get your prize. You came across 3 gates with different colored doors.\nChoose a color: blue, red or green: ").lower())
        if third_question == "blue":
            print("Unfortunately you chose the wrong door and came across a trap.\nGame Over.")
        elif third_question == "red":
            print("Congratulations!!! You chose the right door and managed to reach the treasure room! What\'s it like to be the new rich guy on the block?")
        elif third_question == "green":
            print("Unfortunately you chose the wrong door and came across hungry beasts.\n Game Over")
        else:
            print("Just try to choose the suggested words")
    elif second_question == "bypass":
        print("How can I say this? You walked for a long time until you ended up starving without being able to get around the river.\nGame Over.")
    else:
        print("Just try to choose the suggested words")
elif first_question == "left":
    print("Oh no! You ended up finding a Lion with eats and ended up dying..\nGame Over.")
else:
    print("Just try to choose the suggested words")

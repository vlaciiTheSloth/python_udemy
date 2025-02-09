# Section 3 main project - Treasure Island game

print("""               
               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|""")

dead = """

                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`

"""

win = """
             ..--------------------..
            |``--------------------''|
            |                        |
            |      ,,,;;;;;;,,,      |
            |   ,;;;;;;;;;;;;;;;;,   |
            |  ;;;;;;;;;;;;;;;;;;;;  |
            | ;;;;;;;;;'''  _  '';;; |
            |   _'''_  _   (_'  |  ` |
            |  |_) |_  |_) ._)  |    |
            | .|   |_  |     .....   |
            | :::..     ...::::::::: |
            |  ::::::::::::::::::::  |
            |   '::::::::::::::::'   |
            |      '''::::::'''      |
            |                        |
            |                        |
            ';----..............----;'
              '--------------------'
"""

print("Welcome to Treasure Island. Your mission is to find the treasure.")
left_or_right = str(input("Which way do you want to go? Left or right? "))
if left_or_right != "Left" and left_or_right != "left":
    print(f"You've fallen into a hole. Game over.\n{dead}")
else:
    swim_or_wait = str(input("You've arrived to a lake. Decide: would you like to wait or try to swim over? "))
    if swim_or_wait != "wait" and swim_or_wait != "Wait":
        print(f"You were attacked by a trout. Game over.\n{dead}")
    else:
        door = str(input("A boat came and took you to a house. You can enter 3 doors. Which one do you choose? Red, blue or yellow? "))
        if door != "yellow" and door != "Yellow":
            if door == "red" and door == "Red":
                print(f"Burned by fire. Game over.\n{dead}")
            elif door == "blue" and door == "Blue":
                print(f"Eaten by beasts. Game over.\n{dead}")
        else:
            print(f"You win!{win}")

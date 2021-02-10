try:

    pc_point = 0
    player_point = 0

    roundn = 0
    while roundn < 10:
        roundn = roundn + 1

        import random

        list2 = ["snake", "water", "gun"]
        list1 = random.choice(list2)

        print("\n snake , water , gun")
        inp1 = input("choose one of this : ")  # user input

        # if else statement start here
        if list1 == "snake" and inp1 == "water":
            print("computer choice", list1)
            print("computer won this round")
            pc_point += 1

        elif list1 == "water" and inp1 == "snake":
            print("computer choice", list1)
            print("you won this round")
            player_point += 1

        elif list1 == "gun" and inp1 == "water":
            print("computer choice", list1)
            print("you won this round")
            player_point += 1

        elif list1 == "water" and inp1 == "gun":
            print("computer choice", list1)
            print("computer won this round")
            pc_point += 1

        elif list1 == "gun" and inp1 == "snake":
            print("computer choice", list1)
            print("computer won this round")
            pc_point += 1

        elif list1 == "snake" and inp1 == "gun":
            print("computer choice", list1)
            print("you won this round")
            player_point += 1

        elif list1 == "snake" and inp1 == "snake":
            print("computer choice", list1)
            print("both are winners this round")
            pc_point += 1
            player_point += 1

        elif list1 == "gun" and inp1 == "gun":
            print("computer choice", list1)
            print("both are winners this round")
            pc_point += 1
            player_point += 1

        elif list1 == "water" and inp1 == "water":
            print("computer choice", list1)
            print("both are winners this round")
            pc_point += 1
            player_point += 1

        else:
            print("your input maybe wrong ! please try again")
        # finished code

        print("you have finished", roundn, "round , and you have", 10 - roundn, "left")

        if roundn == 10 and player_point < pc_point:
            print("\nGame is over")
            print("your point =", player_point, "and compuer point =", pc_point)
            print("Computer the winner of this game")

        elif roundn == 10 and player_point > pc_point:
            print("\nGame is over")
            print("your point =", player_point, "and compuer point =", pc_point)
            print("You are the winner of this game")

        elif roundn == 10 and player_point == pc_point:
            print("\nGame is over")
            print("your point =", player_point, "and compuer point =", pc_point)
            print("Both are the winner of this game")

except Exception as k:
    print(k)

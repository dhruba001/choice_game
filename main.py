print('WELCOME TO MY GAME OF CHOICE')
name = (input("WHAT IS YOUR NAME ? "))
age = int(input("WHAT IS YOUR AGE ? "))
print("HELLO", name, "YOU ARE", age, "YEARS OLD")
health = 10
if age >= 18 :
    print('YOU ARE OLD ENOUGH !')

    wants_to_play = input("DO YOU WANT TO PLAY ? (YES/NO) ").upper()
    if (wants_to_play == "YES"):
        print("let's play !")
        print('you are starting with',health,'health')
        direction = input('you want to go left or right (left/right)').lower()
        if direction == "left":
            option1 = input('there is a lake in your path do yo want to swim accross or go around (accross/around) ? ')
            if option1 == "around":
                print("good you went around")
            else:
                print("you went across and were bit by a fish and loose 5 health")
                health -= 5
                print('your health is ',health)
            option2 = input("you swim over and there is house which way to go (house/river)").lower()
            if option2 == "house":
                print('you are greeted by the owner and he shot you, you lost 5 health')
                health -= 5
                if health <= 0:
                    print('you have 0 health game over')
                else:
                    print("you survived game won")
            else:
                print('you fell into the river and lost')

        else:
            print('you fell down and died..game over !')
    else:
        print('see you later bye')
else:
    print('come back when you are 18 !')
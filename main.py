import random

# User config
user_life_points = 50
user_potions = 3

# Enemy config
enemy_life_points = 50
take_a_turn = False

while user_life_points > 0 and enemy_life_points > 0:

    if not take_a_turn:
        user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choice.isdigit() and user_choice == "1":

            user_attack_strength = random.randint(5, 10)
            enemy_attack_strength = random.randint(5, 15)

            user_life_points -= enemy_attack_strength
            enemy_life_points -= user_attack_strength

            print(f"Vous avez infligé {user_attack_strength} points de dégâts à l'ennemi ⚔️")
            print(f"L'ennemi vous a infligé {enemy_attack_strength} points de dégâts ⚔️")
            print(f"Il vous reste {user_life_points} points de vie.")
            print(f"Il reste {enemy_life_points} points de vie à l'ennemi.")
            print("------------------------------------------------------")

        elif user_choice.isdigit() and user_choice == "2":
            if user_potions > 0:

                take_a_turn = True
                user_potions -= 1
                potion_value = random.randint(15, 50)
                user_life_points = user_life_points + potion_value
                print(f"Vous avez récupéré {potion_value} points de vie ❤️({user_potions} 🧪 restante{'s' if user_potions > 1 else ''})")

                enemy_attack_strength = random.randint(5, 15)
                user_life_points -= enemy_attack_strength

                print(f"L'ennemi vous a infligé {enemy_attack_strength} points de dégâts ⚔️")
                print(f"Il vous reste {user_life_points} points de vie.")
                print(f"Il reste {enemy_life_points} points de vie à l'ennemi.")
                print("------------------------------------------------------")
            else:
                print("Vous n'avez plus de potion.")
    else:
        print("Vous passez votre tour...")
        enemy_attack_strength = random.randint(5, 15)
        user_life_points -= enemy_attack_strength
        take_a_turn = False

        print(f"L'ennemi vous a infligé {enemy_attack_strength} points de dégâts ⚔️")
        print(f"Il vous reste {user_life_points} points de vie.")
        print(f"Il reste {enemy_life_points} points de vie à l'ennemi.")
        print("------------------------------------------------------")

if user_life_points >= 0:
    print("Vous avez gagné 💪 !")
else:
    print("Vous êtes mort 💀! Votre ennemi a gagné !")

print("Fin du jeu.")

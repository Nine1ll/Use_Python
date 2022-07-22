
# human = Character()
#
# human.move()
# human.check_health()
#
# human.move()
# human.check_health()
#
# human.rest()
# human.check_health()

class Character:
    def __init__(self):
        self.health = 200

    def move(self):
        print("움직 입니다. 체력이 10 감소 합니다.")
        self.health -= 10

    def rest(self):
        print("잠시 쉬었 습니다. 체력이 10 증가 합니다.")
        self.health += 10

    def check_health(self):
        print(f"현재의 체력은 {self.health} 입니다.\n")


class Knight(Character):
    def __init__(self):
        super().__init__()

    def move(self):
        print("움직 입니다. 체력이 15 감소 합니다.")
        self.health -= 15

    def attack(self):
        print(f"공격 합니다.")

class Healer(Character):
    def __init__(self):
        super().__init__()
        self.mana = 100

    def heal(self, character):
        print("아군을 힐 합니다. 마나를 10 소모 하고, 아군의 체력이 10 상승 합니다.")
        self.mana -= 10
        character.rest()

    def check_mana(self):
        print(f"현재 힐러의 마나는 {self.mana} 입니다.")



cleric = Healer()
knight = Knight()

knight.move()
knight.move()
knight.move()
knight.check_health()

cleric.heal(knight)
knight.check_health()
cleric.check_mana()

cleric.heal(knight)
knight.check_health()
cleric.check_mana()

cleric.heal(knight)
knight.check_health()
cleric.check_mana()

knight.attack()
knight.attack()
knight.attack()
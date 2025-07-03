class MobileSuit:

    def __init__(self, name, hp, power, defense):
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense

    def attack(self, enemy_name):
        print(f"{self.name} 攻击了 {enemy_name}")


gundam = MobileSuit("Gundam", 100, 50, 30)
gundam.name = "Gundam"
gundam.attack("zaku")

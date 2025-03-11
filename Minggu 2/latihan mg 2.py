#DIWAN RAMADHANI DWI PUTRA
#123140116
#PBO RA

import random # Import modul random untuk generate angka random

class Robot(): # Class Robot untuk membuat objek robot
    def __init__(self, name, attack, hp): # Method untuk inisialisasi objek robot
        self.name = name
        self.attack = attack
        self.hp = hp
        self.defending = False # Penanda digunakan untuk menandai apakah robot sedang defense atau tidak
        self.armor = 0.1  # 10% pengurangan damage berdasarkan HP saat diserang
        self.last_recover = -2  # Untuk melacak ronde terakhir recover

    # Method untuk menambah HP robot
    def recover(self, round_number):
        if self.hp <= 0:
            print(f"{self.name} kalah, tidak bisa nambah HP")
            return
        if round_number - self.last_recover == 1:
            print(f"{self.name} tidak bisa recover di ronde ini, harus menunggu 1 ronde.")
            return
        
        hp_sblmnya = self.hp #nyimpen hp sblmnya

        if self.hp + 10 > 100:
            self.hp = 100
        else:
            self.hp += 10
        self.last_recover = round_number #update ke ronde terakhir recover
        print(f"{self.name} nambah HP. HP sekarang = {hp_sblmnya} + 10 = {self.hp}")

    # Method untuk menyerang musuh
    def attack_enemy(self, target):
        if target.hp <= 0:
            print(f"Musuh {target.name} kalah")
            return # Keluar dari method jika target kalah
        
        # Menghitung akurasi berdasarkan HP target
        accuracy = max(0.5, target.hp / 100)  # Akurasi minimal 50% serta berkurang seiring berkurangnya HP target
        if random.random() > accuracy: # random.random() menghasilkan angka random antara 0-1
            print(f"{self.name} missed attack ke {target.name} karna kurang akurasi!")
            return

        # Jika target dalam mode defense, kurangi damage berdasarkan armor
        if target.defending:
            reduction = target.armor * target.hp  # 10% dari HP target
            effective_damage = self.attack - reduction # Kurangi damage dengan reduction
            if effective_damage < 0:
                effective_damage = 0
            print(f"{target.name} make defense. Damage dikurangi {reduction:.2f} jadi {effective_damage}") # Menampilkan damage yang diterima setelah defense
            target.defending = False  # Reset tanda defense setelah diserang
        else:
            effective_damage = self.attack

        # ngasih damage dan cek apakah target kalah
        if target.hp - effective_damage <= 0:
            target.hp = 0
            print(f"Musuh {target.name} kalah")
        else:
            target.hp -= effective_damage
            print(f"{self.name} attack {target.name}. Damage = {effective_damage}")
    # Method untuk defense robot
    def defense(self):
        if self.hp <= 0:
            print(f"{self.name} sudah kalah")
            return
        self.defending = True
        print(f"{self.name} make defense. Armor aktif untuk next attack")
    # Method untuk surend robotnya
    def giveup(self):
        self.hp = 0
        print(f"{self.name} surrend")

# Class Game untuk mengatur jalannya game
class Game():
    def __init__(self, robot1, robot2): # Menginisialisasi robot yang akan bertarung
        self.robot1 = robot1 # robot1 adalah atribut 
        self.robot2 = robot2

    def start_game(self):# Method untuk memulai game
        round_number = 1
        print(f"HP awal saat ini :")
        print(f"{self.robot1.name} HP: {self.robot1.hp}")
        print(f"{self.robot2.name} HP: {self.robot2.hp}")
        print()
        while self.robot1.hp > 0 and self.robot2.hp > 0: # Looping selama kedua robot masih hidup
            print(f"=== Round {round_number} ===")
            action1 = input(f"{self.robot1.name}: 1.Attack 2.Defense 3.Regen Health 4.Giveup: ")
            action2 = input(f"{self.robot2.name}: 1.Attack 2.Defense 3.Regen Health 4.Giveup: ")
            print()

            # Eksekusi aksi untuk robot1
            if action1 == "1":
                self.robot1.attack_enemy(self.robot2)
            elif action1 == "2":
                self.robot1.defense()
            elif action1 == "3":
                self.robot1.recover(round_number)
            elif action1 == "4":
                self.robot1.giveup()
            else:
                print(f"{self.robot1.name}: Aksi tidak valid.")

            # Cek apakah robot2 sudah hancur sebelum giliran robot2
            if self.robot2.hp <= 0:
                print(f"{self.robot2.name} kalah. Game Over.")
                break

            # Eksekusi aksi untuk robot2
            if action2 == "1":
                self.robot2.attack_enemy(self.robot1)
            elif action2 == "2":
                self.robot2.defense()
            elif action2 == "3":
                self.robot2.recover(round_number)
            elif action2 == "4":
                self.robot2.giveup()
            else:
                print(f"{self.robot2.name}: Aksi tidak valid.")

            print()
            print(f"HP saat ini untuk ronde {round_number + 1} :")
            print(f"{self.robot1.name} HP: {self.robot1.hp}")
            print(f"{self.robot2.name} HP: {self.robot2.hp}")
            print()

            round_number += 1

        # Menentukan pemenang
        if self.robot1.hp > self.robot2.hp:
            print(f"{self.robot1.name} menang!")
        elif self.robot1.hp < self.robot2.hp:
            print(f"{self.robot2.name} menang!")
        else:
            print("Seri")


# Contoh instansiasi dan pemanggilan game
dialga = Robot("Dialga", 35, 100)
palkia = Robot("Palkia", 30, 100)
game = Game(dialga, palkia)
game.start_game()
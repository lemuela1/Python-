from tkinter import *

root = Tk()
root.wm_title('勇者斗恶龙')


# function
def mage_grow():
    if P1.EXP >= 100:
        P1.INT *= 2
        P1.MANA += 20
        P1.EXP -= 100
    if P1.EXP <= 100:
        Label(root, text='您的经验值不足').grid(row=5, column=0)
    Label(root, text=f'MP:{PlayerMAX_MANA}/{P1.MANA}').grid(row=4, column=1)
    Label(root, text=f'STR:{P1.STR}').grid(row=4, column=2)
    Label(root, text=f'INT:{P1.INT}').grid(row=4, column=3)
    Label(root, text=f'EXP:{P1.EXP}').grid(row=4, column=4)
    root.mainloop()
def str_grow():
    if P1.EXP >= 100:
        P1.STR *= 2
        P1.EXP -= 100
    if P1.EXP <= 100:
        Label(root, text='您的经验值不足').grid(row=5, column=0)
    Label(root, text=f'MP:{PlayerMAX_MANA}/{P1.MANA}').grid(row=4, column=1)
    Label(root, text=f'STR:{P1.STR}').grid(row=4, column=2)
    Label(root, text=f'INT:{P1.INT}').grid(row=4, column=3)
    Label(root, text=f'EXP:{P1.EXP}').grid(row=4, column=4)
    root.mainloop()
def mage_attack():
    Damage = Player.INT * 3
    Player.MANA -= 20
    D1.health -= Damage
    Label(root, text=f'HP:{DMAX_health}/{D1.health}  STR:{D1.STR}').grid(row=1, column=0)
    if P1.health <= 0:
        Button(root, text='attack', command=attack, padx=30, pady=10, state=DISABLED).grid(row=2, column=1)
        Label(root, text=f'You Die').grid(row=5, column=0)
    if D1.health <= 0:
        P1.EXP += 10
        D1.health = DMAX_health
    Label(root, text=f'EXP:{P1.EXP}').grid(row=4, column=4)
    root.mainloop()

def attack():
    Damage = Player.STR * 2
    D1.health -= Damage
    P1.health -= D1.STR
    Label(root, text=f'HP:{PMAX_health}/{P1.health}').grid(row=4, column=0)
    Label(root, text=f'HP:{DMAX_health}/{D1.health}  STR:{D1.STR}').grid(row=1, column=0)
    if P1.health <= 0:
        Button(root, text='attack', command=attack, padx=30, pady=10, state=DISABLED).grid(row=2, column=1)
        Label(root, text=f'You Die').grid(row=5, column=0)
    if D1.health <= 0:
        P1.EXP += 10
        D1.health = DMAX_health
    Label(root, text=f'EXP:{P1.EXP}').grid(row=4, column=4)


class Player:
    health = 100
    STR = 10
    INT = 10
    MANA = 200
    EXP = 0


class Dragon:
    health = 150
    STR = 15
    INT = 15
    MANA = 300


P1 = Player()
D1 = Dragon()

# layout
Label(root, text='恶龙').grid(row=0, column=0)
DMAX_health = D1.health
Label(root, text=f'HP:{DMAX_health}/{D1.health}  STR:{D1.STR}').grid(row=1, column=0)
Label(root, text='').grid(row=2, column=0)
Label(root, text='勇者').grid(row=3, column=0)
PMAX_health = P1.health
PlayerMAX_MANA = P1.MANA
Label(root, text=f'HP:{PMAX_health}/{P1.health}').grid(row=4, column=0)
Label(root, text=f'MP:{PlayerMAX_MANA}/{P1.MANA}').grid(row=4, column=1)
Label(root, text=f'STR:{P1.STR}').grid(row=4, column=2)
Label(root, text=f'INT:{P1.INT}').grid(row=4, column=3)
Label(root, text=f'EXP:{P1.EXP}').grid(row=4, column=4)
Button(root, text='attack', command=attack, padx=30, pady=10).grid(row=2, column=1)
Button(root, text='mage_attack', command=mage_attack, pady=10, padx=30).grid(row=2, column=2)
Button(root, text='mage_grow', command=mage_grow, padx=30, pady=10).grid(row=3, column=1)
Button(root, text='STR_grow', command=str_grow, padx=30, pady=10).grid(row=3, column=2)
root.mainloop()

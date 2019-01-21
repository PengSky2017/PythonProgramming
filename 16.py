class Hero():
    def __init__(self, name, grade, blood):
        self.name = name
        self.grade = grade
        self.blood = blood
        self.q_hurt = 0
        self.w_hurt = 0
        self.e_hurt = 0

    def q(self, hero):
        hero.blood -= self.q_hurt
        print('{}收到{}伤害'.format(hero.name, self.q_hurt))

    def w(self, hero):
        hero.blood -= self.w_hurt
        print('{}收到{}伤害'.format(hero.name, self.w_hurt))

    def e(self, hero):
        hero.blood -= self.e_hurt
        print('{}收到{}伤害'.format(hero.name, self.e_hurt))

    def state(self):
        if self.blood == 0:
            print('{} died!'.format(self.name))


hero1 = Hero('yase', 1, 100)
hero1.q_hurt = 50
hero1.w_hurt = 10
hero1.e_hurt = 10

hero2 = Hero('xiahd', 1, 100)
hero2.q_hurt = 10
hero2.w_hurt = 10
hero2.e_hurt = 10

hero1.q(hero2)
print(hero2.blood)
hero1.q(hero2)
print(hero2.blood)


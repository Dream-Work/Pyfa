from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Dominix"

    # Gallente Battleship Skill Bonus:
    # 5% bonus to Large Hybrid Turret damage per skill level

    def test_gallenteBattleship_damageMultiplier_moduleHybridWeaponLarge(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Neutron Blaster Cannon I"
        skill = "Gallente Battleship"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteBattleship_damageMultiplier_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "250mm Railgun I"
        skill = "Gallente Battleship"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Battleship Skill Bonus:
    # 10% bonus to drone hitpoints per skill level

    def test_gallenteBattleship_hp_droneCombat(self):
        self.buildTested = 0
        item = "Ogre I"
        skill = "Gallente Battleship"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteBattleship_hp_droneLogistic(self):
        self.buildTested = 0
        item = "Heavy Shield Maintenance Bot I"
        skill = "Gallente Battleship"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteBattleship_hp_droneEwar(self):
        self.buildTested = 0
        item = "Wasp EC-900"
        skill = "Gallente Battleship"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteBattleship_hp_droneCapDrain(self):
        self.buildTested = 0
        item = "Praetor EV-900"
        skill = "Gallente Battleship"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteBattleship_hp_droneWeb(self):
        self.buildTested = 0
        item = "Berserker SW-900"
        skill = "Gallente Battleship"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteBattleship_hp_droneMining(self):
        self.buildTested = 0
        item = "Mining Drone I"
        skill = "Gallente Battleship"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Battleship Skill Bonus:
    # 10% bonus to drone damage per skill level

    def test_gallenteBattleship_damageMultiplier_droneCombat(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Infiltrator I"
        skill = "Gallente Battleship"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteBattleship_damageMultiplier_other(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "1200mm Artillery Cannon I"
        skill = "Gallente Battleship"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

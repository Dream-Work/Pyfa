from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Small Artillery Specialization"

    # 2% bonus per skill level to the damage of small turrets requiring Small Artillery Specialization.

    def test_damageMultiplier_moduleWithSkillrq(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "280mm Howitzer Artillery II"
        iLvl = 1
        iIngame = 1.02
        fLvl = 4
        fIngame = 1.08
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl))
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl))
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_damageMultiplier_moduleNoSkillrq(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "280mm Howitzer Artillery I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl))
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl))
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

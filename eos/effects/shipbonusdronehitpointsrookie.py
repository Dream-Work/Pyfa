# Used by:
# Ship: Gnosis
# Ship: Taipan
# Ship: Velator
type = "passive"
def handler(fit, ship, context):
    for type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                     type, ship.getModifiedItemAttr("rookieDroneBonus"))
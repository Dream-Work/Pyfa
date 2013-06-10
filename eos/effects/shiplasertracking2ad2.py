# Used by:
# Ship: Coercer
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Destroyer").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("shipBonusAD2") * level)

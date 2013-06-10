# Used by:
# Modules named like: Particle Dispersion Projector (8 of 8)
# Skill: Long Distance Jamming
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM Burst",
                                  "ecmBurstRange", container.getModifiedItemAttr("rangeSkillBonus") * level,
                                  stackingPenalties = False if "skill" in context else True)

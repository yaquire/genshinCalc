import math

totalDamagePossible = (BaseDMG * BaseDamageMulti)+AdditiveBaseDMGBonus*DMGBonusMulti*TargetDEFMulti*TargetRESMulti*AmplifyingMulti
CritDamgeMulti = totalDamagePossible*(1+CritDMGPercent)

#if ability scales with TPYE
if scaleableAbility == Attack:
  BaseDMG = abilityPercent * Attack


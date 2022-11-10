# x --------- R ----------->
# 0

batteryCharge = 70    # %
ratePerStep = 10      # 10%/m scade per metru sau per pas parcurs

steps = 0

# estimatedSteps = batteryCharge / ratePerStep
# print("Steps Remaining", estimatedSteps)

# Compexity cods
# DRY - Do not Repeat yourself
while batteryCharge > 0:
    steps += 1  # incriment
    batteryCharge -= ratePerStep # decriment
    print("steps: ", steps, "battery: ", batteryCharge)
    if batteryCharge <= 10:
        print(" Warning!!! need to charge battery." )
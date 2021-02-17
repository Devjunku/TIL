orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
newmenu ={}

for order in orders:
    for orde in order:
        newmenu[orde] = newmenu.get(orde, 0) + 1
print(newmenu)
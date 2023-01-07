xa = float(input('Write x punktu A: '))
ya = float(input('Write y punktu A: '))
xb = float(input('Write x punktu B: '))
yb = float(input('Write y punktu B: '))
xc = float(input('Write x punktu C: '))
yc = float(input('Write y punktu C: '))

area = abs(0.5 * (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa))

print(f"Area triangle equal: {area}")
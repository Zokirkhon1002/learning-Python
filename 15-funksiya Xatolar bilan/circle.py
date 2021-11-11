def getArea(r,pi=3.14159):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)

def getPerimetr(r,pi=3.14159):
    """Doiraning perimetrini qaytaruvchi funkisya"""
    return 2*pi*r

print(getArea(5))
print(getPerimetr(5))
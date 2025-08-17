def main():

    mass = int(input("m: "))

    energy(mass)


def energy(m):

    c = 300000000

    E = m * (c ** 2)
    print(f"E: {E}")  


main()

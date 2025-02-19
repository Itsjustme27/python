def five(y,z):
    def add():
        return y+z
    return add() + 5

def main():
    result = five(1,1)
    print(result)


if __name__ == "__main__":
    main()

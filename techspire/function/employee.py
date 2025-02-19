def employee(name, salary=9000):
    return name, salary

def main():
    result_1 = employee("ram", 19999)

    # When no arguments is passed
    result_2 = employee("hari")

    print(result_1)
    print(result_2)

if __name__ == "__main__":
    main()


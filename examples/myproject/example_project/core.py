class Unused:
    def __init__(self):
        pass


unused_var = 'this is a unused variable'
used_var = 'this is a used variable'

def func_used():
    print(used_var)
    print("This function is actually used")


def func_not_used():
    print("This function is not used.")
    return False
    print("This is unreachable code")


def main():
    func_used()


if __name__ == '__main__':
    main()


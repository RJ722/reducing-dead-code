def increase_power():
    return 1

def power_increase():
    return 0

def main():
    print("Hello")
    # Use power_increase
    power_increase()
    # Now, we wanted to use increase_power()
    # But, we were confused and instead used power-increase()
    power_increase()
    return 0

if __name__ == '__main__':
    main()


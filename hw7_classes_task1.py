def calc_salt(amount):
    try:
        x = int(amount) / 100
        return x
    except ValueError:
        print("invalid literal for int() with base 10: 'abc'")
        return 0.0

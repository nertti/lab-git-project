from utils import add_numbers, multiply_numbers

def main():
    x, y = 5, 10
    print(f"Сумма чисел - {x} и {y}: {add_numbers(x, y)}")
    print(f"Произведение чисел - {x} и {y}: {multiply_numbers(x, y)}")

if __name__ == "__main__":
    main()

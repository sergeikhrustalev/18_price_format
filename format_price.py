

def format_price(price):

    try:
        price = float(price)
    except ValueError:
        return

    if price < 0:
        return

    price = str(int(round(price)))

    price = price[::-1]

    price = ' '.join(price[char:char+3] for char in range(0, len(price), 3))

    price = price[::-1]

    return price


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('price', type=float)
    arguments = parser.parse_args()

    print(format_price(arguments.price))

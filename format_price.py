

def format_price(price):

    try:
        price = float(price)
    except ValueError:
        return

    if price < 0:
        return

    price = int(round(price))

    return '{0:,}'.format(price).replace(',', ' ')


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('price', type=float)
    arguments = parser.parse_args()

    print(format_price(arguments.price))

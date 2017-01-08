import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="This script can change price to format",
    )
    parser.add_argument('--price')
    return parser.parse_args()


def format_price(price):
    if price is None:
        return ''
    only_digits_in_price = str(price)
    for char in ['e', 'E', '.', ',', ' ', '+', '-']:
        only_digits_in_price = only_digits_in_price.replace(char, '')
    if not only_digits_in_price.isdigit():
        return 'Incorrect value'
    price = float(str(price).replace(',', '.'))
    if price.is_integer():
        return '{:,.0f}'.format(float(price)).replace(',', ' ')
    else:
        return '{:,.2f}'.format(float(price)).replace(',', ' ')


if __name__ == '__main__':
    args = get_args()
    print(format_price(args.price))

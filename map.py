from tabulate import tabulate

def print_map():
    """prints map of Cambell"""
    map = [['', 'English'],
          ['Math   ', 'Main Hall', 'History'],
          ['', 'French', ]]
    print(tabulate(map, tablefmt="grid"))

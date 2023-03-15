import argparse

parser = argparse.ArgumentParser(
    prog='Image bulk resizer',
    description='It can resize all images in specific directory',
    epilog='Author: A'
)

parser.add_argument('path', type=str)
parser.add_argument('target', type=str)
parser.add_argument('--width', type=int, default=300)
parser.add_argument('--height', type=int, default=300)

arguments - parser.parse_args()
print('path', arguments.path)
print('target', arguments.target)
print('width', arguments.width)
print('height', arguments.height)
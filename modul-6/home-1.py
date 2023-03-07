import pytest


def return_sentence(**kwargs):
    result = []
    for k,v in kwargs.items():
        result.append(f'{k.title()} is {v}')

    return '\n'.join(result)



def test_return_sentence():
    assert return_sentence(wall="red", tomato="red") == 'Wall is red\nTomato is red'


print(return_sentence(wall="red", tomato="red", light="yellow", lemon="yellow", grass="green"))

import requests

def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y

# in c++ this will all need a static keyword
# def requestData(self,moth) while this is the normal method request an instance of a class
def requestData(month):
    response = requests.get(f'http://company.com/{month}')
    if response.ok:
        return response.text
    else:
        return 'Bad Response!'

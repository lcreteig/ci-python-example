import pyjokes

def tell():
    the_joke = pyjokes.get_jokes()
    print(the_joke)
    return the_joke

if __name__ == '__main__':
    tell()
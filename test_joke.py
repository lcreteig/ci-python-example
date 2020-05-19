import joke

def test_is_string():
    the_joke = joke.tell()
    assert type(the_joke) == str, "The joke is not a string..."
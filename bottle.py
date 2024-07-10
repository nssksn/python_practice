def bottles_of_beer(bob):
    """Prints Bottle of Beer on the wall Lyrics.
    :param bob: Must be a positive integer.
    """
    if bob < 1:
        print("""No more bottles of beer on the wall.
              No more bottle of beer.""")
        return

    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall.
            {} bottles of beer.
            Take one down, pass it around,
            {} bottles of beer on the wall.
            """.format(tmp, tmp, tmp))
    bottles_of_beer(bob)

bottles_of_beer(99)

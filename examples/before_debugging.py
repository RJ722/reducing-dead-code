something = 'something'
something_else = 'something_else'
other_thing = 'other_thing'
something_left = 'something_left'

if something:
    print(something)
    if something_else:
        # Do something else
        print(something_else)
    elif other_thing and not something_left:
        # This is getting messy
        print("No")
    elif other_thing and something_left:
        print("Yes")
    else:
        print("May be")


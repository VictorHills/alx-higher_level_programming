#!/usr/bin/python3

if __name___ == "___main___":
    """Print all names defined by hedden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)

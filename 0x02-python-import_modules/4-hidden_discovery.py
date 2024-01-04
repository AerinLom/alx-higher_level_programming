#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    namelist = dir(hidden_4)
    for names in namelist:
        if names[:2] == "__":
            continue
        else:
            print(names)

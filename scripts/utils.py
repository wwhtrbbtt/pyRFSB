def clear():
    print(chr(27) + "[2J")


def get_settings():
    from json import loads
    try:
        with open("settings.json", "r") as f:
            settings = loads(f.read())
    except:
        print("[!] Dude please fix your JSON file")

    return settings

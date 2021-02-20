def available_emojis():
    return [
        # normal
        ":lightbulb:",
        ":huh:",
        ":biggrin:",
        ":dodgy:",
        ":at:",
        ":shy:",
        ":confused:",
        ":rolleyes:",
        ":sleepy:",
        ":sick:",
        ":exclamation:",
        ":sad:",
        ":angel:",
        ":arrow:",
        ":blush:",
        ":succ:",
        # simple
        ";(",  # AKA cry
        ":)",  # AKA smile
        "<3",  # AKA hearth
        ":P",  # AKA tongue
        ";)",  # AKA wink
        # raidforums specific
        "Kappa",  # normal kappa (without color)
        "KappaHD",  # normal kappa (with color)
        "KappaPride",  # rainbow kappa
        "Keepo",  # kappa with cat ears
        "KappaRoss",  # kappa with bob ross hair
        "newfag",
        "nazimods",
        "rustbin",
        "pjsalt",
        "rfskid",
        "illuminati",
        "normie",
        "BumpyRide",
        "moonman",
    ]


def commands(msg):
    if msg == "/open":
        import webbrowser
        webbrowser.open("https://raidforums.com")

    elif msg == "/emojis":
        for x in available_emojis():
            print(x)

    elif msg == "/commands":
        print("/open - open raidforums.com in your browser")
        print("/emojis - see all available emojis")
        print("/commands - see all available commands")

    # elif msg == "/signature":
    #     print("ok")

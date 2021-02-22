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
        print("/setsignature <newSignature> - change your signature")
        print("/togglelog - toggle if you wanna log all messages into a text file")
        print("/toggledebug - toggle debug mode")

    elif msg.startswith("/setsignature "):
        from scripts.client import change_signature

        new = msg.split(" ")[1:]
        if type(new) == list:
            new = " ".join(new)
        change_signature(new)
        print(f"[!] Changed your signature to '{new}'")

    elif msg.startswith("/togglelog"):
        from scripts.client import toggle_log
        toggle_log()
        # print("Toggled your logging settings")

    elif msg.startswith("/toggledebug"):
        from scripts.client import toggle_debug
        toggle_debug()

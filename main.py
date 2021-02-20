from scripts.utils import clear, get_settings
from scripts.client import main

if __name__ == "__main__":
    settings = get_settings()
    main(
        settings["debug"],
        settings["signature"],
        settings["token"]
    )




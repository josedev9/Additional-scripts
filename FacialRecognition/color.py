class Color:
    """Color class for quick formatting.
    ===

    Quick example:
    ---

    print(Color.BOLD + 'Hello World !' + color.END)
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
print(f"{Color.BOLD}{Color.RED}Hello world!")
print("Hello world")
import textwrap
import os
import subprocess

# Kaunis viiva
fancyLine = "\n───◇ ◆ ◇─────────────────────────────────────────────────────────────────────\n\n"

# Jakaa tekstin riveihin
def divide(text):
    lines = textwrap.wrap(text, width=64)
    return "» " + "\n  ".join(lines)

# Tyhjentää terminaalin
def clear_shell():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
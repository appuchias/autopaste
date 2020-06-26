import keyboard, pyperclip, os

fn = input("Type the filename:\n> ")

try:
    with open("fp.txt") as r:
        fp = r.read()
except FileNotFoundError:
    with open("fp.txt", "x"):
        pass
    fp = input("Type the folder where to save all the files:\n> ")

path = os.path.join(fp, fn)

with open(path, "a") as a:
    while True:
        if keyboard.read_key() == "esc":
            raise SystemExit

        copy = pyperclip.waitForNewPaste()
        a.write(copy + "\n")
        print(copy)

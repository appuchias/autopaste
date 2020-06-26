import keyboard, pyperclip, os

try:
    with open("fp.txt") as r:
        fp = r.read()
except FileNotFoundError:
    with open("fp.txt", "x"):
        pass
    fp = input("Type the folder where to save all the files:\n> ")

fn = input("Type the filename:\n> ")

if fn[:-4] != ".txt":
    fn =+ ".txt"

path = os.path.join(fp, fn)

with open(path, "a") as a:
    while True:
        if keyboard.read_key() == "esc":
            raise SystemExit

        copy = pyperclip.waitForNewPaste()
        a.write(copy + "\n")
        print(copy)

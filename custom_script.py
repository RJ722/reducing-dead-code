from vulture import Vulture

vulture = Vulture()

files = ['file1.py', 'file2.py']
vulture.scavenge(files)

for item in vulture.get_unused_code():
    # filter items
    print(item)

import os

directory = "developer/scripts/version_detector/"

if not directory.endswith('/'):
    directory = directory + "/"

OGcompare = open(f"{directory}compare.txt").read()
OGcontrast = open(f"{directory}contrast.txt").read()

compare = OGcompare
contrast = OGcontrast

compare_array = compare.split('\n')
contrast_array = contrast.split('\n')

compare = ""
compare_version_index = 0
for item in compare_array:
    if item == "||":
        compare_version_index = compare_version_index + 2
        break
    compare = compare + item + "\n"
    compare_version_index = compare_version_index + 1
compare = compare.removesuffix('\n')

contrast = ""
contrast_version_index = 0
for item in contrast_array:
    if item == "||":
        contrast_version_index = contrast_version_index + 2
        break
    contrast = contrast + item + "\n"
    contrast_version_index = contrast_version_index + 1
contrast = contrast.removesuffix('\n')

compare_array = compare.split('\n')
contrast_array = contrast.split('\n')

compare_version = OGcompare.split("\n")[compare_version_index - 1]
contrast_version = OGcontrast.split("\n")[contrast_version_index - 1]

os.system('cls')

version_array = []
version_array = compare_version.removeprefix('v').split('.')

if contrast_version_index < compare_version_index + 5:
    print("Small Update compared to the last. Patch number should increase")
    version_array[2] = str(int(version_array[2]) + 1)
elif contrast_version_index < compare_version_index + 10:
    print("Big Update compared to the last. Minor number should increase")
    version_array[2] = "0"
    version_array[1] = str(int(version_array[1]) + 1)
elif contrast_version_index >= compare_version_index + 10:
    print("Massive Update compared to the last. Major number should increase")
    version_array[2] = "0"
    version_array[1] = "0"
    version_array[0] = str(int(version_array[0]) + 1)

version_string = "v"

for item in version_array:
    version_string = version_string + item + "."

version_string = version_string.removesuffix('.')
print(version_string)
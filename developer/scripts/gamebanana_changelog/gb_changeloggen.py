# This script automatically generates a Bulk changelog to add onto gamebanana
# 1.0 - Base Script

# Written by Sphis_Sinco for "Fun over Money".
# This cool little minecraft mod ;)
# https://gamebanana.com/mods/569653

# Changelog variables
changelog = ""
gamebanana_changelog = ""

# progress variables
progress = 0
max_progress = 0

# read the log.txt file
f = open("developer/scripts/gamebanana_changelog/log.txt", "r")
changelog = f.read()

# set the array_logs and max_progress variables
array_logs = changelog.split('\n')
max_progress = array_logs.__len__()

# this function does the actual ", {changelog entry type}"
def checkFor(checking, prefix, suffix):
    returnval = ""

    if checking.startswith(f"- {prefix} ") :
        returnval = checking.removeprefix(f"- {prefix} ")
        returnval = returnval + f", {suffix}"

        return returnval

    return checking

index = 0
for entry in array_logs:
    addition = entry

    # check for different keywords after seeing if the current entry is a changelog entry
    if entry.startswith('- '):
        addition = checkFor(addition, "Added", "Addition")
        addition = checkFor(addition, "Removed", "Removal")
        addition = checkFor(addition, "Reworked", "Overhaul")
        addition = checkFor(addition, "Changed", "Tweak")
        addition = checkFor(addition, "Fixed", "Bugfix")

    gamebanana_changelog = gamebanana_changelog + addition

    # prevent extra line break
    if index + 1 != array_logs.__len__():
        gamebanana_changelog = gamebanana_changelog + "\n"


    index=index + 1
    progress = progress + 1

    # print progress
    print(f"Progress: {round(progress/max_progress*100)}%")


# write to the final_log.txt file
the_log = open('developer/scripts/gamebanana_changelog/final_log.txt', 'w')
the_log.write(gamebanana_changelog)
print("Written to developer/scripts/gamebanana_changelog/final_log.txt")
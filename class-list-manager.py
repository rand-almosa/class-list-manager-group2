
# Class List Manager - Group 2

# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Rand (task 3)

def sort_names(names):
    return sorted(names)

# Written by: Leen (task 7)
def count_vowels(names):
    count = 0
    for letter in names.lower():
        if letter in "aeiou":
           count += 1
    return count


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Sorted names:", sort_names(names))
    print("Vowels in first name:", count_vowels(names[0]))
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))


main()

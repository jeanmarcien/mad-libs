# This is Python script to play a Mad Libs game.

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   ITALIC = '\033[3m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print("\nHello!"
      "\nGet a friend or do this ridiculous word game on your own. "
      "\nCome up with words that fit with the parts of speech listed on this page. "
      "\nThen fill in the matching blanks on the next page to create a nonsensical story! ")

print("\nPlease, insert your ideas below.")
proper_noun_1 = input("1. Proper Noun: ")
noun_1 = input("2. Noun: ")
adjective_1 = input("3. Adjective (Feeling): ")
verb_1 = input("4. Verb: ")
adjective_2 = input("5. Adjective (Feeling): ")
animal_1 = input("6. Animal: ")
verb_2 = input("7. Verb: ")
color_1 = input("8. color: ")
verb_3 = input("9. Verb (ending in -ing): ")
adverb_1 = input("10. Adverb (ending in -ly): ")
number_1 = input("11. Number (more than one (1)): ")
measure_of_time_1 = input("12. Measure of Time (minutes, hours, ..., days): ")
color_2 = input("13. color: ")
animal_2 = input("14. Animal: ")
number_2 = input("15. Number: ")
silly_word_1 = input("16. Silly Word: ")
animal_3 = input("17. Animal: ")

print("\nThanks for filling the blanks. Let's look at the final story.\n")

# print(f"This weekend I am going camping with ________________. I packed my lantern, sleeping bag, and\n"
#       f"________________. I am so ________________ to ________________ in a tent. I am ________________ we\n"
#       f"might see a ________________, they are kind of dangerous. We are going to hike, fish, and ________________.\n"
#       f"I have heard that the ________________ lake is great for ________________. Then we will\n"
#       f"________________hike through the forest for ________________ ________________. If I see a\n"
#       f"________________ ________________ while hiking, I am going to bring it home as a pet! At night we will tell\n"
#       f"________________ _______________ stories and roast ________________ around the campfire!! ")

# print(f"This weekend I am going camping with {proper_noun_1.title()}. I packed my lantern, sleeping bag, and\n"
#       f"{noun_1.lower()}. I am so {adjective_1.lower()} to {verb_1.lower()} in a tent. I am {adjective_2.lower()} we\n"
#       f"might see a {animal_1.lower()}, they are kind of dangerous. We are going to hike, fish, and {verb_2.lower()}.\n"
#       f"I have heard that the {color_1.lower()} lake is great for {verb_3.lower()}. Then we will\n"
#       f"{adverb_1.lower()} hike through the forest for {number_1.lower()} {measure_of_time_1.lower()} . If I see a\n"
#       f"{color_2.lower()} {animal_2.lower()} while hiking, I am going to bring it home as a pet! At night we will tell\n"
#       f"{number_2.lower()} {silly_word_1.lower()} stories and roast {animal_3.lower()} around the campfire!! ")

print("This weekend, I am going camping with " + color.RED + proper_noun_1.title().rstrip() + color.END + ". I packed my lantern, sleeping bag, and\n"
      + color.RED + noun_1.lower().rstrip() + color.END + ". I am so " + color.RED + adjective_1.lower().rstrip() + color.END + " to " + color.RED + verb_1.lower().rstrip() + color.END + " in a tent. I am " + color.RED + adjective_2.lower().rstrip() + color.END + " we\n"
      "might see a " + color.RED + animal_1.lower().rstrip() + color.END + " , they are kind of dangerous. We are going to hike, fish, and " + color.RED + verb_2.lower().rstrip() + color.END + ".\n"
      "I have heard that the " + color.RED + color_1.lower().rstrip() + color.END + " lake is great for " + color.RED + verb_3.lower().rstrip() + color.END + ". Then we will\n"
      + color.RED + adverb_1.lower().rstrip() + color.END + " hike through the forest for " + color.RED + number_1.lower().rstrip() + color.END + " " + color.RED + measure_of_time_1.lower().rstrip() + color.END + ". If I see a\n"
      + color.RED + color_2.lower().rstrip() + color.END + " " + color.RED + animal_2.lower().rstrip() + color.END + " while hiking, I am going to bring it home as a pet! At night we will tell\n"
      + color.RED + number_2.lower().rstrip() + color.END + " " + color.RED + silly_word_1.lower().rstrip() + color.END + " stories and roast a " + color.RED + animal_3.lower().rstrip() + color.END + " around the campfire!! ")

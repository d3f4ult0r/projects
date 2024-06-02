adjective = input("Enter an adjective: ").lower()
noun = input("Enter a noun: ").lower()
place = input("Enter a place: ").lower()
verb = input("Enter a verb: ").lower()
emotion = input("Enter an emotion: ").lower()
sound = input("Enter a sound: ").lower()

d_verb = f"{verb}ing"
p_verb = f"{verb}ed"


madlib = f"Once upon a time in a {adjective} {place}, there lived a {adjective} {noun}. Every morning, the {noun} would {verb} to the {place} to start their day. One {adjective} day, while {d_verb}, they stumbled upon a {adjective} {noun} that was {d_verb} a {noun}. This surprised the {noun} so much that they let out a loud {sound}! Feeling {emotion}, the {noun} decided to {verb} the {noun} back to its {place}. On the way, they met a {adjective} {noun} who offered them a {noun} in exchange for a {adjective} favor. The {noun} agreed and {p_verb} the {noun}. Finally, they reached the {place}, where everyone was {d_verb} to celebrate their return. It was a {adjective} day in the {place}, and the {noun} realized that sometimes, the most {adjective} adventures happen when you least expect them."

print(madlib)
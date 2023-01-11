facts = [["vertebrate", "duck"], ["flying", "duck"], ["mammal", "cat"]]


def add_fact(fact):
    if not fact in facts:
        facts.append(fact)


# here cond stands for condidtion
for cond, item in facts:
    if cond == "mammal":
        add_fact(["vertebrate", item])
    if cond == "vertebrate":
        add_fact(["animal", item])
    if cond == "vertebrate" and ["flying", item] in facts:
        add_fact(["bird", item])

print(facts)

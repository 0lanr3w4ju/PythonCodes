import random

articles = ["the", "a", "one", "some", "any"]
noun = ["boy", "girl", "dog", "town", "car"]
verb = ["drove", "jumped", "ran", "walked", "skipped"]
preposition = ["to", "from", "over", "under", "on"]

x = 0
while True:

    articlesChosen = random.choice(articles)
    nounChosen = random.choice(noun)
    verbChosen = random.choice(verb)
    prepositionChosen = random.choice(preposition)
    articlesChosen1 = random.choice(articles)
    nounChosen1 = random.choice(noun)

    sentence = "{} {} {} {} {} {}.".format(
        articlesChosen, nounChosen, verbChosen, prepositionChosen, articlesChosen1, nounChosen1
    ).capitalize()

    print(sentence)

    x += 1
    if x == 20:
        break

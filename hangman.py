import random
stages = ['''
          +---+
          |   |
              |
              |
              |
              |
          =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
              =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
                  =========''', '''
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                      =========''', '''
                      
                        +---+
                        |   |
                        O   |
                       /|\  |
                            |
                            |
                            =========''', '''
                            +---+
                            |   |
                            O   |
                           /|\  |
                           /    |
                                |
                                =========''', '''
                                 +---+
                                |   |
                                O   |
                               /|\  |
                               / \  |
                                    |
                                =========


''']
print("Welcome to Hangman game!")
print("Words will be in romainian.")
print("Have fun!\n")


word_list_easy = ['camila', 'pirat', 'veverita', 'farfurie', 'calculator',
                  'telefon', 'masina', 'casa', 'papagal', 'pisica', 'caine',
                  'mancare', 'pantof', 'pantaloni', 'tricou', 'bluza', 'geanta',
                  'ochelari', 'ochi', 'nas', 'gura', 'ureche', 'mana', 'picior',
                  'cap', 'picioare', 'maini', 'brat', 'coapsa', 'genunchi', 'deget',
                  'mouse', 'tastatura', 'monitor', 'casti', 'boxe', 'fereasta',
                  'pizza', 'cascaval', 'telecomanda', 'televizor', 'laptop',
                  'carte', 'creion', 'pix', 'cana', 'sticla', 'apa', 'suc', 'vin',
                  'bere', 'soare']

word_list_medium = ['jargon', 'dragon', 'papusa', 'radiografie', 'calorifer',
                    'sinonim', 'antinim', 'antagonist', 'protagonist',
                    'omonim', 'ciclic', 'cicatrice', 'fososinteza']

word_list_hard = ['spectru', 'neologism', 'sintagma', 'metafora', 'epitete',
                  'falanga', 'fascicul', 'fascinatie', 'fascism',
                  'elocvent', 'hemocrom', 'romanizare', 'siliciu',
                  'anticonceptionale', 'memorandum', 'sindrom',
                  'homodiegetic', 'pneumatic', 'pneumonie']


def start():

    while True:
        dif = input("Please choose difficulty: easy, medium or hard: ")
        if dif == "easy":
            word = random.choice(word_list_easy)
            break
        elif dif == "medium":
            word = random.choice(word_list_medium)
            break
        elif dif == "hard":
            word = random.choice(word_list_hard)
            break
        else:
            print("Invalid input\n")
            continue
    return word


cuvant = start()
lungime = len(cuvant)
display = ['_'] * lungime
count = 0
final = 0
while count <= 6 and final == 0:
    result = ' '.join(display)
    print(stages[count])
    print("\n")
    print(result)
    while True:
        guess = input("Please insert guess: ")
        if len(guess) > 1:
            print("Please insert a letter!")
        else:
            break
    if guess.lower() in cuvant:
        lun = 0
        while lun < len(cuvant):
            if guess.lower() == cuvant[lun]:
                display[lun] = guess.lower()
            lun += 1
    else:
        count += 1
    verif = 0
    for item in display:
        if item != '_':
            verif += 1
    if verif == len(cuvant):
        final = 1
    continue

if final == 1:
    print("\n\nCongratulations! You won!")
else:
    print("\n\nThe word was {}".format(cuvant))
    print("Better luck next time!")

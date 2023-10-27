import random

def roll():
    value = random.randint(1, 6)
    print(f"Вы бросили кубик и выпало: {value}")
    if value in (5, 6):
        print("Вы победили!")
    elif value in (3, 4):
        print("Вы перебрасываете кубик...")
        roll()
    else:
        print("Вы проиграли.")

if __name__ == "__main__":
    print("Игра в кубик")
    roll()

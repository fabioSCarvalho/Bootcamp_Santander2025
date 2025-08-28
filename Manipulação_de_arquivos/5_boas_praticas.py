from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "ilrem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"erro ao abrir o arquivo {exc}")

'''try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipulandor arquivo utilizando python.")
except IOError as exc:
    print(f"errp ap anrir o arquivo {exc}")'''

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"errp ap anrir o arquivo {exc}")
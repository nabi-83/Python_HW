from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy", "+79521452555"),
    Smartphone("Iphone", "14Pro Max", "+79658524411"),
    Smartphone("Iphone", "12 Pro", "+79632225544"),
    Smartphone("Iphone", "17", "+79554158844"),
    Smartphone("Iphone", "X", "+79854561245")
]

for smartphone in catalog:
    print(f"<{smartphone.marka}> - <{smartphone.model}>. <{smartphone.number}>")
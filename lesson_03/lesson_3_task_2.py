from smartphone import Smartphone

catalog = [
    Smartphone("Sony","Z5","+7 921-358-65-45"),
    Smartphone("iPhone","6S","+7 921-147-47-74"),
    Smartphone("Samsung","Galaxy J5","+7 911-899-66-69"),
    Smartphone("Xiaomi","Redmi Note 10","+7 911-177-88-06"), 
    Smartphone("iPhone","69S","+7 921-550-00-55")   
]

for Smartphone in catalog:
    print(f"{Smartphone.marka} - {Smartphone.model} - {Smartphone.nomer}")

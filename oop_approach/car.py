class Vehicle:
    def __init__(self, brand, model, year, color) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    
    def __str__(self) -> str:
        return f"{self.brand}, {self.model}, {self.year}, {self.color}"
    
    def start(self):
        print(f"The car {self.brand} {self.model} start the engine")
    
    
    def drive(self):
        print(f"The car {self.brand} {self.model} is driving")
    
    
    def stop(self):
        print(f"The car {self.brand} {self.model} stopped")
    
    
    def honk(self):
        print('Beep Beep!')
        

car1 = Vehicle("Cadilac", "Impala", "1967", "black")
car2 = Vehicle("Cadilac", "Potter", "1967", "blue")
car3 = Vehicle("Cadilac", "Malfoy", "1967", "red")
car4 = Vehicle("Cadilac", "Snape", "1967", "green")

print(car1)
print(car2)
print(car3)
print(car4)

car1.honk()
car2.start()
car3.drive()
car4.stop()
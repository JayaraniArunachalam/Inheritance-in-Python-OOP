class Car:
    def __init__(self, brand, model, year, color,fuel):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel

    def display(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        print("Fuel Type:",self.fuel)
class ElectricCar(Car):
     def __init__(self,brand, model, year, color,fuel,battery_capacity):
         super().__init__(brand, model, year, color,fuel)
         self.battery = battery_capacity
     def displayev(self):
         print(self.brand,"",self.model,"is an electric car.")
         self.display()
         print("Battery capacity:",self.battery)

mycar = ElectricCar("MG","Windsor EV Essence Pro",2025,"Gold","Electricity","38 kWh")
mycar.displayev()
class Car:
    def __init__(self, car_id, make, model):
        self.car_id = car_id
        self.make = make
        self.model = model

# Example usage:

car1 = Car(1, "Toyota", "Camry")
car2 = Car(2, "Honda", "Accord")
car3 = Car(1, "Toyota", "Camry")

# Even if car1 and car2 have the same make and model, they are distinct entities because they have different identities (car_id).
print(car1 == car2)  # False
print(car1 == car3)  # False
print(car1.model==car3.model) # True

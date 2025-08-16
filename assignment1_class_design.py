# Assignment 1: Design Your Own Class! 🏗️
# Example: Smartphone with Inheritance

# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"

# Derived Class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
        self.battery = 100  # Default battery percentage
    
    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."
    
    def install_app(self, app_name):
        return f"Installing {app_name} on {self.brand} {self.model}."
    
    def use_battery(self, amount):
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0
        return f"Battery is now at {self.battery}%."
    
    def device_info(self):
        # Polymorphism: override parent method
        return f"{self.brand} {self.model} | OS: {self.os} | Storage: {self.storage}GB | Battery: {self.battery}%"


# Example Usage
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 15", "iOS", 256)
    phone2 = Smartphone("Samsung", "Galaxy S24", "Android", 512)
    
    print(phone1.device_info())
    print(phone1.make_call("123-456-7890"))
    print(phone1.use_battery(20))
    print(phone1.install_app("WhatsApp"))
    
    print("\n---\n")
    
    print(phone2.device_info())
    print(phone2.make_call("987-654-3210"))
    print(phone2.use_battery(35))
    print(phone2.install_app("Instagram"))

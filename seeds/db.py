from  flask_seeder import Seeder, Faker, generator

from  application.models import Employee,Service

class UserSeeder(Seeder):
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
        cls=Employee,
            init={
                "name": generator.Name()
            }
        )
        # Create 5 users
        for employee in faker.create(5):
            print("Adding Employee: %s" % employee)
            self.db.session.add(employee)

class  ServiceSeeder(Seeder):
    def run(self):
        # Create a new Faker and tell it how to create User objects
        services = [
            Service("Car Washing (One Car)","60"),
            Service("House Cleaning","120"),
            Service("Run Errand","45.20"),
            Service("Do maths Assigment","30.45")
        ]
        
        # Create 5 Services
        for service in services:
            print("Adding  services: %s" % service)
            self.db.session.add(service)



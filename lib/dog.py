#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = 'Mutt'):
        self.name = name
        self.breed = breed

    def show_self(self):
        return self
    
# Dog takes a name as an argument and saves it to self.name 
# Dog takes a breed as an argument and saves it to self.breed                                                                                 [ 50%]
# Dog sets self.breed = "Mutt" when no breed specified 

# fido = Dog('Fido')
# fido.breed
# snoopy = Dog('Snoopy', 'Husky')
# snoopy.breed

# fido.show_self()
# fido is fido.show_self()

from abc import ABC, abstractmethod

class Forma:
    def __init__(self,cor):
        self.cor = cor

    @abstractmethod
    def cacular_area(self):
        pass

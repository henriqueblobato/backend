'''
Created on 3 de abr de 2019

@author: ik
'''
class Animal():
    def __init__(self, name, typeA, rescue_date, porte, vaccinated, approximate_age):
        self.__name = name
        self.__type = typeA
        self.__rescue_date = rescue_date
        self.__adoption_date = None
        self.__porte = porte
        self.__vaccinated = vaccinated
        self.__approximate_age = approximate_age
    
    def set_adoption_date(self, adoption_date):
        self.__adoption_date = adoption_date
        
class Cliente():
    def __init__(self, name, last_name, RG, proof_of_address, email, phone):
        self.__name = name
        self.__last_name = last_name
        self.__RG = RG
        self.__proof_of_address = proof_of_address
        self.__email = email
        self.__phone = phone
        
        

# Принцып
#from ast import Pass


class User:
    def __init__(self, name:str):
        self.name = name



    def get_name(self) -> str:
        pass


    def save(self,user):
        pass


#Правильно  это  разделить класс на  классы


class Person:
    def  __init__(self, name: str):
        self.name = name
        
    def  get_name(str):
        pass


class UserDB:
    def get_user(self,id)  -> Person:
        pass


    def save(self,user:Person):
        pass
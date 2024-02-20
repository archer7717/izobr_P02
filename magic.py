class  Pencil:
    def __eq__(self,other):
        print('pencil eq')
        return self  is other 

class Egg:
    def __eq__(self, other):
        print('egg eq')
        return self  is other 
        


my_pencil = Pencil()
my_egg = Egg()

print(my_egg == my_pencil)

print(my_pencil == my_pencil)
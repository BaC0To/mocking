class Man():
    _sex = 'male'
    __has_balls = True
    arg3 = ''
    
    def __init__(self, age, name):
       self.age = age
       self._name = name

    @property
    def name(self):
      # print(dir(self))
       return self._name
    
    @name.setter
    def name(self, name):
       self._name = name


    @staticmethod
    def my_print():
       print('asd')

   
    
ivan = Man(22, 'Ivan')
Pesho = Man(33, 'Pesho')
Pesho.name
Pesho.name='Petran'
print(Pesho.name)
#print(dir(Pesho))
# clases

class Auto:
    
    def avanzar(self,metros): 
        print('Se avanzo ',metros,'metros')
    
    def tocar_bocina(self):
        print('RAKATAKATAKA BUUUM BUUUUM')
        
        
# instanciar un objeto
auto1 = Auto()
auto2 = Auto()

auto1.tocar_bocina()
auto1.avanzar(5)
auto2.avanzar(20)
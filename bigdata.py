from abc import ABC, abstractmethod


class BigDataHandler(ABC):
    dataMatrix = [list(i) for i in """                                                                                             

    DDDDDDDDDDDDD                  AAA         TTTTTTTTTTTTTTTTTTTTTTT         AAA               
    D::::::::::::DDD              A:::A        T:::::::::::::::::::::T        A:::A              
    D:::::::::::::::DD           A:::::A       T:::::::::::::::::::::T       A:::::A             
    DDD:::::DDDDD:::::D         A:::::::A      T:::::TT:::::::TT:::::T      A:::::::A            
      D:::::D    D:::::D       A:::::::::A     TTTTTT  T:::::T  TTTTTT     A:::::::::A           
      D:::::D     D:::::D     A:::::A:::::A            T:::::T            A:::::A:::::A          
      D:::::D     D:::::D    A:::::A A:::::A           T:::::T           A:::::A A:::::A         
      D:::::D     D:::::D   A:::::A   A:::::A          T:::::T          A:::::A   A:::::A        
      D:::::D     D:::::D  A:::::A     A:::::A         T:::::T         A:::::A     A:::::A       
      D:::::D     D:::::D A:::::AAAAAAAAA:::::A        T:::::T        A:::::AAAAAAAAA:::::A      
      D:::::D     D:::::DA:::::::::::::::::::::A       T:::::T       A:::::::::::::::::::::A     
      D:::::D    D:::::DA:::::AAAAAAAAAAAAA:::::A      T:::::T      A:::::AAAAAAAAAAAAA:::::A    
    DDD:::::DDDDD:::::DA:::::A             A:::::A   TT:::::::TT   A:::::A             A:::::A   
    D:::::::::::::::DDA:::::A               A:::::A  T:::::::::T  A:::::A               A:::::A  
    D::::::::::::DDD A:::::A                 A:::::A T:::::::::T A:::::A                 A:::::A 
    DDDDDDDDDDDDD   AAAAAAA                   AAAAAAATTTTTTTTTTTAAAAAAA                   AAAAAAA
                                                                                                 """.split("\n")]

    def __init__(self, *args, **kwargs):
        self.arguments = args

        for key, val in kwargs.items():
            self.__dict__[key] = val

    @abstractmethod
    def renderMatrix(self):
        pass

    @abstractmethod
    def displayData(self):
        pass


class BigDataHandlerV1(BigDataHandler):

    def renderMatrix(self):
        return "\n".join(["".join(line) for line in self.dataMatrix])

    def displayData(self):
        print(self.renderMatrix())


class bigDataHandlerFactory:
    def __init__(self, bigDataVersion):
        self.bigDataVersion = str(bigDataVersion)

    def generateDataHandler(self) -> BigDataHandler:
        return globals()["BigDataHandlerV" + self.bigDataVersion]()


if __name__ == "__main__":
    x = bigDataHandlerFactory(1)
    handler = x.generateDataHandler()
    handler.displayData()

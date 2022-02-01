class OperacionesAritmeticas:

    numero_temporal1 =-1
    numero_temporal2 =-1
    operacionAritmetica=None
    resultado=0

    @classmethod
    def resolverOperacionAritmetica(cls):
        if cls.operacionAritmetica ==  '+':
            cls.resultado = cls.numero_temporal1 + cls.numero_temporal2

        if cls.operacionAritmetica ==  '-':
            cls.resultado = cls.numero_temporal2 -cls.numero_temporal1

        if cls.operacionAritmetica ==  '*':
            cls.resultado = cls.numero_temporal1 * cls.numero_temporal2

        if cls.operacionAritmetica ==  '/':
            if cls.numero_temporal1 != 0:
                cls.resultado = int(cls.numero_temporal2 / cls.numero_temporal1  )
            else:
                print('No existe division para 0 :/')

        if  cls.operacionAritmetica != None:
            print(cls.resultado)

    @classmethod
    def zero(cls,valor= None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 0
        else:
            cls.numero_temporal2= 0

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def nine(cls,valor= None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 9
        else:
            cls.numero_temporal2= 9

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def eight(cls,valor= None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 8
        else:
            cls.numero_temporal2= 8

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def seven(cls,valor= None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 7
        else:
            cls.numero_temporal2= 7

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def six(cls,valor= None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 6
        else:
            cls.numero_temporal2= 6

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def five(cls,valor= None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 5
        else:
            cls.numero_temporal2= 5

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def four(cls,valor= None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 4
        else:
            cls.numero_temporal2= 4

        OperacionesAritmeticas.resolverOperacionAritmetica()
    @classmethod
    def three(cls, valor=None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 3
        else:
            cls.numero_temporal2 = 3

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def two(cls, valor=None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 2
        else:
            cls.numero_temporal2 = 2

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def one(cls, valor=None):
        if cls.numero_temporal1 == -1:
            cls.numero_temporal1 = 1
        else:
            cls.numero_temporal2 = 1

        OperacionesAritmeticas.resolverOperacionAritmetica()

    @classmethod
    def plus(cls, segundoNumero=None):
        cls.operacionAritmetica = '+'

    @classmethod
    def times(cls, segundoNumero=None):
        cls.operacionAritmetica = '*'

    @classmethod
    def minus(cls, segundoNumero=None):
        cls.operacionAritmetica = '-'

    @classmethod
    def divided_by(cls, segundoNumero=None):
        cls.operacionAritmetica = '/'

OperacionesAritmeticas.nine(OperacionesAritmeticas.divided_by(OperacionesAritmeticas.two()))
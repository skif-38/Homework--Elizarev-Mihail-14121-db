class Negator:
    @staticmethod
    def neg(obj):
        if isinstance(obj, (int, float)):
            return -obj
        elif isinstance(obj, bool):
            return not obj
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')


if __name__ == "__main__":
    print(Negator.neg(5))
    print(Negator.neg(-3)) 
    
    print(Negator.neg(2.5))   
    print(Negator.neg(-1.7))   
    
    try:
        Negator.neg("строка")
    except TypeError as e:
        print(e)
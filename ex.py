def fabrica_de_decoradores(param):
    print(param)
    def fabrica_de_funcoes(func):
        print('Decoradora', param)
        def interna(*args, **kwargs):
            print('Aninhada', param)
            return func(*args, **kwargs), param
        return interna
    return fabrica_de_funcoes


@fabrica_de_decoradores(1)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores(2)(lambda x, y: x * y)

resultado = soma(5, 5)
print(resultado)
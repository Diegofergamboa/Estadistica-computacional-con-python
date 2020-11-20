'''
    Herramienta usada para optimizar problemas, los cuales tiene una subestructura optima
    es decir que las solucones se pueden encontrar de manera optima aplicandolo a problemas locales
    El problema del morral, es encontrar una solucion optima dentro de problemas cada vez mas pequeños
    Problemas emplalmados es encontrar la solucion en varias ocasiones       
'''

# Memoization o memorizacion = La cual es una tecnica que evita computos adicionales guardando computos anteriores en diccionarios

# Numeros de Fibonacci bajo la formula "Fn = Fn-1 + Fn-2" 

# Ejemplo de programa

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


if __name__ == '__main__':
    n = int(input('Escoge un numero: ')) 
    resultado = fibonacci_recursivo(n)
    print(resultado)
    
    

# Vamos a mejorar este algoritmo por medio de fibonacci

def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1 :
        return 1
    
    try:
       return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
        memo[n] =   resultado
        
        return(resultado)
    
if __name__ == '__main__':
    n = int(input('Escoge un numero: ')) 
    resultado = fibonacci_dinamico(n)
    print(resultado)
    
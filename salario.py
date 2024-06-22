print('de qual empresa deseja ver as informações?')
print('''A)empresa1
B)empresa2
C)empresa3
D)empresa4
E)empresa5''')
escolha = input()

if escolha == 'a' or 'A':
    import statistics
    notas = [1000,6000,1200,8000,1400]
    print('empresa1')
    print("salarios", notas)
    print('media:',sum(notas) / len(notas))
    print('moda:',statistics.mode(notas))
    print('variancia:',statistics.variance(notas))
    print('desvio de padrão:',statistics.stdev(notas))
    print('menor salario:', min(notas))
    print('maior salario:',max(notas))
    
elif escolha == 'b' or 'B':
    import statistics
    notas = [5000,4000,3000,2000,7000]
    print('empresa2')
    print("salarios", notas)
    print('media:',sum(notas) / len(notas))
    print('moda:',statistics.mode(notas))
    print('variancia:',statistics.variance(notas))
    print('desvio de padrão:',statistics.stdev(notas))
    print('menor salario:', min(notas))
    print('maior salario:',max(notas))
    
elif escolha == 'c' or 'C':
    import statistics
    notas = [1200,1300,8000,3000,15000]
    print('empresa3')
    print("salarios", notas)
    print('media:',sum(notas) / len(notas))
    print('moda:',statistics.mode(notas))
    print('variancia:',statistics.variance(notas))
    print('desvio de padrão:',statistics.stdev(notas))
    print('menor salario:', min(notas))
    print('maior salario:',max(notas))
    
elif escolha == 'd' or 'D':
    import statistics
    notas = [1400,1750,2000,4500,5900,7000]
    print('empresa4')
    print("salarios", notas)
    print('media:',sum(notas) / len(notas))
    print('moda:',statistics.mode(notas))
    print('variancia:',statistics.variance(notas))
    print('desvio de padrão:',statistics.stdev(notas))
    print('menor salario:', min(notas))
    print('maior salario:',max(notas))
    
    
elif escolha == 'e' or 'E':
    import statistics
    notas = [1400,1750,2000,4500,5900,7000]
    print('empresa5')
    print("salarios", notas)
    print('media:',sum(notas) / len(notas))
    print('moda:',statistics.mode(notas))
    print('variancia:',statistics.variance(notas))
    print('desvio de padrão:',statistics.stdev(notas))
    print('menor salario:', min(notas))
    print('maior salario:',max(notas))

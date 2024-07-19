def remover_duplicatas(lista):
    # Usar um conjunto para armazenar dicionários convertidos em tuplas
    conjunto_de_dicionarios = set()
    lista_sem_duplicatas = []
    
    for dicionario in lista:
        # Converter o dicionário em uma tupla de pares chave-valor
        
        # Verificar se a tupla já está no conjunto
        if dicionario not in conjunto_de_dicionarios:
            # Adicionar a tupla ao conjunto e o dicionário original à lista sem duplicatas
            conjunto_de_dicionarios.add(dicionario)
            lista_sem_duplicatas.append(dicionario)
    
    return lista_sem_duplicatas
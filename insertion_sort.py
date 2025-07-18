def insertion_sort_passo_a_passo(arr):
    print(f"Array Original: {arr}\n")
    a = arr[:]
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        
        parte_ordenada = a[:i+1]
        parte_nao_ordenada = a[i+1:]
        print(f"Passo {i}: Inserindo '{key}' -> {parte_ordenada} | {parte_nao_ordenada}")
            
    print(f"\nResultado Final: {a}")

dados_insertion = ['R', 'A', 'N', 'Y', 'A', 'D', 'U', 'R', 'A', 'N']
insertion_sort_passo_a_passo(dados_insertion)
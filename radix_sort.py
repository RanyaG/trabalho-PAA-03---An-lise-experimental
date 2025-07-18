def radix_sort_passo_a_passo(arr):
    print(f"Array Original: {arr}\n")
    
    max_val = max(arr)
    exp = 1
    passada = 1
    
    while max_val // exp > 0:
        print(f"--- Passada {passada} (Ordenando pelo dígito das {exp}s) ---")
        _counting_sort_for_radix(arr, exp)
        print(f"Resultado da passada: {arr}\n")
        exp *= 10
        passada += 1
        
    print(f"Resultado Final: {arr}")

def _counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

dados_radix = [81824, 23579, 69983, 76653, 13105, 27567, 22828, 98316, 18695, 70751]
radix_sort_passo_a_passo(dados_radix)
def counting_sort_passo_a_passo(arr):
    print(f"Array Original: {arr}")
    
    max_val = max(arr)
    n = len(arr)
    
    count_arr = [0] * (max_val + 1)
    for num in arr:
        count_arr[num] += 1
    print(f"Array de Contagem (frequência): {count_arr}")
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    print(f"Array de Contagem Cumulativa:   {count_arr}")
    
    output_arr = [0] * n
    for i in range(n - 1, -1, -1):
        num = arr[i]
        pos = count_arr[num] - 1
        output_arr[pos] = num
        count_arr[num] -= 1
        
    print(f"\nResultado Final: {output_arr}")

dados_counting = [4, 1, 0, 2, 3, 2, 0, 5, 3, 5]
counting_sort_passo_a_passo(dados_counting)
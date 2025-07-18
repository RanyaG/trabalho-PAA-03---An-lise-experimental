def merge_sort_passo_a_passo(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        print(f"Dividindo: {arr} -> {L} e {R}")

        merge_sort_passo_a_passo(L)
        merge_sort_passo_a_passo(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
        print(f"Intercalando -> {arr}")
    return arr

dados_merge = [35, 82, 24, 74, 46, 29, 86, 83, 66, 81]
print(f"Array Original: {dados_merge}\n")
resultado = merge_sort_passo_a_passo(dados_merge)
print(f"\nResultado Final: {resultado}")
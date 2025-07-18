def quick_sort_passo_a_passo(arr, low, high, nivel=0):
    if low < high:
        pivot_val = arr[high]
        print(f"{'  '*nivel}Particionando: {arr[low:high+1]} (Pivô: {pivot_val})")
        
        pi = _partition(arr, low, high)
        print(f"{'  '*nivel}Após partição: {arr[low:high+1]} (Pivô '{pivot_val}' está no índice {pi})")

        quick_sort_passo_a_passo(arr, low, pi - 1, nivel + 1)
        quick_sort_passo_a_passo(arr, pi + 1, high, nivel + 1)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

dados_quick = [15, 25, 37, 86, 21, 30, 23, 57, 42, 41]
print(f"Array Original: {dados_quick}\n")
quick_sort_passo_a_passo(dados_quick, 0, len(dados_quick) - 1)
print(f"\nResultado Final: {dados_quick}")
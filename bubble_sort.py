def bubble_sort_passo_a_passo(arr):
    """Executa o Bubble Sort mostrando cada passada."""
    print(f"Array Original: {arr}\n")
    n = len(arr)
    a = arr[:]
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        
        print(f"Após Passada {i+1}: {a}")
        
        if not swapped:
            print("\nNenhuma troca realizada. A lista está ordenada.")
            break
            
    print(f"\nResultado Final: {a}")

dados_bubble = [-69, 63, 6, 65, 22, -80, -48, -72, 93, 18]
bubble_sort_passo_a_passo(dados_bubble)
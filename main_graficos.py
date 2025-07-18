
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import alg  

def main():
    print("Iniciando analise experimental dos algoritmos...")

    algoritmos_para_testar = {
        "Bubble Sort": alg.bubble_sort,
        "Insertion Sort": alg.insertion_sort,
        "Merge Sort": alg.merge_sort,
        "Quick Sort": alg.quick_sort,
        "Heap Sort": alg.heap_sort,
        "Counting Sort": alg.counting_sort,
        "Radix Sort": alg.radix_sort,
    }


    base_array = [-69, 63, 6, 65, 22, -80, -48, -72, 93, 18]


    tamanhos = list(range(10, 201, 10))


    resultados = []
    print("Coletando dados de tempo de processamento...")

    for nome_algoritmo, funcao_algoritmo in algoritmos_para_testar.items():
        print(f"  -> Testando: {nome_algoritmo}...")
        for n in tamanhos:
            for tipo_dado in ['Original', 'Crescente', 'Decrescente']:
                arr_expandido = (base_array * (n // len(base_array) + 1))[:n]
                if tipo_dado == 'Crescente':
                    dados = sorted(arr_expandido)
                elif tipo_dado == 'Decrescente':
                    dados = sorted(arr_expandido, reverse=True)
                else:
                    dados = arr_expandido

                tempo_inicio = time.perf_counter()
                funcao_algoritmo(dados)
                tempo_fim = time.perf_counter()

                resultados.append({
                    "Algoritmo": nome_algoritmo,
                    "Tamanho (n)": n,
                    "Tipo de Entrada": tipo_dado,
                    "Tempo (s)": tempo_fim - tempo_inicio,
                })


    print("Gerando graficos com Seaborn...")

    df_resultados = pd.DataFrame(resultados)

    sns.set_theme(style="whitegrid")

    g = sns.relplot(
        data=df_resultados,
        x="Tamanho (n)",
        y="Tempo (s)",
        hue="Algoritmo",    
        style="Algoritmo",   
        col="Tipo de Entrada",
        kind="line",         
        facet_kws={"sharey": False, "sharex": True}, 
        marker='o',           
        legend="full"
    )

    g.fig.suptitle("Analise de Desempenho de Algoritmos de Ordenacao", y=1.03, fontsize=16)
    g.set_titles("Entrada: {col_name}", fontsize=12)
    g.set_axis_labels("Tamanho da Entrada (n)", "Tempo de Execucao (s)")

    nome_arquivo_grafico = "desempenho_algoritmos.png"
    plt.savefig(nome_arquivo_grafico, dpi=300, bbox_inches='tight')

    print(f"\nAnalise concluida! Graficos salvos em '{nome_arquivo_grafico}'.")

if __name__ == "__main__":
    main()
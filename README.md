
### **1. Sobre o Projeto**

O objetivo deste trabalho é duplo:

1.  **Compreensão Conceitual:** Entender o funcionamento interno de cada algoritmo através de simulações passo a passo.
2.  **Análise Empírica:** Comparar o desempenho prático dos algoritmos medindo seus tempos de execução em diferentes cenários e com volumes de dados crescentes.

Os algoritmos analisados foram:

  * Bubble Sort
  * Insertion Sort
  * Merge Sort
  * Quick Sort
  * Heap Sort
  * Counting Sort
  * Radix Sort

-----

### **2. Estrutura do Repositório**

  * `alg.py`: Módulo principal que contém as implementações limpas de todos os sete algoritmos de ordenação.
  * `main_graficos.py`: Script principal que executa a análise experimental, mede os tempos e gera os gráficos de desempenho comparativos.
  * `desempenho_algoritmos.jpg`: Imagem com os gráficos gerados pela análise, mostrando a performance dos algoritmos em três cenários.
  * `bubble_sort.py`, `insertion_sort.py`, etc.: Scripts individuais para demonstrar a execução passo a passo de cada algoritmo com os dados específicos da atividade.
  * `README.md`: Este arquivo.

-----

### **3. Como Executar a Análise**

Para replicar a análise experimental e gerar os gráficos, siga os passos abaixo.

#### **Pré-requisitos**

  * Python 3.8 ou superior

#### **Instalação de Dependências**

Clone o repositório e instale as bibliotecas necessárias usando o pip:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install pandas seaborn matplotlib
```

#### **Execução**

Execute o script principal a partir do seu terminal:


Ao final da execução, o arquivo `desempenho_algoritmos.png` será gerado (ou atualizado) na raiz do projeto.


### **4. Resultados e Análise**

A análise experimental gerou os seguintes resultados, comparando o tempo de execução (em segundos) pelo tamanho da entrada (`n`).

#### **Conclusões Principais:**

  * **Entrada Original (Caso Médio):** Os algoritmos de complexidade `O(n log n)` (Merge, Quick, Heap) e os lineares (Counting, Radix) são drasticamente mais eficientes que os de complexidade `O(n²)` (Bubble, Insertion).
  * **Entrada Crescente (Melhor/Pior Caso):** Este cenário evidencia o melhor caso `O(n)` do **Insertion Sort**, que se torna um dos mais rápidos. Em contrapartida, expõe o pior caso `O(n²)` do **Quick Sort**, que tem seu desempenho severamente degradado.
  * **Entrada Decrescente (Pior Caso):** Confirma o pior cenário para **Bubble Sort**, **Insertion Sort** e também para o **Quick Sort**, enquanto os demais algoritmos (Merge, Heap, Counting, Radix) mantêm sua performance robusta.


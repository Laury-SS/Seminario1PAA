# Teoria dos Grafos: Problema do Carteiro Chinês  

Este repositório contém os materiais do seminário de **Projeto e Análise de Algoritmos** sobre o *Problema do Carteiro Chinês (Chinese Postman Problem – CPP)*.  

## 🎥 Apresentação  
O vídeo da apresentação do seminário está disponível no YouTube:  
👉 [Assistir no YouTube](https://youtu.be/6fLUU3uK5qM)  

## 📑 Conteúdo do Repositório  
- **Slides**: [`ProblemadoCarteiroChinês_Lauryane.pdf`](ProblemadoCarteiroChinês_Lauryane.pdf)  
- **Código-fonte**: implementação do Problema do Carteiro Chinês em **Python**.  
- **Dados**: arquivo `graph3.input` contendo a instância do problema utilizada no estudo de caso.  
- **Imagens**: representação visual do grafo usado no exemplo e da solução final.

## 📌 Descrição do Problema  
O Problema do Carteiro Chinês consiste em encontrar o **menor percurso fechado** que percorra todas as arestas de um grafo pelo menos uma vez.  

- Se o grafo for **euleriano**, a solução é o próprio circuito euleriano.  
- Se o grafo não for euleriano, é necessário duplicar arestas de forma ótima para que todos os vértices tenham grau par, e então construir o circuito euleriano.  

## 🧮 Implementação  
A implementação foi feita em **Python**, utilizando o algoritmo de **Dijkstra** para calcular as distâncias mínimas entre os vértices de grau ímpar.  
Em seguida, foi aplicado o **emparelhamento mínimo perfeito** para definir quais arestas deveriam ser duplicadas.  

A solução final retorna:  
- Sequência dos vértices percorridos no circuito.  
- Custo base do grafo original.  
- Custo adicional das duplicações.  
- Custo total da rota final.  

## 📂 Dados de Entrada  
Arquivo: `graph3.input`  

## 📊 Resultado Obtido  
- **Vértices ímpares**: a, b, d, e  
- **Emparelhamento escolhido**: (a, e), (b, d)  
- **Custo base**: 72
- **Custo adicional**: 21  
- **Custo total**: 93

## 🖼️ Visualização  
### Grafo usado no estudo de caso  
![Grafo original](images/grafo_inicial.png)  

### Solução final com a rota  
![Solução final](images/grafo_solucao.png)  

# Reconhecedor de Palavras Utilizando o algoritmo CYK
# Sobre
- Matéria: Linguagens Formais e Autômatos
- Trabalho Prático 2
- Linguagem: Python


## Alunos:
- Kledyson Henrique Goes Dos Santos

## Descrição do Projeto:
O trabalho prático consiste na implementação de um reconhecedor de palavras utilizando o algoritmo CYK. Cada aluno deve pesquisar sobre o algoritmo e apresentar uma implementação do mesmo.

A implementação deve partir de uma gramática colocada em um arquivo de texto. O programa deve ler esse arquivo de texto e carregar a gramática correspondente. Considere que a gramática já vai ser escrita na forma normal de Chomsky, requisito necessário para o algoritmo CYK.

## Exemplo de Formato de Leitura do Arquivo:
A gramática no arquivo de texto deve seguir a seguinte notação:
> S => XB | AB  
X => AS  
A => a  
B => b  

## Como Executar:
1. Edite o arquivo "gramatica.txt" localizado dentro da pasta "arquivos" com a gramática desejada.
    - Importante lembrar que o conteúdo do arquivo deve seguir a notação informada anteriormente.
2. Execute o arquivo "main.py", localizado na raiz desse projeto.
3. Escolha a opção número 1 para informar uma palavra.
4. Informe a palavra desejada.    
> Pronto, o programa irá informar se ela é aceita, além de também imprimir a tabela feita para verificar a aceitação.
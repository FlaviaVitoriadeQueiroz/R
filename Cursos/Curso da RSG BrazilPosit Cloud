link: https://posit.cloud/content/9432691

Aplicativo/site Posit Cloud
 Os pacotes necessários podem ser baixados no icone amarelo no início do projeto
 Os pacotes não ficam sempre ativos, então é necessário ativa-los com Ctrl + Entrer

Operações Básicas com R:
 x = 5
 x
 y = 7
 y
 z = y + x
 z
 multi = x * y
 multi

Os comandos de operaçãos númericas são os mesmos do Python:
a == b #Igual?
a != b #Diferente?
x < y # Menor?
x > y # Maior?
x <= 5 # Menor ou igual?

O.B.S.: Para colocar texto como uma string basta colocar entre "".
 Já para digitar textos que não são string colocasse # antes, como no Python

Vetores:
 São estruturas que armazenam conjuntos de dados iguais de forma sequencial
 Vetores não podem armazenar textos e números, ou os números seram convertidos em textos

Função:
 Funções no R se dão por um caracterio+(), exemplo F()
 Para saber o que uma função faz é necessário colocar um ponto de interrogação antes do caracterio, exemplo ?F()

Dataframes e tibbles:
 São tabelas com linhas e colunas de diferentes classes como número, caracteres e fatores
 As tabelas tibbles se diferenciam em sua apresentação e falicidade de se trabalahr com tabelas grandes e largas
 O.B.S.: É melhor cria-las no excel, mas da para fazer no R usando a função data.frame( nome da coluna = vetor("linhas),; ou usando a
função tibble, que ficaria, tibble= tibble(~nome da coluna, ~nome da coluna, ~nome da coluna
                                           "nome da linha", valor            valor
 Para transformar variavel em dataframe usa-se: as.data.frame()

Tipos de Visualizações:
Com print()
print(data) #No documento ou console
print(tibble)
Com nome do objeto
data
tibble 
Com glimpse(). #Descrição mais completa da tabela
glimpse(data) 
glimpse(tibble)
Com view() ou View(). A tabela completa com mais funcionalidades (filtragem manual, pesquisa e ordenamento) abrirá em uma nova janela
view(data) 
view(tibble)

Para conseguir estatísticas gerais:
Como summary
summary(tibble)
summary(data)
Usando skim
skim(tibble)
skim(data)

Pivotar= transformar uma tabela grande/larga em uma tabela pequena
data_long = pivot_longer(data, #Tabela 
             cols = c(variavel1, variavel2), #Colunas para alongar 
             values_to = "valor", #Estocar valores em uma nova coluna
             names_to = "variavel" #Estocar variáveis em uma nova coluna
             ) 
data
data_long
ou podemos deixar elas melhores para visualização:
data_wide = pivot_wider(data_long, #Tabela
            names_from = variavel, #Dividir níveis de uma coluna em novas colunas
            values_from = valor)   #Estocar valores relacionados à coluna nome 
                                   #e novas variáveis) 
data_wide

45:06 aula 2

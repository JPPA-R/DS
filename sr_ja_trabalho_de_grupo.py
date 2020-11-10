# -*- coding: utf-8 -*-
"""SR_JA_trabalho_de_grupo (Parte I - Python).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bztTR1_ieUgI-h6wVfD8lX5J-igNig22

# PGDS Rumos - Programação em Python 
### Trabalho prático de grupo (Parte I)

Data limite de entrega: 24 de Fevereiro de 2020 às 23:59

---

O trabalho consiste em 7 exercícios de programação, **dos quais têm de resolver 6**, onde terão a oportunidade de aplicar os conceitos de Python aprendidos nas primeiras 3 aulas.

# **Trabalho Realizado por Sofia Ribeiro e João Ascensão**

## Exercício 1

Escreva uma função `get_words` que devolva o _conjunto_ de palavras que ocorrem numa string em Língua Portuguesa, em minúsculas. Não se esqueça de retirar a pontuação!

**Exemplo:**

Para `s = "Atirei o pau ao gato, mas o gato não morreu; Dona Chica assustou-se com o berro que o gato deu.`

temos que
`get_words(s) == {'atirei', 'o', 'pau', 'ao', 'gato', 'mas', 'não', 'morreu',
'dona', 'chica', 'assustou-se', 'com', 'berro', 'que', 'deu'}`
"""

def get_words(s):

  #Verifica a existência de pontuação concatenando uma string com os caracteres que não se encontrem nessa lista, 
  #ao retornar o valor converte-se para set de modo a obtermos o resultado pretendido

  pontuacao = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
  resultado = ""

  for c in s:
    if c not in pontuacao:
        resultado = resultado + c
        
  return set( resultado.split() )

# testes:

get_words('Atirei o pau ao gato, mas o gato não morreu; Dona Chica assustou-se com o berro que o gato deu.')

"""## Exercício 2

Escreva uma função `has_repeated` que, dada uma string `s`, devolva `True` se `s` contiver caracteres repetidos e `False` caso contrário.
"""

def f(s):

  #Fazemos a verificação do tamanho da string com o tamanho da string convertida em set onde vai colocar apenas os valores únicos.
  
  if len( set(s) ) == len(s):
    return False
  else:
    return True
    
# testes: esta célula não deve dar erros AssertionError!

assert f('abc') == False
assert f('aba') == True
assert f('  a') == True
assert f('carlos') == False
assert f('Aa') == False

"""## Exercício 3

Escreva uma função `barchart` que, dada uma lista ou tuplo de inteiros, produza (`print`) um ``gráfico de barras`` com os valores da lista ou tuplo como ilustrado abaixo:

**Nota:** Não é necessário validar que se tratam efectivamente de inteiros.

**Exemplo:**
A lista ``l = [3, 4, 20, 15, 3, 4]`` deve produzir `f(l)`

```
|***| 3
|****| 4
|********************| 20
|***************| 15
|***| 3
|****| 4
```
"""

def bar_chart(l):

  #Fazemos a validação se a lista ou tuplo são inteiros imprimindo até o tipo que está a ser tratado

  if all( isinstance(x, int) for x in l ):
     temp=''

     if type(l) is tuple:
       print ('Tuple')
     else:
       print ('List')

     for p in l:
       print ('|' + '*'*p + '| ' + str(p) + '\n')

  else:
    print('Só aceita inteiros')

# testes:

li=[3, 4, 20, 15, 3, 4]
bar_chart(li)

"""## Exercício 4

Escreva uma função `median` em Python puro (sem recurso a bibliotecas importadas via `import`!) que encontre a mediana de uma lista de números `float`.

**Nota:** Para efeitos deste exercício, considere que a lista tem um número ímpar de elementos!
"""

def median(l):

  #Validamos se a lista é uma lista de floats, após isso obtemos o tamanho da lista e ordenamos a mesma 
  #analisamos a lista se a mesma for par o valor da mediana vai ser a soma dos valores centrais a dividir a dividir por 2,
  # caso seja impar vai ser o valor central que se encontra na lista

  if all( isinstance(x, float) for x in l ):
    n = len(l) 
    l.sort() 

    if n % 2 == 0: 
        median = (l[n//2] + l[n//2 - 1] )/2
    else: 
        median = l[n//2] 

    print("O Valor da mediana é: " + str(median))

  else:
    print('Só aceita listas do tipo float') 

# testes:

me=[25.0 ,4.7 ,5.1, 7.1 ,9.9]
median(me)

"""## Exercício 5

Escreva uma função `mode` em Python puro (sem recurso a bibliotecas importadas via `import`, excepto possivelmente a biblioteca `collections`!) que encontre a moda estatística de uma lista de números `int`.
"""

import collections
def mode(l):

  #Validamos se a lista é de inteiros, usamos a função counter para contar o número de vezes que cada elemento se encontra na lista,
  #convertemos para dicionário e no dicionário vamos comparar cada elemento com o maior valor do contador , o elemento que corresponder é a moda, 
  #caso todos os valores sejam unicos não temos moda

  if all( isinstance(x, int) for x in l ):

    contador = collections.Counter(l) 
    dictcont = dict(contador) 
    moda = [number for number, value in dictcont.items() if value == max(list(contador.values())) ] 

    if len(moda) == len(l): 
        print('Não existe moda')
    else: 
        print( "O valor da moda é " + ', '.join( map(str, moda) ) ) 
        
  else:
    print ('Só aceita listas de inteiros')

# testes:

mo=[1,2,3,4,5,5]
mode(mo)

"""## Exercício 6

Escreva uma função `is_email` que retorne `True` se uma string for um endereço de e-mail e `False` caso contrário.

**Nota:** Para efeitos deste exercício, considere que um endereço de e-mail:

- contém exactamente uma `arroba` (@);
- contém apenas letras minúsculas antes da arroba;
- contém apenas um ponto, e este está a seguir à arroba;
- contém apenas letras minúsculas antes do ponto, e apenas letras a seguir ao ponto.
- não contém caracteres além de letras minúsculas, pontos e arrobas.

**Exemplos:**

- `is_email("luismbpsousa@gmail.com")` deve retornar `True`,
 mas
- `is_email("joao.Ratao33 at carochinha.pt")` deve retornar `False`

**Complemento:** 
Não é necessário escrever manualmente uma lista com todos os caracteres do alfabeto. Pode usar a seguinte lista:

`letras_minusculas = [chr(x) for x in range(ord('a'), ord('z') + 1)]`
"""

def is_email(s):

  #valida presença de @ tem que ser exatamente 1

  if s.count('@')!=1:
    return False

  #verifica posição ponto e apenas pode conter 1

  if s.count('.')>1 and s.index('.')<s.index('@'):
   return False
  
  #verifica minusculas retirando o '@' e o '.' da string dado já terem sido validados anteriormente, usei a lista minusculas para retirar ã por exemplo
  letras_minusculas = [chr(x) for x in range(ord('a'), ord('z') + 1)]
  nminusculas=all(list(map(lambda x:x.islower() and x in letras_minusculas,s.replace('@','').replace('.',''))))

  return nminusculas

assert is_email('joão@gmail.com') == False
assert is_email('luismbpsousa@gmail.com') == True
assert is_email('joao.Ratao33 at carochinha.pt') == False

"""# Exercício 7

Verifique a [Lei de Benford](https://pt.wikipedia.org/wiki/Lei_de_Benford) para a população residente em cidades em Portugal.

Em detalhe: usando o dicionário `data` abaixo, contendo as populações residentes nas cidades portuguesesas, verifique se a distribuição do primeiro dígito dessas populações segue aproximadamente ou não a Lei de Benford (cuja distribuição se encontra já calculada em `benford_freqs`). 
Comece por transformar cada população no seu primeiro dígito, depois extraia a sua distribuição de frequências absolutas, e por fim as relativas.

**Não é necessário realizar testes estatísticos (como o Kolmogorov-Smirnov), apenas uma comparação informal.**

**Nota:** Deve retirar da sua análise os valores iguais a zero.
"""

# Se este link falhar, podem obter um novo para o mesmo dataset em https://dados.gov.pt/pt/datasets/populacao-residente-em-cidades-n-o/ 
# Em Dataset json url, clicar em Copiar permalink para a área de transferência e colá-lo em baixo 👇🏽

url = "https://dados.gov.pt/pt/datasets/r/1b8ee646-144d-4532-985d-3d62a058653e"

import json
import requests
import math
from collections import Counter

benford_freqs = {d: math.log10(1 + 1/d) for d in range(1, 10)}

r = json.loads(requests.get(url).text)
data = {x['geodsg']: int(x['valor']) for x in r[0]['Dados']['2013'] if len(x['geocod']) == 7}

#Cria dicionário com numeração númerica 1 a 9
dictfr={
  "1":{"fa" : 0,
       "fr" :0
       },
  "2": {"fa" : 0,
       "fr" :0
       },
  "3":{"fa" : 0,
       "fr" :0
       },
  "4": {"fa" : 0,
       "fr" :0
       },
  "5": {"fa" : 0,
       "fr" :0
       },
  "6": {"fa" : 0,
       "fr" :0
       },
  "7": {"fa" : 0,
       "fr" :0
       },
  "8": {"fa" : 0,
       "fr" :0
       },
  "9": {"fa" : 0,
       "fr" :0
       },
}

#Filtra os dados do dicionário retirando os 0.

newdata = dict(filter(lambda x: x[1] > 0, data.items()))

#Vamos obter o valor total de registos válidos

totalamostra=len(newdata.keys())
for cidade,valor in newdata.items():

  #Obtemos o primeiro digito do número de populações
  firstnumber=str(valor)[:1]
  
  #obtemos o valor que se encontra no dicionário incrementando para cada número encontrado.
  valuefa=dictfr[firstnumber]['fa']
  valuefa+=1
  dictfr[firstnumber]['fa']=valuefa
  dictfr[firstnumber]['fr']=valuefa/totalamostra

#verificamos a diferença entre eles
dictdif={}
for x in benford_freqs.items():
  tempfa=dictfr[str(x[0])]['fr']
  dictdif[str(x[0])]=x[1]-tempfa

dictdif

"""# Divirtam-se! :)

Luís Miguel Sousa
"""
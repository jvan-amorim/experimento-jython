# Experimento com Jython: Python integrado à JVM

Este projeto explora a interoperabilidade entre Python e Java usando o **Jython**. Os dois scripts são escritos em Python, mas usam diretamente classes do Java, sem nenhuma camada intermediária.

[Vídeo Apresentação (YouTube)](https://youtu.be/0wbGUFZCqDI)

## Sobre o Jython

O Jython é uma implementação da linguagem Python escrita em Java. Ele compila o código Python para bytecode Java e executa tudo sobre a **Máquina Virtual Java (JVM)**. Por isso, um programa em Jython pode importar e usar qualquer classe da biblioteca padrão do Java ou de outros arquivos `.jar`, como se fossem módulos Python.

Essa característica permite que Python e Java compartilhem a mesma plataforma de execução, objetos e bibliotecas.

## Programas desenvolvidos

### `exemplo1.py`: manipulação de arquivos com `java.io`

Cria a pasta `saida/`, grava um arquivo de tarefas, acrescenta uma linha no modo *append*, lê o conteúdo de volta linha a linha, exibe metadados do arquivo, lista o conteúdo da pasta e remove o arquivo ao final.

### `exemplo2.py`: contagem de palavras com `java.util`

Lê um texto com `Scanner`, conta a frequência das palavras em um `HashMap`, ignora palavras comuns guardadas em um `HashSet`, exibe as palavras em ordem alfabética com `TreeMap` e produz um ranking com `ArrayList` ordenado por `Collections.sort`. Também usa um `Iterator` para filtrar palavras que aparecem uma única vez.

## Classes e bibliotecas Java utilizadas

| Pacote | Classes |
|---|---|
| `java.io` | `File`, `FileWriter`, `BufferedWriter`, `FileReader`, `BufferedReader` |
| `java.util` | `Scanner`, `HashMap`, `HashSet`, `ArrayList`, `TreeMap`, `Collections`, `Comparator`, `Iterator` (via `iterator()`) |

## Como Python e Java são integrados

1. Importação direta. Linhas como `from java.io import File` carregam a classe Java diretamente da JVM. O Jython resolve esses nomes automaticamente.

2. Chamada de métodos Java com sintaxe Python. Por exemplo, `arquivo.getAbsolutePath()` e `contagem.put(palavra, valor)` são métodos Java chamados normalmente a partir do código Python.

3. Conversão automática de tipos. Strings Python são convertidas para `java.lang.String`, e inteiros são convertidos para `Integer` quando necessário. Valores que voltam do Java, como `Integer`, são usados como números Python. Por isso, `int(...)` aparece em alguns pontos para deixar a intenção explícita.

4. Iteração sobre coleções Java. O `for` do Python funciona diretamente sobre `keySet()` e outras coleções do Java.

5. Implementação de interfaces Java em Python. No `exemplo2.py`, a classe `PorFrequencia` herda de `java.util.Comparator` e implementa o método `compare`. O `Collections.sort` do Java chama esse método, que é código Python. É a integração nos dois sentidos: Java chamando Python.

## Setup

### Como executar com Docker

É preciso ter o Docker instalado e, na pasta do projeto, executar:

```bash
docker build -t atividade-jython .
docker run --rm atividade-jython
```

O primeiro comando constrói a imagem: ele baixa uma imagem base com Java 17 e o Jython 2.7.3, e copia os scripts. O segundo executa `exemplo1.py` e, em seguida, `exemplo2.py`.

## Estrutura do repositório

```
atividade-jython/
├── README.md        # (Você está aqui!)
├── Dockerfile       # Imagem com Java e Jython para executar os exemplos
├── exemplo1.py      # Manipulação de arquivos com java.io
├── exemplo2.py      # Contagem de palavras com java.util
└── .gitignore       # Ignora arquivos gerados na execução
```

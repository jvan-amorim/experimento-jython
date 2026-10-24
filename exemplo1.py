# -*- coding: utf-8 -*-
# Exemplo 1: manipulacao de arquivos usando classes do pacote java.io
from __future__ import print_function

# Em Jython, classes Java sao importadas como se fossem modulos Python.
from java.io import File, FileWriter, BufferedWriter, FileReader, BufferedReader

PASTA_SAIDA = "saida"
NOME_ARQUIVO = "tarefas.txt"

# Cria a pasta, se nao existir, usando java.io.File.
def preparar_pasta(nome):
    pasta = File(nome)
    if not pasta.exists():
        pasta.mkdirs()
    return pasta

# Escreve linhas com BufferedWriter sobre FileWriter (classes Java).
def escrever_linhas(caminho, linhas, anexar=False):
    writer = BufferedWriter(FileWriter(caminho, anexar))
    try:
        for linha in linhas:
            writer.write(linha)
            writer.newLine()
    finally:
        writer.close()

# Le todas as linhas com BufferedReader sobre FileReader (classes Java).
def ler_linhas(caminho):
    reader = BufferedReader(FileReader(caminho))
    linhas = []
    try:
        linha = reader.readLine()  # retorna None ao chegar ao fim do arquivo
        while linha is not None:
            linhas.append(linha)
            linha = reader.readLine()
    finally:
        reader.close()
    return linhas


if __name__ == "__main__":
    print('\n** Exemplo1 **')
    pasta = preparar_pasta(PASTA_SAIDA)
    arquivo = File(pasta, NOME_ARQUIVO)

    print("1) Criando arquivo:", arquivo.getAbsolutePath())
    escrever_linhas(arquivo.getPath(),
                    ["Configurar Docker", "Instalar Jython", "Ler a documentacao do java.io"])

    print("2) Acrescentando uma linha (modo append)")
    escrever_linhas(arquivo.getPath(), ["Revisar o README"], anexar=True)

    print("3) Conteudo lido:")
    for i, linha in enumerate(ler_linhas(arquivo.getPath()), 1):
        print("   %d: %s" % (i, linha))

    print("4) Metadados via java.io.File:")
    print("   tamanho em bytes:", arquivo.length())
    print("   e um arquivo?", arquivo.isFile())

    print("5) Conteudo de", pasta.getName() + ":")
    for f in pasta.listFiles():
        print("   -", f.getName())

    print("6) Arquivo removido:", arquivo.delete())

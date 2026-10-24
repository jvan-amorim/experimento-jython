# -*- coding: utf-8 -*-
# Exemplo 2: contagem de palavras usando estruturas de dados do pacote java.util
from __future__ import print_function

from java.util import Scanner, HashMap, HashSet, ArrayList, TreeMap, Collections, Comparator

TEXTO = """
Jython permite escrever programas em Python que usam classes Java.
Com Jython, Python e Java compartilham a mesma JVM.
Colecoes Java organizam dados, e o Python tambem organiza dados com listas e dicionarios.
Na JVM, Python e Java executam juntos e trocam objetos de forma direta.
"""

STOPWORDS = ["a", "o", "e", "de", "da", "do", "em", "que", "com", "um",
             "uma", "se", "na", "no", "as", "os", "mas", "para", "pela", "pelo"]

# Comparator do java.util implementado em Python: ordem decrescente de contagem
class PorFrequencia(Comparator):
    def __init__(self, contagem):
        self.contagem = contagem

    def compare(self, a, b):
        return int(self.contagem.get(b)) - int(self.contagem.get(a))

# Conta as palavras usando HashSet (stopwords) e HashMap (contagem) do java.util
def contar_palavras(texto):
    stop = HashSet()
    for p in STOPWORDS:
        stop.add(p)

    contagem = HashMap()
    scanner = Scanner(texto)  # java.util.Scanner quebra o texto em tokens
    scanner.useDelimiter("[^A-Za-z]+")
    try:
        while scanner.hasNext():
            palavra = unicode(scanner.next()).lower()
            if palavra and not stop.contains(palavra):
                atual = contagem.get(palavra)
                contagem.put(palavra, 1 if atual is None else atual + 1)
    finally:
        scanner.close()
    return contagem

if __name__ == "__main__":
    print('\n** Exemplo2 **')

    contagem = contar_palavras(TEXTO)
    print("Palavras distintas:", contagem.size())

    # TreeMap: mantem as chaves ordenadas alfabeticamente
    print("\nPrimeiras palavras em ordem alfabetica:")
    ordenado = TreeMap(contagem)
    for i, chave in enumerate(ordenado.keySet()):
        if i >= 8:
            break
        print("  %-12s %d" % (chave, int(ordenado.get(chave))))

    # ArrayList + Collections.sort com um Comparator Java escrito em Python
    chaves = ArrayList(contagem.keySet())
    Collections.sort(chaves, PorFrequencia(contagem))
    print("\nTop 5 por frequencia:")
    for i in range(min(5, chaves.size())):
        palavra = chaves.get(i)
        print("  %d. %s (%d)" % (i + 1, palavra, int(contagem.get(palavra))))

    # Iterator explicito do java.util para filtrar palavras que aparecem uma vez
    print("\nPalavras que aparecem uma unica vez:")
    it = chaves.iterator()
    unicas = []
    while it.hasNext():
        p = unicode(it.next())
        if int(contagem.get(p)) == 1:
            unicas.append(p)
    print("  " + ", ".join(sorted(unicas)))

    # Soma total das ocorrencias
    total = 0
    for chave in contagem.keySet():
        total += int(contagem.get(chave))
    print("\nTotal de palavras contadas:", total)

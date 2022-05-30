import difflib

def word_check(s, palavras):
    for palavra in s.casefold().split():
        if palavra not in palavras:
            sugestao = difflib.get_close_matches(palavra, palavras)
            sugestao = ', '.join(str(x) for x in sugestao)

            return "" if sugestao == "" else sugestao
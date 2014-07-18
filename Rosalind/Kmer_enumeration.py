__author__ = 'ravi'
import itertools


def lex_perm(symbols,n):
    products = itertools.product(symbols,repeat = n)
    for product in products:
        combo = ""
        for p in product:
            combo = combo + p
        print combo
    return

if __name__ == "__main__":
    symbol_fh = open("rosalind_lexf.txt",'rU')
    symbols = symbol_fh.readline().strip().replace(" ","")
    n = int(symbol_fh.readline().strip())
    lex_perm(symbols,n)

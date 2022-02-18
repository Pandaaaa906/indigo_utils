from collections import Counter
from typing import Callable

from indigo import Indigo, IndigoObject

_indigo = Indigo()


def symbol_wrapper(symbol, isotope):
    if symbol == 'H' and isotope == 2:
        return 'D'
    elif symbol == 'H' and isotope == 3:
        return 'T'
    elif isotope:
        return f'[{isotope}{symbol}]'
    else:
        return symbol


def hill_ordering(symbol: str):
    if symbol == 'C':
        return '0'
    if symbol == 'H':
        return '1'
    return symbol.lower()


def formula_from_obj(m: IndigoObject, symbol_ordering: Callable = None):
    symbol_ordering = hill_ordering if symbol_ordering is None else symbol_ordering
    m.unfoldHydrogens()
    d = {}
    for atom in m.iterateAtoms():
        key = (atom.symbol(), atom.isotope())
        d[key] = d.get(key, 0) + 1
    atoms = sorted(d.items(), key=lambda x: (symbol_ordering(x[0][0]), x[0][1]))
    return ''.join((f'{symbol_wrapper(symbol, isotope)}{num if num > 1 else ""}' for (symbol, isotope), num in atoms))


def sep_formula_from_smiles(smiles, sep=' ', ordering=-1):
    ss = smiles.split('.')
    mc = Counter(ss)
    ms = sorted(((_indigo.loadMolecule(s), c) for s, c in mc.items()), key=lambda m: ordering * m[0].molecularWeight())
    return sep.join((f'{f"{c}*" if c > 1 else ""}{formula_from_obj(m)}' for m, c in ms))


def sep_formula_from_obj(m: IndigoObject, sep=' ', ordering=-1):
    smiles, *_ = m.canonicalSmiles().split(' ')
    return sep_formula_from_smiles(smiles, sep=sep, ordering=ordering)

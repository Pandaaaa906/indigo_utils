from indigo import Indigo, IndigoObject

_indigo = Indigo()

SYMBOL_ORDERING = {
    'C': '0',
    'H': '2',
    'Cl': '3',
    'N': '4',
    'O': '5',
    'P': '6',
    'S': '7',
}


def symbol_wrapper(symbol, isotope):
    if symbol == 'H' and isotope == 2:
        return 'D'
    elif symbol == 'H' and isotope == 3:
        return 'T'
    elif isotope:
        return f'[{isotope}{symbol}]'
    else:
        return symbol


def formula_from_obj(m: IndigoObject, symbol_ordering=None):
    symbol_ordering = SYMBOL_ORDERING if symbol_ordering is None else symbol_ordering
    m.unfoldHydrogens()
    d = {}
    for atom in m.iterateAtoms():
        key = (atom.symbol(), atom.isotope())
        d[key] = d.get(key, 0) + 1
    atoms = sorted(d.items(), key=lambda x: (symbol_ordering.get(x[0][0], x[0][0]), x[0][1]))
    return ''.join((f'{symbol_wrapper(symbol, isotope)}{num if num > 1 else ""}' for (symbol, isotope), num in atoms))


def sep_formula_from_obj(m: IndigoObject, sep=' ', ordering=-1):
    smiles, *_ = m.canonicalSmiles().split(' ')
    ss = smiles.split('.')
    ms = sorted((_indigo.loadMolecule(s) for s in ss), key=lambda tmp: ordering*tmp.molecularWeight())
    return sep.join((formula_from_obj(m) for m in ms))


def sep_formula_from_smiles(smiles, sep=' ', ordering=-1):
    ss = smiles.split('.')
    ms = sorted((_indigo.loadMolecule(s) for s in ss), key=lambda m: ordering*m.molecularWeight())
    return sep.join((formula_from_obj(m) for m in ms))

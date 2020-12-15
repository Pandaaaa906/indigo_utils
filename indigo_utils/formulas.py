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
    if symbol == 'H' and isotope:
        return 'D'
    elif isotope:
        return f'[{isotope}{symbol}]'
    else:
        return symbol


def get_mf_from_obj(m: IndigoObject, symbol_ordering=None):
    symbol_ordering = SYMBOL_ORDERING if symbol_ordering is None else symbol_ordering
    m.unfoldHydrogens()
    d = {}
    for atom in m.iterateAtoms():
        key = (atom.symbol(), atom.isotope())
        d[key] = d.get(key, 0) + 1
    atoms = sorted(d.items(), key=lambda x: (symbol_ordering.get(x[0][0], x[0][0]), x[0][1]))
    return ''.join((f'{symbol_wrapper(symbol, isotope)}{num if num > 1 else ""}' for (symbol, isotope), num in atoms))


def get_sep_mf_from_smiles(smiles, sep=' '):
    ss = smiles.split('.')
    return sep.join((get_mf_from_obj(_indigo.loadMolecule(s)) for s in ss))


if __name__ == '__main__':
    smiles = 'O=C(N)/[13C]([H])=C([2H])\[15NH]S(OP(O[Na])(O)=O)(=O)=O.Cl'
    m = _indigo.loadMolecule(smiles)
    print(get_mf_from_obj(m))
    print(get_sep_mf_from_smiles(smiles))
    pass

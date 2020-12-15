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




if __name__ == '__main__':
    smiles = 'O=C(N)/[13C]([H])=C([2H])\[15NH]S(OP(O[Na])(O)=O)(=O)=O.Cl'
    m = _indigo.loadMolecule(smiles)

    pass

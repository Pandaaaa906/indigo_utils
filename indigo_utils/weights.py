from typing import Union

from indigo import Indigo, IndigoObject

_indigo = Indigo()


def weight_with_sep(obj: Union[IndigoObject, str], sep=' ', n=2, ordering=-1):
    if isinstance(obj, str):
        m = _indigo.loadMolecule(obj)
    elif isinstance(obj, IndigoObject):
        m = obj
    else:
        raise TypeError(f'Wrong type received: {type(obj)}')
    smiles, = m.canonicalSmiles().split(' ')
    ss = smiles.split('.')
    ms = sorted((_indigo.loadMolecule(s) for s in ss), key=lambda m: ordering*m.molecularWeight())
    tmp = f'{{:.{n}f}}'
    return sep.join((tmp.format(m.molecularWeight()) for m in ms))

from collections import Counter
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
    smiles, *_ = m.canonicalSmiles().split(' ')
    ss = smiles.split('.')
    mc = Counter(ss)
    ms = sorted(((_indigo.loadMolecule(s).molecularWeight(), c) for s, c in mc.items()), key=lambda x: ordering*x[0])
    tmp = f'{{:.{n}f}}'
    return sep.join((f'{f"{c}*" if c > 1 else ""}{tmp.format(mw)}' for mw, c in ms))

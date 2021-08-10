import unittest

from indigo import Indigo

from indigo_utils import sep_formula_from_smiles, formula_from_obj, sep_formula_from_obj

_indigo = Indigo()


class TestFormulaMethods(unittest.TestCase):
    def test_sep_formula_from_smiles(self):
        smiles = r'O=C(N)/[13C]([H])=C([2H])\[15NH]S(OP(O[Na])(O)=O)(=O)=O.Cl'
        m = _indigo.loadMolecule(smiles)
        self.assertEqual(
            sep_formula_from_smiles(smiles),
            'C2[13C]H5DN[15N]NaO7PS HCl'
        )

    def test_formula_from_obj(self):
        smiles = r'O=C(N)/[13C]([H])=C([2H])\[15NH]S(OP(O[Na])(O)=O)(=O)=O.Cl'
        m = _indigo.loadMolecule(smiles)
        self.assertEqual(
            formula_from_obj(m),
            'C2[13C]H6DClN[15N]NaO7PS'
        )

    def test_sep_formula_from_obj(self):
        smiles = r'O=C([O-])C1=CC=CC=C1.[Na+]'
        m = _indigo.loadMolecule(smiles)
        self.assertEqual(
            sep_formula_from_obj(m),
            'C7H5O2 Na'
        )


if __name__ == '__main__':
    unittest.main()

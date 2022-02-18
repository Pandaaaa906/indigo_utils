import unittest

from indigo import Indigo

from indigo_utils import sep_formula_from_smiles, formula_from_obj, sep_formula_from_obj, weight_with_sep

_indigo = Indigo()


class TestFormulaMethods(unittest.TestCase):
    def test_sep_formula_from_smiles(self):
        smiles = r'O=C(N)/[13C]([H])=C([2H])\[15NH]S(OP(O[Na])(O)=O)(=O)=O.Cl'
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
        smiles = 'O.O.[Na+].[Na+].[O-]C(=O)CN(CC([O-])=O)CCN(CC(O)=O)CC(O)=O'
        m = _indigo.loadMolecule(smiles)
        self.assertEqual(
            sep_formula_from_obj(m),
            'C10H14N2O8 2*Na 2*H2O'
        )

    def test_weight_with_sep(self):
        smiles = 'O.O.[Na+].[Na+].[O-]C(=O)CN(CC([O-])=O)CCN(CC(O)=O)CC(O)=O'
        self.assertEqual(
            weight_with_sep(smiles),
            '290.23 2*22.99 2*18.02'
        )


if __name__ == '__main__':
    unittest.main()

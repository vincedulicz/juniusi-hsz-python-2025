from orai_feladat.ListDictCompExercise import ListDictComp
from orai_feladat.NumpyExercise import NumpyFeladatok
from orai_feladat.PandasExercise import PandasFeladatok

def main():
    NumpyFeladatok.matrix_manipulacio()
    NumpyFeladatok.vektor_muveletek()
    NumpyFeladatok.adathalmaz_statisztika()
    NumpyFeladatok.maszkolas()
    NumpyFeladatok.matrix_szorzasa()
    NumpyFeladatok.felteteles_modositas()
    NumpyFeladatok.sinus_koszinus_gorbe()
    NumpyFeladatok.sor_oszlop_atlag()

    PandasFeladatok.dataframe_letrehozasa()
    PandasFeladatok.csv_beolvasas()
    PandasFeladatok.csoportositas()
    PandasFeladatok.hianyzo_kezeles()
    PandasFeladatok.idosor_elemzes()
    PandasFeladatok.felteteles_szures()
    PandasFeladatok.adatok_modositasa()
    PandasFeladatok.adatok_rendezese()

    ListDictComp.square_numbers()
    ListDictComp.even_numbers()
    ListDictComp.filter_non_divisible_by_3()
    ListDictComp.dict_square()
    ListDictComp.filter_dict()

main()

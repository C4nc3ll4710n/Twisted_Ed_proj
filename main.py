import parser as pars
import Projective_Coords as Proj_coords
import Twisted_Ed as T_E



def main():  
    params = pars.parse_curve_parameters('A1_sequence.txt')
    print(params)
    


if __name__ == "__main__":  # Стандартный способ запуска main()
    main()
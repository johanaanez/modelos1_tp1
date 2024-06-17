import time
import args
from laundry.laundry_factory import LaundryFactory
from laundry.laundry_manager import LaundryManager


def main():
    # obtención de argumentos
    start_time = time.time()
    arguments = args.parse_arguments()
    input_file = "laundry/tercer_problema.txt"
    output_file = "tercer_problema.txt"
    #input_file = arguments.inputfile
    #output_file = arguments.outputfile

    # cargar datos de los lavados
    laundry = LaundryFactory.Load(input_file)

    # calcular cantidad de lavados
    manager = LaundryManager(laundry)
    washes = manager.apply_ordered()

    # escribir en el archivo de salida
    LaundryFactory.output(washes, output_file)
    print("Execution time %s seconds" % (time.time() - start_time))
    
if __name__ == '__main__':
    main()

import time
import args
from laundry.laundry_factory import LaundryFactory

def main():
    # obtención de argumentos
    start_time = time.time()
    arguments = args.parse_arguments()
    input_file = "laundry/primer_problema.txt"
    output_file = "primer_problema.txt"
    #input_file = arguments.inputfile
    #output_file = arguments.outputfile

    # cargar datos de los lavados
    laundry = LaundryFactory.Load(input_file)

    print("Execution time %s seconds" % (time.time() - start_time))
    
if __name__ == '__main__':
    main()

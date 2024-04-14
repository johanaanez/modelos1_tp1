import argparse

def parse_arguments():
    usage_options = "%(prog)s [-v] [-if] [-of] "

    parser = argparse.ArgumentParser(
        usage=usage_options,
        description="<command description>"
    )

    parser.add_argument("-if", "--inputfile")
    parser.add_argument("-of", "--outputfile")

    return parser.parse_args()

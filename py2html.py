import sys


def main():

    """
    This program reformats the Python source code file specified
    as a command line argument as HTML and saves it to a new file
    with the original name with ".html" appended.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| Py2HTML       |")
    print("-----------------\n")

    if len(sys.argv) != 2:
        printf("input file must be specified")
    else:
        generate_html(sys.argv[1])


def generate_html(inputfile):

    """
    Central function performing substitution and file saving.
    """

    outputfile = inputfile + ".html"
    print("Input file:  " + inputfile)
    print("Output file: " + outputfile)

    # The mappings list contains a character or string to substitute
    # for each character indexed using its ASCII code
    mappings = [" "] * 128
    populate_mappings(mappings)

    try:

        fin = open(inputfile, "r")
        fout = open(outputfile, "w+")

        while True:
            c = fin.read(1)
            if not c:
                break
            fout.write(mappings[ord(c)])

        fin.close()
        fout.close()

        print("Output file generated")

    except IOError as ioe:

        print(str(ioe))


def populate_mappings(mappings):

    """
    Creates and returns the list of input to output character substitutions.
    """

    # initialize to default values
    for i in range(0, 128):
        mappings[i] = chr(i)

    # overwrite values we want to replace

    # tab
    mappings[9] = "&nbsp;&nbsp;&nbsp;&nbsp;"

    # linefeed
    mappings[10] = "</br>\n"

    # carriage return
    mappings[13] = ""

    # space
    mappings[32] = "&nbsp;"

    # <
    mappings[60] = "&lt;"

    # >
    mappings[62] = "&gt;"


main()

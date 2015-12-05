import sys
import os
from PyPDF2 import PdfFileReader, PdfFileMerger


# pdf merger function
def pyMerger(directory):
    pdfFiles = [f for f in os.listdir(directory) if f.endswith("pdf")]
    merger = PdfFileMerger()

    if pdfFiles != []:  # check if directory has pdf files in it
        for filename in pdfFiles:
            if filename != "_mergedFull.pdf":  # check if merged file already exists and skip it
                merger.append(PdfFileReader(os.path.join(directory, filename), "rb"))

        outputFile = os.path.join(directory, "_mergedFull.pdf")
        merger.write(outputFile)  # it will overwrite if final file existed
    else:
        print(directory + " has no pdf files in it.")


def main(topDir):
    # get top directory pdf files merged first
    print("Working in directory:\n" + topDir)
    pyMerger(topDir)


    # loop through directory tree and merge pdf files
    for root, dirs, files in os.walk(topDir, topdown=True):
        for name in dirs:
            print("Working in directory:\n" + os.path.join(root, name))
            pyMerger(os.path.join(root, name))


if __name__ == "__main__":
    main(str(sys.argv[1]))


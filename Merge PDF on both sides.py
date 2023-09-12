import PyPDF2
from reverse import reverse_pdf


### require PyPDF < 3.0 

def merge_pdf(frontPDF, backPDF, combinedName):
    """
    Combine the pdf that is the scanned only on the front and pdf that is scanned only on the back side,
    both coming from the same document.

    :type front: str
    :param front: name of the front side pdf
    :type back; str
    :param back: name of the back side pdf
    :return: None
    """
    front = open(frontPDF, 'rb')
    back = open(backPDF, 'rb')

    frontReader = PyPDF2.PdfFileReader(front)
    backReader = PyPDF2.PdfFileReader(back)

    mergedWriter = PyPDF2.PdfFileWriter()

    # both equal number of pages
    for pageNum in range(frontReader.numPages):
        frontObj = frontReader.getPage(pageNum)
        backObj = backReader.getPage(pageNum)
        mergedWriter.addPage(frontObj)
        mergedWriter.addPage(backObj)

    # write to output
    pdfOutput = open(combinedName, 'wb')
    mergedWriter.write(pdfOutput)

    # close all files
    pdfOutput.close()
    front.close()
    back.close()
    return




if __name__ == "__main__":
    frontPDF = "Front.pdf"
    backPDF = "Back.pdf"
    back_reversed = "Back Reverse.pdf"
    combinedName = 'Result.pdf'

    reverse_pdf(back_reversed)
    merge_pdf(frontPDF, backPDF, combinedName)
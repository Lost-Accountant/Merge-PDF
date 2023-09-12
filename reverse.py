import PyPDF2

def reverse_pdf(back_reversed_pdf):
    """

    :type back_reversed: str
    :param back_reversed:
    :return:
    """
    back_reversed = open(back_reversed_pdf, 'rb')

    reversedReader = PyPDF2.PdfFileReader(back_reversed)

    writer = PyPDF2.PdfFileWriter()

    # write from end to beginning
    for pageNum in range(reversedReader.numPages):
        obj = reversedReader.getPage(reversedReader.numPages - pageNum - 1)
        writer.addPage(obj)

    # write to output
    pdfOutput = open("Back.pdf", 'wb')
    writer.write(pdfOutput)

    # close all file
    pdfOutput.close()
    back_reversed.close()
    return

if __name__ == "__main__":
    back_reversed = "Back Reverse.pdf"

    reverse_pdf(back_reversed)
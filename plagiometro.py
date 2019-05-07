import PyPDF2


def pdf_to_list(filename):
    pdfFileObject = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    count = pdfReader.numPages
    phrases = []
    for i in range(count):
        page = pdfReader.getPage(i)
        phrases.append(page.extractText().replace('\n', ' ').lower())
    words = []
    for phrase in phrases:
        words += phrase.split()
    return words

def compare_lists(list_one, list_two):
    iquals = [i for i, j in zip(list_one, list_two) if i == j]
    iquals = len(iquals)
    result_one = iquals/len(list_one) * 100
    result_two = iquals/len(list_two) * 100
    return result_one, result_two


if __name__ == '__main__':
    # file_one = pdf_to_list('pdf1.pdf')
    # file_two = pdf_to_list('pdf2.pdf')
    file_one = "Text one".split()
    file_two = "text two.".split()
    result_one, result_two = compare_lists(file_one, file_two)
    print(round((result_one+result_two)/2))

from urllib import request
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def read_pdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    rests = StringIO()
    la_params = LAParams()
    device = TextConverter(rsrcmgr, rests, laparams=la_params)

    process_pdf(rsrcmgr, device, pdf_file)
    device.close()

    content = rests.getvalue()
    rests.close()
    return content


pdf_file = request.urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
out_put_string = read_pdf(pdf_file)
print(out_put_string)
pdf_file.close()

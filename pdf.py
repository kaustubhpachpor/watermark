#!/bin/py
'''
About Script: This asks for PDFs for merging (inputs). The last one will be of the watermark file. In order just to merge the PDF pages, skip from line 18 till end of the file. 
Also remove line 4 and 7. These are used for watermarking the files.'super.pdf' will be the ultimate merged PDF file. 'watermarked_output.pdf' will be final watermarked that file.
Please be my guest and change it as per your needs.
'''

import PyPDF2
import sys

inputs = sys.argv[1:-1]
wtrmark = sys.argv[-1]

def pdf_converter(pdf_list):
		merger = PyPDF2.ReadFileMerger()
		for pdf in pdf_list:
				print(pdf)
				merger.append(pdf)
		merger.write('super.pdf')

pdf_converter(inputs)

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open(wtrmark, 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  	page = template.getPage(i)
  	page.mergePage(watermark.getPage(0))
  	output.addPage(page)
  	
		with open('watermarked_output.pdf', 'wb') as file:
    		output.write(file)

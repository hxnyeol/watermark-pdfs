import PyPDF2
import os

wat_direc = './watermark/'
water_file = os.listdir(wat_direc)[0]  # takes only 1 file

inp_direc = './input_pdf/'
pdf_file = os.listdir(inp_direc)

out_direc = './output_pdf/'


def addWaterMark():
    '''No args Adds a watermark from watermark folder to each file given'''
    for i in range(len(pdf_file)):
        with open(f"{inp_direc}{pdf_file[i]}", "rb") as input_file:
            pdf_input = PyPDF2.PdfFileReader(input_file)
            file_name = os.path.splitext(pdf_file[i])[0]  # store filename

            with open(f"{wat_direc}{water_file}", "rb") as water_mark:
                water = PyPDF2.PdfFileReader(water_mark)
                watermark_page = water.getPage(0)
                output = PyPDF2.PdfFileWriter()

                for i in range(pdf_input.getNumPages()):
                    page = pdf_input.getPage(i)
                    page.mergePage(watermark_page)  # merge watermark with page
                    output.addPage(page)

                with open(f"{out_direc}{file_name}-converted.pdf", "wb") as result:

                    output.write(result)


# Main!!
addWaterMark()

from pdfmerge import pdfmerge
def merged_pdfs(pdf_list,Merged_filename):
    pdfmerge(pdf_list,Merged_filename)
pdf_list=['acknowledgementSlip.pdf','RTO LINCENSE.PDF']
Merged_filename="merged.pdf"

merged_pdfs(pdf_list,Merged_filename)
print('Congratulations the pdf is merged to :"{Merged_filename}"')
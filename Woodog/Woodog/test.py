# path_wkthmltopdf = 'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

# pdfkit.from_string(html_string, output_file, configuration=config)



import pdfkit
ret = generate_pdf('<html></html>')
with open('output.pdf', 'wb') as w:
    w.write(ret)


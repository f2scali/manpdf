#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def Dividir(archivo):
    pdf = PdfFileReader(archivo)
    nuevoarch=archivo[:-4]

    for pag in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(pag))
        archsalida = '{}_pag_{}.pdf'.format(nuevoarch, pag+1)
        with open(archsalida, 'wb') as out:
            pdf_writer.write(out)

    print('Pags. Procesadas: {}'.format(pdf.getNumPages()))


def Unir(archivos, salida):
    try:

        resultado=open(salida,'wb')
        pdf_writer = PdfFileWriter()
        for archivo in archivos:
            entrada_pdf=open(archivo, 'rb')
            pdfReader = PdfFileReader(entrada_pdf)
            for pageNum in range(pdfReader.numPages):
                pdf_writer.addPage(pdfReader.getPage(pageNum))
            pdf_writer.write(resultado)
            entrada_pdf.close()
        resultado.close()

    except Exception as e:
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Procesador de PDF')
    parser.add_argument('-d','--dividir', dest='dividir', default=None,    help='Accion Dividir archivo')
    parser.add_argument('-p','--password', dest='password', default='12345',    help='Nombre pdf Salida')
    parser.add_argument('-s','--salida', dest='salida', default='salida.pdf',    help='Nombre pdf Salida')
    parser.add_argument('-u','--unir', nargs='*', dest='unir', default=[], help='Lista de archivos a Unir')
    args = parser.parse_args()

    if args.dividir:
        print (f'Dividiendo en paginas:{args.dividir}')
        if not os.path.isfile(args.dividir):
            raise TypeError('No existe el archivo a modificar !!!')
        Dividir(args.dividir)

    elif args.unir:
        print ('Unir archivos:')
        for archivo in args.unir:
            if not os.path.isfile(archivo):
                raise TypeError('No existe el archivo a unir !!!')
        Unir(args.unir, args.salida)
    else:
        print(  'No se a definido la accion!!')

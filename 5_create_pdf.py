import yaml
import numpy as np
import matplotlib.pyplot as plt
from skimage import io 
import fitz
from PyPDF2 import PdfFileWriter
import argparse
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument('--save_csv_path', type=str, default='/nfs/masi/gaor2/tmp/justtest/prep',
                    help='the root for save result data')

parser.add_argument('--save_txt_path', type=str, default='/nfs/masi/gaor2/tmp/justtest/prep',
                    help='the root for save result data')

parser.add_argument('--save_prep_path', type=str, default='/nfs/masi/gaor2/tmp/justtest/prep',
                    help='the root for save result data')

parser.add_argument('--save_pdf_path', type=str, default='/nfs/masi/gaor2/tmp/justtest/prep',
                    help='the root for save result data')

args = parser.parse_args()

df = pd.read_csv(args.save_csv_path)

f = open(args.save_txt_path, 'w')

pdf_writer = PdfFileWriter()
pdf_writer.addBlankPage(width=220, height=300)
from pathlib import Path
with Path("./blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

for i, item in df.iterrows():
    tmp_id = item['exam_id']
    prob = item['pred']
    f.write(tmp_id + ' predicted as: ' + str(prob > 0.2) + ' cancer \n')
    
    img = np.load(args.save_prep_path + '/' + tmp_id + '_clean.npy')
    io.imsave('./temp_img.png', img[0][int(img.shape[1] / 2)])
    
    image_rectangle = fitz.Rect(0,0,200,200)

    # retrieve the first page of the PDF
    file_handle = fitz.open('./blank.pdf')
    first_page = file_handle[0]
    pix = fitz.Pixmap('./temp_img.png') 
    # add the image
    first_page.insertImage(image_rectangle, pixmap=pix)
    
    text = "predicted cancer likelihood: {:.4f}".format(prob)

    where = fitz.Point(10, 220)    # text starts here
    # this inserts 2 lines of text using font `DejaVu Sans Mono`
    first_page.insertText(where, text,
    #                 fontname=fname,    # arbitrary if fontfile given
    #                 fontfile=ffile,    # any file containing a font
                    fontsize=10,       # default
                    rotate=0,          # rotate text
                    color=(0, 0, 1),   # some color (blue)
                    overlay=True)      # text in foreground

    file_handle.save(args.save_pdf_path + '/' + tmp_id + '.pdf')
    
f.close()

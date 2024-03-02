#!/bin/sh
# pandoc -s cv_en_john_doe.md -o cv_en_john_doe.docx
python md_to_tex.py cv.md english
pdflatex cv.tex

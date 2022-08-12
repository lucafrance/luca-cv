pandoc -s cv_en_Luca_Franceschini.md -o cv_en_Luca_Franceschini.docx
python md_to_tex.py cv_en_Luca_Franceschini.md
pdflatex cv_en_Luca_Franceschini.tex

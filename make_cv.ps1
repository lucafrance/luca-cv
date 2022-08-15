pandoc -s cv_en_Luca_Franceschini.md -o cv_en_Luca_Franceschini.docx
pandoc -s cv_de_Luca_Franceschini.md -o cv_de_Luca_Franceschini.docx
python md_to_tex.py cv_en_Luca_Franceschini.md english
python md_to_tex.py cv_de_Luca_Franceschini.md german
pdflatex cv_en_Luca_Franceschini.tex
pdflatex cv_de_Luca_Franceschini.tex

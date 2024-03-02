# Luca-CV

Use

- Replace `photo.jpg` with your photo.
- Update `cv_en_john_doe.md`.
- Run `make_cv.ps1` to generate `cv_en_john_doe.docx`,`cv_en_john_doe.tex`, `cv_en_john_doe.pdf`.

Requirements

- [Python](https://www.python.org/)
- [Pandoc](https://pandoc.org/)
- pdflatex (included in [MiKTeX](https://miktex.org))

Acknowledgment
[Template photo](https://unsplash.com/photos/dLij9K4ObYY) by [Joe Shields](https://unsplash.com/@fortyozsteak)

# Changes from original repo

## Fri Feb 23 10:28:44 PM EST 2024

- split dates using `_` rather than `*` (for some reason my editor changes those)
- split CV entry titles based on `--` pattern and pass it to `\cventry` with correct number of arguments
- add config variable to the top to reproduce original design
- add link to gitlab
- would like 'cvtag'

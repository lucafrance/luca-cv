import os.path
import sys


class CurriculumVitae():

    def __init__(self, markdown_src):
        pass

    def to_tex(self):
        return ""


if __name__ == "__main__":
    src_filename = sys.argv[1]
    cv = CurriculumVitae(open(src_filename, "rt").read())
    open(os.path.splitext(src_filename)[0] + ".tex", "wt").write(cv.to_tex())

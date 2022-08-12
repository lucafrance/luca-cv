import os.path
import sys

def personal_info_from_md_line(txt):
    """Return personal info for lines with links
    
    e.g.
    input: "`email`    [lucaf@lucaf.eu](mailto:lucaf@lucaf.eu)"
    output: "lucaf@lucaf.eu"
    """

    txt = txt.split("[")[1]
    txt = txt.split("]")[0]
    return txt


class CurriculumVitae():

    def __init__(self):
        self.name = ("John", "Doe")
        self.title = None

    def from_markdown(self, markdown_src):
        lines = markdown_src.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("# "):
                line = line.removeprefix("# ")
                self.name = line.split(" ", 1)
                i += 1
                # The first non-empty line after the name is the title
                while lines[i] == "":
                    i += 1
                self.title = lines[i]
                i += 1
                continue
            
            if line.startswith("`email`"):
                self.email = personal_info_from_md_line(line)
                i += 1
                continue
            if line.startswith("`homepage`"):
                self.homepage = personal_info_from_md_line(line)
                i += 1
                continue
            if line.startswith("`linkedin`"):
                self.linkedin = personal_info_from_md_line(line)
                i += 1
                continue
            if line.startswith("`github`"):
                self.github = personal_info_from_md_line(line)
                i += 1
                continue

            i += 1

    def personal_data_md(self):
        tex_out = []
        tex_out.append("\\name {{{}}}{{{}}}".format(self.name[0], self.name[1]))
        if self.title is not None:
            tex_out.append("\\title{{{}}}".format(self.title))
        if self.email is not None:
             tex_out.append("\\email{{{}}}".format(self.email))
        if self.homepage is not None:
             tex_out.append("\\homepage{{{}}}".format(self.homepage))
        if self.linkedin is not None:
             tex_out.append("\\social[linkedin]{{{}}}".format(self.linkedin))
        if self.github is not None:
             tex_out.append("\\social[github]{{{}}}".format(self.github))
        
        tex_out = "\n".join(tex_out)
        return tex_out
        

    def to_tex(self):
        content = ""
        tex_template = open("cv_template.tex", "rt").read()
        tex_template = tex_template.replace("$personal_data", self.personal_data_md())
        tex_template = tex_template.replace("$content", content)
        return tex_template


if __name__ == "__main__":
    src_filename = sys.argv[1]
    cv = CurriculumVitae()
    cv.from_markdown(open(src_filename, "rt").read())
    open(os.path.splitext(src_filename)[0] + ".tex", "wt").write(cv.to_tex())

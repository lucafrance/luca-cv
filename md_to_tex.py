import os.path
import sys

DATE_SEP = "_"
SPLIT_TITLE = True


def personal_info_from_md_line(txt):
    """Return personal info for lines with links

    e.g.
    input:  "`email`    [abc@example.com](mailto:abc@example.com)"
    output: "abc@example.com"
    """

    txt = txt.split("[")[1]
    txt = txt.split("]")[0]
    return txt


def split_cv_line(txt):
    """Return a tuple of the side bar text and title

    e.g.
    input:  "*Gen 2000 -- Dec 2020* Example GmbH -- Intern"
    output: ("Gen 2000 -- Dec 2020", "Example GmbH -- Intern")
    """

    content = []
    if DATE_SEP not in txt:
        return "", txt

    txt = txt.split(DATE_SEP, 1)[1]
    txt = txt.split(DATE_SEP)
    content.append(txt[0].strip())
    title = txt[1].strip()
    if SPLIT_TITLE and "--" in title:
        content.extend(title.split("--"))
    else:
        content.append(title)
    return content


class CvSection:
    def __init__(self, title):
        self.title = title

    def to_tex(self):
        return "\\section{{{}}}".format(self.title)


class CvEntry:
    def __init__(self, content):
        self.content = content

    def to_tex(self):
        # generate cventry arguments based on  number of elements
        nb_par = 6
        nb_elt = len(self.content)
        start = "{{{}}}" * nb_elt
        end = "{{}}" * (nb_par - nb_elt)
        entry = f"\\cventry{start}{end}"
        return entry.format(*self.content)


class CvItem:
    def __init__(self, side_txt, title):
        self.side_txt = side_txt
        self.title = title

    def to_tex(self):
        title = self.title
        if title.startswith("-"):
            title = "\\( \\circ \\)" + title[1:]
        return "\\cvitem{{{}}}{{{}}}".format(self.side_txt, title)


class CurriculumVitae:
    def __init__(self, language=None):
        if language is None:
            language = "english"
        self.language = language
        self.name = ("John", "Doe")
        self.title = None
        self.content = None

    def from_markdown(self, markdown_src):
        self.content = []
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

            if line.startswith("![]"):
                self.photo = line.split("(")[1].split(")")[0]
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
            if line.startswith("`gitlab`"):
                self.gitlab = personal_info_from_md_line(line)
                i += 1
                continue

            if line.startswith("## "):
                self.content.append(CvSection(line.removeprefix("## ")))
                i += 1
                continue

            if line.startswith("### "):
                txt = line.removeprefix("### ")
                content = split_cv_line(txt)
                self.content.append(CvEntry(content))
                i += 1
                continue

            if line.strip() != "":
                content = split_cv_line(line)
                side_text = content[0]
                title = "--".join(content[1:])
                self.content.append(CvItem(side_text, title))
                i += 1
                continue

            i += 1

    def personal_data_to_tex(self):
        tex_out = []
        tex_out.append("\\name {{{}}}{{{}}}".format(self.name[0], self.name[1]))
        if self.title is not None:
            tex_out.append("\\title{{{}}}".format(self.title))
        if self.photo is not None:
            tex_out.append("\\photo[80pt][0pt]{{{}}}".format(self.photo))
        if self.email is not None:
            tex_out.append("\\email{{{}}}".format(self.email))
        if self.homepage is not None:
            tex_out.append("\\homepage{{{}}}".format(self.homepage))
        if self.linkedin is not None:
            tex_out.append("\\social[linkedin]{{{}}}".format(self.linkedin))
        if self.github is not None:
            tex_out.append("\\social[github]{{{}}}".format(self.github))
        if self.gitlab is not None:
            tex_out.append("\\social[gitlab]{{{}}}".format(self.gitlab))

        tex_out = "\n".join(tex_out)
        return tex_out

    def content_to_tex(self):
        content_lines = [item.to_tex() for item in self.content]
        return "\n".join(content_lines)

    def to_tex(self):
        tex_template = open("cv_template.tex", "rt").read()
        tex_template = tex_template.replace("$language", self.language)
        tex_template = tex_template.replace(
            "$personal_data", self.personal_data_to_tex()
        )
        tex_template = tex_template.replace("$content", self.content_to_tex())
        return tex_template


if __name__ == "__main__":
    src_filename = sys.argv[1]
    if len(sys.argv) > 2:
        language = sys.argv[2]
    else:
        language = None
    cv = CurriculumVitae(language)
    cv.from_markdown(open(src_filename, "rt").read())
    open(os.path.splitext(src_filename)[0] + ".tex", "wt").write(cv.to_tex())

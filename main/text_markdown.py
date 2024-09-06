import tkinter as tk
from tkinter import font
import re


def parse_markdown(md_text, text_widget):
    text_widget.delete("1.0", tk.END)

    bold_pattern = re.compile(r'\*\*(.*?)\*\*', re.DOTALL)
    italic_pattern = re.compile(r'_(.*?)_', re.DOTALL)
    # example_pattern = re.compile(r'<([\s\S]*)>')
    inline_code_pattern = re.compile(r'`(.*?)`', re.DOTALL)
    header_pattern = re.compile(r'^(#{1,6})\s*(.*)', re.MULTILINE)
    list_pattern = re.compile(r'^\*\s(.*)', re.MULTILINE)

    bold_font = font.Font(weight="bold")
    italic_font = font.Font(slant="italic")
    code_font = font.Font(family="Courier", size=10)
    header_fonts = {
        1: font.Font(weight="bold", size=18),
        2: font.Font(weight="bold", size=16),
        3: font.Font(weight="bold", size=14),
        4: font.Font(weight="bold", size=12),
        5: font.Font(weight="bold", size=10),
        6: font.Font(weight="bold", size=8)
    }

    text_widget.tag_configure('bold', font=bold_font)
    text_widget.tag_configure('italic', font=italic_font)
    text_widget.tag_configure('inline_code', font=code_font, background='lightgray')
    text_widget.tag_configure('example', font=code_font, background='lightgray')

    for level in range(1, 7):
        tag_name = f'header{level}'
        text_widget.tag_configure(tag_name, font=header_fonts[level])

    text_widget.tag_configure('list', lmargin1=20, lmargin2=40)

    def apply_tags(text, in_code_block):
        pos = 0
        while pos < len(text):
            match = None
            for pattern, tag in [
                (bold_pattern, 'bold'),
                (italic_pattern, 'italic'),
                (inline_code_pattern, 'inline_code'),
            ]:
                match = pattern.search(text, pos)
                if match:
                    start, end = match.span()
                    if start > pos:
                        text_widget.insert(tk.END, text[pos:start])

                    text_widget.insert(tk.END, match.group(1), tag)
                    pos = end
                    break

            if not match:
                if in_code_block:
                    text_widget.insert(tk.END, text[pos:], 'example')
                else:
                    text_widget.insert(tk.END, text[pos:])
                break

    lines = md_text.splitlines(keepends=True)
    in_code_block = False

    for line in lines:
        if line.strip().startswith("<") and not in_code_block:
            in_code_block = True
            text_widget.insert(tk.END, line.strip('<'), 'example')
            continue

        elif line.strip().endswith(">") and in_code_block:
            in_code_block = False
            line = line.replace(">", '')
            text_widget.insert(tk.END, line, 'example')
            continue

        if in_code_block:
            text_widget.insert(tk.END, line, 'example')
            continue

        header_match = header_pattern.match(line)
        if header_match:
            level = len(header_match.group(1))
            header_text = header_match.group(2)
            tag = f'header{level}' if level <= 6 else 'header6'
            text_widget.insert(tk.END, header_text + "\n", tag)
            continue

        list_match = list_pattern.match(line)
        if list_match:
            list_item = list_match.group(1)
            text_widget.insert(tk.END, f'• {list_item}\n', 'list')
            continue

        apply_tags(line, in_code_block)

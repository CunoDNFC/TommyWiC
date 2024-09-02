import tkinter as tk
from tkinter import font
import re

def parse_markdown(md_text, text_widget):
    text_widget.delete("1.0", tk.END)

    bold_pattern = re.compile(r'\*\*(.*?)\*\*')  # **bold**
    italic_pattern = re.compile(r'_(.*?)_')  # _italic_
    inline_code_pattern = re.compile(r'`(.*?)`')  # `inline code`
    header_pattern = re.compile(r'^(#+)\s*(.*)')  # ### Header
    list_pattern = re.compile(r'^\*\s(.*)')  # * list item

    text_widget.tag_configure('bold', font=font.Font(weight="bold"))
    text_widget.tag_configure('italic', font=font.Font(slant="italic"))
    text_widget.tag_configure('inline_code', font=font.Font(family="Courier", size=10), background='lightgray')
    text_widget.tag_configure('header1', font=font.Font(weight="bold", size=18))
    text_widget.tag_configure('header2', font=font.Font(weight="bold", size=16))
    text_widget.tag_configure('header3', font=font.Font(weight="bold", size=14))
    text_widget.tag_configure('list', lmargin1=20, lmargin2=40)

    def apply_tags(line):
        pos = 0
        while pos < len(line):
            match = inline_code_pattern.search(line, pos)
            if match:
                text_widget.insert(tk.END, line[pos:match.start()])
                text_widget.insert(tk.END, match.group(1), 'inline_code')
                pos = match.end()
            else:
                break

        line = line[pos:]
        pos = 0

        while pos < len(line):
            match = bold_pattern.search(line, pos)
            if match:
                text_widget.insert(tk.END, line[pos:match.start()])
                text_widget.insert(tk.END, match.group(1), 'bold')
                pos = match.end()
            else:
                break

        line = line[pos:]
        pos = 0

        while pos < len(line):
            match = italic_pattern.search(line, pos)
            if match:
                text_widget.insert(tk.END, line[pos:match.start()])
                text_widget.insert(tk.END, match.group(1), 'italic')
                pos = match.end()
            else:
                break

        text_widget.insert(tk.END, line[pos:])

    lines = md_text.splitlines()

    for line in lines:
        header_match = header_pattern.match(line)
        if header_match:
            level = len(header_match.group(1))
            header_text = header_match.group(2)
            tag = f'header{level}' if level <= 3 else 'header3'
            text_widget.insert(tk.END, header_text + "\n", tag)
            continue

        list_match = list_pattern.match(line)
        if list_match:
            list_item = list_match.group(1)
            text_widget.insert(tk.END, f'• {list_item}\n', 'list')
            continue

        apply_tags(line + "\n")
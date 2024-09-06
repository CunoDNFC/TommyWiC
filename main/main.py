import tkinter as tk
from tkinter import Menu, Text, INSERT, END, filedialog, messagebox, simpledialog
from text_markdown import parse_markdown
from dotenv import load_dotenv
import io, sys, re, os
from grammar.TommyWiCParser import TommyWiCParser
from grammar.TommyWiCLexer import TommyWiCLexer
from antlr4 import InputStream, CommonTokenStream
from customVisitor import customVisitor

load_dotenv()

start_phrase = 'Oh hi Mark'
end_phrase = 'What a story, Mark'

output_stream = io.StringIO()

EXAMPLES_FILE = "examples.md"
if not os.path.exists(EXAMPLES_FILE):
    os.makedirs(EXAMPLES_FILE)


def interpret_code(code):
    sys.stdout = output_stream
    input_stream = InputStream(code)
    lexer = TommyWiCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TommyWiCParser(token_stream)
    tree = parser.program()
    visitor = customVisitor()
    result = visitor.visit(tree)
    sys.stdout = sys.__stdout__
    return result


def run_code():
    code = code_input.get("1.0", END).strip()
    if re.fullmatch(rf"{re.escape(start_phrase)}\s*{re.escape(end_phrase)}", code, re.DOTALL):
        result = ('Why Lisa! Why Lisa! Why don\'t you talk to me! Come on Lisa! Lisa! Lisa! Lisa! Talk to me please! '
                  'Without you I would be nothing. You are my life, my everything, I could not go on without you Lisa')
    else:
        output_stream.seek(0)
        output_stream.truncate()
        interpret_code(code)
        result = output_stream.getvalue()

    output_display.config(state=tk.NORMAL)
    output_display.insert(END, result)
    output_display.config(state=tk.DISABLED)


def clear_all():
    clear_input()
    clear_output()


def clear_input():
    code_input.delete("1.0", END)
    code_input.insert("1.0", f"{start_phrase}\n\n{end_phrase}")
    code_input.mark_set(INSERT, "2.0")
    code_input.focus()


def clear_output():
    output_display.config(state=tk.NORMAL)
    output_display.delete("1.0", END)
    output_display.config(state=tk.DISABLED)


def save_code_to_file(code_text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(code_text)
        messagebox.showinfo("Save Code", "It's good for you. Don't worry about it.")


def show_wiki():
    wiki_window = tk.Toplevel(root)
    wiki_window.title("Wiki")
    wiki_window.geometry("600x600")

    wiki_text = tk.Text(wiki_window, wrap=tk.WORD)
    wiki_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    try:
        with open('Syntax.md', 'r', encoding='utf-8') as file:
            md_content = file.read()
            parse_markdown(md_content, wiki_text)
    except FileNotFoundError:
        wiki_text.insert(tk.END, "Wiki in progress...")


def show_examples():
    if not hasattr(show_examples, 'examples_window') or not tk.Toplevel.winfo_exists(show_examples.examples_window):
        show_examples.examples_window = tk.Toplevel(root)
        show_examples.examples_window.title("Examples")
        show_examples.examples_window.geometry("600x600")

        examples_text_widget = tk.Text(show_examples.examples_window, wrap=tk.WORD)
        examples_text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        load_examples(examples_text_widget)


def add_code_to_examples(examples_text_widget):
    code = examples_text_widget.get("1.0", tk.END)
    save = messagebox.askyesno("Save", "Are you sure? For now, deletion is only possible manually from the file")

    if save:
        with open(EXAMPLES_FILE, 'a', encoding='utf-8') as file:
            example_name = simpledialog.askstring("Input", "Enter information about this example:")

            if example_name:
                file.write(f"\n### {example_name}\n\n")
                file.write(f"<{code}>")

        messagebox.showinfo("Success!", "You're so unique. Let me kiss you")


def load_examples(examples_text_widget):
    try:
        with open(EXAMPLES_FILE, 'r', encoding='utf-8') as file:
            md_content = file.read()
            parse_markdown(md_content, examples_text_widget)
    except FileNotFoundError:
        examples_text_widget.insert(tk.END, "No examples available now")


def on_closing():
    root.attributes("-fullscreen", False)
    root.destroy()


def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))


def minimize_window(event=None):
    root.iconify()


def maximize_window(event=None):
    root.state('zoomed')


root = tk.Tk()
root.title("TommyWiC")
root.geometry("1200x700")

root.attributes("-fullscreen", False)
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.bind("<Alt-m>", minimize_window)
root.bind("<Alt-x>", maximize_window)
root.protocol("WM_DELETE_WINDOW", on_closing)

code_input = Text(root, wrap=tk.WORD)
code_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

code_input.insert("1.0", f"{start_phrase}\n\n{end_phrase}")
code_input.mark_set(INSERT, "2.0")
code_input.tag_add("gray_text", "1.0", "1.end")
code_input.tag_add("gray_text", "3.0", "3.end")
code_input.tag_configure("gray_text", foreground="gray")
code_input.focus()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

run_button = tk.Button(button_frame, text="Run", command=run_code)
run_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear all", command=clear_all)
clear_button.pack(side=tk.LEFT)

clear_input_button = tk.Button(button_frame, text="Clear input", command=clear_input)
clear_input_button.pack(side=tk.LEFT)

clear_output_button = tk.Button(button_frame, text="Clear output", command=clear_output)
clear_output_button.pack(side=tk.LEFT)

save_button = tk.Button(button_frame, text="Save", command=lambda: save_code_to_file(code_input.get("1.0", tk.END)))
save_button.pack(side=tk.LEFT)

add_to_examples_button = tk.Button(button_frame, text="Add to Examples",
                                   command=lambda: add_code_to_examples(code_input))
add_to_examples_button.pack(side=tk.LEFT)

output_display = Text(root, wrap=tk.WORD, state=tk.DISABLED)
output_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

menu = Menu(root)
root.config(menu=menu)

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Show wiki", command=show_wiki)
help_menu.add_command(label="Show examples", command=show_examples)

root.mainloop()

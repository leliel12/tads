#!/usr/bin/env python3
import nbconvert
import nbformat
import os

def join_notebooks(directory=".", output_filename="out.ipynb"):
    notebooks = []
    for filename in os.listdir(directory):
        if filename.endswith(".ipynb") and filename != output_filename:
            notebooks.append(filename)

    if not notebooks:
        print("No notebooks found in the directory.")
        return

    final_notebook = nbformat.v4.new_notebook()
    for notebook_file in notebooks:
        with open(notebook_file, 'r') as f:
            nb = nbformat.read(f, as_version=4)
            final_notebook.cells.extend(nb.cells)

    nbformat.write(final_notebook, output_filename)

if __name__ == "__main__":
    join_notebooks()


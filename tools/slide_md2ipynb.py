#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# slide_md2ipynb.py
# License: MIT
# author: @leliel12

# =============================================================================
# DOCSTRING
# =============================================================================

"""Reads and processes a pandoc-markdown-beamer file and converts it to a \
notebook.

The resulting notebook is written to stdout.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import os
import argparse
import sys
import re

import nbformat as nbf

# =============================================================================
# CONSTANTS
# =============================================================================

RX_CODE = r"```(\w*)\n([\s\S]*?)```"

# =============================================================================
# FUNCTIONS
# =============================================================================


def mdsplit(content):
    """
    Splits markdown content by specific delimiters without including the delimiter.

    Args:
        content (str): Markdown content.

    Returns:
        list: List of content sections without delimiters.
    """
    # Create regex pattern that matches both "---" and "----"
    rx_slide = r"^(-{3,4})\s*$"

    # Split the content using re.split
    sections = re.split(rx_slide, content, flags=re.MULTILINE)

    # Filter out any empty sections and the captured delimiter groups
    processed_sections = [section.strip() for section in sections
                         if section and section.strip() and not re.match(r'^-+$', section.strip())]

    return processed_sections


def split_cells(content):
    """Splits a markdown string into alternating segments of markdown text \
    and code blocks.

    Args:
        content (str): Markdown content with code blocks.

    Returns:
        list: List of alternating markdown text and code block content.

    """
    rx_code = r"```(\w*)\n([\s\S]*?)```"

    # Split the content by code blocks
    parts = []
    last_end = 0

    for match in re.finditer(rx_code, content):
        # Add the markdown text before the code block (if any)
        markdown_text = content[last_end : match.start()].strip()
        if markdown_text:
            parts.append(("md", markdown_text))

        # Add the code block content with its language
        # Get the language identifier or default to ""
        language = match.group(1) if match.group(1) else ""
        code_content = match.group(2)
        parts.append((language, code_content))

        last_end = match.end()

    # Add any remaining markdown text after the last code block
    remaining_text = content[last_end:].strip()
    if remaining_text:
        parts.append(("md", remaining_text))

    return parts


def to_notebook(sections):
    """Converts a list of sections into a notebook.

    Args:
        sections (list): List of sections to convert.

    Returns:
        nbformat.NotebookNode: Notebook object.
    """
    notebook = nbf.v4.new_notebook()

    # iterate over the sections
    for section in sections:

        # split the section into cells
        cells = split_cells(section)

        # add the cells to the notebook
        for idx_in_section, (cell_type, cell_content) in enumerate(cells):
            # create a new cell
            if cell_type == "md":
                cell = nbf.v4.new_markdown_cell(source=cell_content)
            else:
                cell = nbf.v4.new_code_cell(source=cell_content)

            if idx_in_section == 0:  # first cell of the section
                cell.metadata.update(slideshow={"slide_type": "slide"})

            notebook.cells.append(cell)
    return notebook


# =============================================================================
# CLI
# =============================================================================


def get_parser():
    """
    Creates and configures the argument parser.

    Returns:
        ArgumentParser: Configured argument parser.
    """
    # Configure the argument parser
    parser = argparse.ArgumentParser(description="Reads and processes a markdown file.")

    # Add argument for the file path
    parser.add_argument("file_path", type=str, help="Path to the markdown file to read")

    # Add argument for the output file path
    parser.add_argument(
        "--output",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="Path to save the output notebook file (default: stdout)",
    )

    return parser


def main():
    """
    Main function that processes command line arguments and executes the program.

    Returns:
        int: Exit code (0 for success).
    """
    # Get the arguments
    parser = get_parser()
    args = parser.parse_args()

    # Read the file content
    with open(args.file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Split the content into sections
    sections = mdsplit(content)

    # Convert to notebook
    notebook = to_notebook(sections)

    # Write the notebook
    nbf.write(notebook, args.output)

    return 0


if __name__ == "__main__":
    sys.exit(main())

import os
import sys
from pdf2docx import Converter

def pdf_to_word(pdf_file):
    # Derive the output Word file name
    base_name = os.path.splitext(pdf_file)[0]
    word_file = f"{base_name}.docx"

    # Create a Converter object
    cv = Converter(pdf_file)
    
    # Convert the PDF to Word
    cv.convert(word_file, start=0, end=None)
    
    # Close the converter object
    cv.close()

    print(f"Conversion complete: {word_file}")

def convert_pdfs_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder {folder_path} does not exist.")
        return

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a PDF
        if file_name.lower().endswith('.pdf'):
            pdf_file = os.path.join(folder_path, file_name)
            pdf_to_word(pdf_file)

if __name__ == "__main__":
    # Check if a folder path was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_word.py <path_to_folder>")
    else:
        folder_path = sys.argv[1]
        convert_pdfs_in_folder(folder_path)

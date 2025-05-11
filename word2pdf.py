import os
import subprocess

def word_to_pdf(input_path):
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        return
    command = [
        'libreoffice',
        '--headless',
        '--convert-to', 'pdf',
        '--outdir', os.path.dirname(input_path),
        input_path
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted '{input_path}' to PDF.")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")

if __name__ == "__main__":
    filename = input("Enter The filename :").strip()
    filename = filename.strip("'\"")
    input_path = os.path.abspath(filename)
    word_to_pdf(input_path)
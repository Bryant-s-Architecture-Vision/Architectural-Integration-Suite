# FileReader.py
import argparse
import os
import markdown

def read_and_convert_md_to_html(file_path):
    # Read the markdown file
    with open(file_path, 'r') as md_file:
        md_content = md_file.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)

    # Return the HTML content
    return html_content

def main(md_file_path, output_path):
    html_content = read_and_convert_md_to_html(md_file_path)

    # Save the HTML content to the output file
    with open(output_path, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--md_file_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)

    args = parser.parse_args()
    main(args.md_file_path, args.output_path)

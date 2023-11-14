# FileReader.py
import argparse
import os
import markdown
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

def read_and_convert_md_to_html(file_path):
    # Validate file path
    if not os.path.exists(file_path):
        logging.error(f"Markdown file not found: {file_path}")
        return None

    try:
        # Read the markdown file
        with open(file_path, 'r') as md_file:
            md_content = md_file.read()

        # Convert markdown to HTML
        html_content = markdown.markdown(md_content)
        return html_content

    except Exception as e:
        logging.error(f"Error reading/converting file: {e}")
        return None

def main(md_file_path, output_path):
    html_content = read_and_convert_md_to_html(md_file_path)

    if html_content is not None:
        # Save the HTML content to the output file
        try:
            with open(output_path, 'w') as html_file:
                html_file.write(html_content)
            logging.info(f"HTML content written to {output_path}")
        except Exception as e:
            logging.error(f"Error writing to file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--md_file_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)

    args = parser.parse_args()
    main(args.md_file_path, args.output_path)

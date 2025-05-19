import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    template_file = open(template_path, "r")
    try:
        content_from = from_file.read()
        content_template = template_file.read()

        html_node = markdown_to_html_node(content_from)
        html = html_node.to_html()

        title = extract_title(content_from)

        full_html = content_template.replace("{{ Title }}", title)
        full_html = full_html.replace("{{ Content }}", html)
        full_html = full_html.replace('href="/', 'href="' + basepath)
        full_html = full_html.replace('src="/', 'src="' + basepath)

        dest_dir_path = os.path.dirname(dest_path)
        if dest_dir_path != "":
            os.makedirs(dest_dir_path, exist_ok=True)
        new_file = open(dest_path, "w")
        try:
            new_file.write(full_html)
        finally:
            new_file.close()

    finally:
        from_file.close()
        template_file.close()

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

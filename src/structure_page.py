from block_helpers import block_to_block_type, BlockType, markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line[:2] == '# ':
            return line[2:].strip()

    raise Exception()


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_file = f.read()

    with open(template_path, "r") as t:
        template_file = t.read()

    html = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as d:
        d.write(template_file)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for unit in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, unit)
        to_path = os.path.join(dest_dir_path, unit)
        if os.path.isfile(from_path):
            if unit.endswith(".md"):
                generate_page(from_path, template_path, to_path[:-3] + ".html")
        elif os.path.isdir(from_path):
            generate_page_recursive(from_path, template_path, to_path)
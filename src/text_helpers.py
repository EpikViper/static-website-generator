from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text) == 0:
            new_nodes.append(node)
        elif len(split_text) % 2 == 0:
            raise Exception() 
        else:
            for i in range(len(split_text)):
                current_text = split_text[i]
                if i % 2 == 0:
                    node = TextNode(current_text, TextType.TEXT)
                else:
                    node = TextNode(current_text, text_type)
                
                new_nodes.append(node)


    return new_nodes
            

def extract_markdown_images(text):
    alt_texts = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_texts

def extract_markdown_links(text):
    alt_texts = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_texts


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            current_position = 0
            for i in range(len(images)):
                alt_text = images[i][0]
                url = images[i][1]
                combined_text = f"![{alt_text}]({url})"
                position = node.text.find(combined_text, current_position)
                pretext = node.text[current_position:position]
                if len(pretext) > 0:
                    pretext_node = TextNode(pretext, TextType.TEXT)
                    new_nodes.append(pretext_node)
                image_node = TextNode(alt_text, TextType.IMAGE, url)
                new_nodes.append(image_node)
                current_position = position + len(combined_text)

            leftover = node.text[current_position:]
            if len(leftover) > 0:
                last_node = TextNode(leftover, TextType.TEXT)
                new_nodes.append(last_node)

    return new_nodes 



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            current_position = 0
            for i in range(len(links)):
                alt_text = links[i][0]
                url = links[i][1]
                combined_text = f"[{alt_text}]({url})"
                position = node.text.find(combined_text, current_position)
                pretext = node.text[current_position:position]
                if len(pretext) > 0:
                    pretext_node = TextNode(pretext, TextType.TEXT)
                    new_nodes.append(pretext_node)
                image_node = TextNode(alt_text, TextType.LINK, url)
                new_nodes.append(image_node)
                current_position = position + len(combined_text)

            leftover = node.text[current_position:]
            if len(leftover) > 0:
                last_node = TextNode(leftover, TextType.TEXT)
                new_nodes.append(last_node)

    return new_nodes 
                
                
def text_to_textnodes(text):
    starting_textnode = TextNode(text, TextType.TEXT)

    bold_split = split_nodes_delimiter([starting_textnode], "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, "_", TextType.ITALIC)
    code_split = split_nodes_delimiter(italic_split, "`", TextType.CODE)
    link_split = split_nodes_link(code_split)
    image_split = split_nodes_image(link_split)

    return image_split


print(text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))
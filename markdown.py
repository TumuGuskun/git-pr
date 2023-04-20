from enum import Enum
import re
from mistletoe import Document, HTMLRenderer
from mistletoe.base_elements import WalkItem
from markdownify import markdownify

from gum import GumSelection, gum_choose_multiple, gum_confirm, gum_input


class Token(Enum):
    LIST = "List"
    HEADING = "Heading"
    RAW_TEXT = "RawText"
    HTML_SPAN = "HTMLSpan"
    HTML_BLOCK = "HTMLBlock"


def get_template_contents(template_file_path: str) -> Document:
    with open(template_file_path, "r") as template_file:
        return Document.read(template_file.read())


def fill_sections(template: Document) -> Document:
    for heading in template.walk(tokens=[Token.HEADING.value]):
        for comment in heading.node.walk(tokens=[Token.HTML_SPAN.value]):
            if "fill=true" in comment.node.content:
                heading_title = next(heading.node.walk(tokens=[Token.RAW_TEXT.value]))
                section_filling = gum_input(message=heading_title.node.content)
                heading_title.node.content += f"\n{section_filling}"
    return template


def display_list_element(list_element: WalkItem) -> str:
    return list_element.node.content.replace("[ ] ", "")


def replace_boxed_text(selection_text: str) -> str:
    reason_regex = re.compile(r"\[(.*?)\]")
    if match := re.search(reason_regex, selection_text):
        reason = gum_input(message=match.group(1))
        selection_text = re.sub(reason_regex, f"[{reason}]", selection_text)
    return selection_text


def fill_checkboxes(template: Document) -> Document:
    heading = ""
    limit = 1
    for child in template.walk(
        tokens=[Token.LIST.value, Token.HEADING.value, Token.HTML_BLOCK.value]
    ):
        if child.node.name == Token.HEADING.value:
            heading = next(child.node.walk(tokens=[Token.RAW_TEXT.value])).node.content
        elif child.node.name == Token.HTML_BLOCK.value:
            if match := re.search(r"limit=(\d+)", child.node.content):
                limit = int(match.group(1))
            else:
                limit = 1
        else:
            choices = []
            for list_element in child.node.walk(tokens=["RawText"]):
                if "[ ]" in list_element.node.content:
                    choices.append(list_element)

            if len(choices) == 1:
                selection = choices[0]
                if not gum_confirm(message=selection.node.content):
                    continue
                gum_selections = [GumSelection(selection=selection, index=0)]
            else:
                gum_selections = gum_choose_multiple(
                    choices=choices,
                    message=heading,
                    limit=limit,
                    display_function=display_list_element,
                )

            for gum_selection in gum_selections:
                selection_text = display_list_element(gum_selection.selection)
                selection_text = replace_boxed_text(selection_text=selection_text)
                choices[gum_selection.index].node.content = f"[x] {selection_text}"

    return template


def get_body_from_template(template: Document) -> str:
    template = fill_checkboxes(template=template)
    template = fill_sections(template=template)
    pr_body = markdownify(HTMLRenderer().render(template)).replace("*", "-")
    return pr_body

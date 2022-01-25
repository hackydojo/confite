def multiline_handler(text: string, break_line_character: string) -> List[String]:
    lines_list: list[str] = text.split(break_line_character)
    multiline_text: string
    if len(lines_list) > 0:
        for index in range(len(lines_list) - 1):
            lines_list[index] += '\n'
    return lines_list

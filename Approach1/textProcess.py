import re

def process_text(text):
    #1.trim new lines and spaces
    text = text.strip()
    #2.split by \n and remove \t and filter out empty lines
    lines =list(filter(lambda line : line not in [""," ","\n"],text.replace("\t","").split("\n")))
    ouput_text = ""
    #3.trim spaces for each line
    #check whether consecutive spaces are present in the text and remove it and also add " " at the last of line
    for i in range(len(lines)):
        line_text = ""
        #line_text = lines[i].replace(r"\s\s+"," ")
        line_text = remove_spaces(lines[i])
        pattern = r"[a-zA-Z0-9]"
        if not re.match(pattern, line_text[0]):
            line_text = line_text.strip(line_text[0]+" ")
        lines[i] = line_text.strip()
    return " ".join(lines)


def remove_spaces(text):
    output_text=""
    isPreviousSpace = False
    for char in text:
        if char != " ":
            output_text += char
            isPreviousSpace = False
        else:
            if(not isPreviousSpace):
                output_text += char
                isPreviousSpace = True
    return output_text
import re

def json_serializer(raw_data:str) -> str:
    # for d in raw_data:
    regex_key = re.findall(r'.*:', raw_data.strip("themes:"))
    regex_content = re.findall(r':.*\n', raw_data.strip("themes:"))
    empty_string_key = ""
    empty_string_content = ""
    regex_key = (empty_string_key + x for x in regex_key)
    regex_content = (empty_string_content + x for x in regex_content).__next__()


json_serializer("""themes:{
    "hello":"this is a hello",
    "bi":"this is a bi"
}""")
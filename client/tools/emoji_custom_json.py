import os

# Directory of this Python file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Target directory relative to this file
target_directory = os.path.join(current_directory, "../src/assets/images/emoji")

def get_all_files_in_directory(directory_path):
    file_list = []
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_list.append(os.path.join(root, file_name))
    return file_list

all_files = get_all_files_in_directory(target_directory)

emoji_definitions = []

for file_path in all_files:
  file_name_with_extension = os.path.basename(file_path)
  file_name_without_extension = os.path.splitext(file_name_with_extension)[0]

  emoji_definition = f"{{name: '{file_name_without_extension}', file: '{file_name_with_extension}', keywords: ['{file_name_without_extension}']}}"
  emoji_definitions.append(emoji_definition)

# print(emoji_definitions)

emoji_definitions = ", ".join(map(str, emoji_definitions))


file_content = f"export const custom = [{emoji_definitions}]"
file_name = "emoji_custom.ts"
file_path = os.path.join(current_directory, file_name)
with open(file_path, 'w') as f:
    f.write(file_content)
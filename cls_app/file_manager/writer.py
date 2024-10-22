def write_to_file(file_name: str, text: str) -> str:
    with open(file_name, "a") as file:
        file.write(text)
        file.write("\n")

"""This module parses the port from the config"""
class PortOrAddressNotFoundException(Exception):
    """This is just a custom error derived from Exception. It's just for less obscure errors."""

def parse_port(file_path: str) -> int:
    """Parses the port from the given file_path, with some simple error handling"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in f.read().split("\n"):
                if i.startswith("port="):
                    return int(i[len("port="):])
            raise PortOrAddressNotFoundException(f"No port or address in file {file_path}")
    except FileNotFoundError:
        input(f"The file {file_path} was not found.")
        exit()

def parse_address_and_port(file_path: str) -> list[int, str]:
    """This is basically parse_port(file_path), but it also parses the address."""
    try:
        output = [0, ""]
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in f.read.split('\n'):
                if i.startswith("port="):
                    output[0] = int(i[len("port="):])
                elif i.startswith("address="):
                    output[1] = i[len("address="):]
                if output[0] != 0 and output[1] != "":
                    return output
            raise PortOrAddressNotFoundException(f"No port or address in file {file_path}")
    except FileNotFoundError:
        input(f"The file {file_path} was not found.\nPress enter to exit...")
        exit()

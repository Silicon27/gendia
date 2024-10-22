import os
import argparse
from typing import TextIO, Optional

# ANSI escape codes for coloring
COLOR_BLUE = '\033[94m'  # Blue for directories
COLOR_GREEN = '\033[92m'  # Green for Python files
COLOR_YELLOW = '\033[93m'  # Yellow for compiled Python files
COLOR_RESET = '\033[0m'  # Reset to default color
COLOR_ORANGE = '\033[33m'  # Orange for JavaScript files
COLOR_RED = '\033[31m'  # Red for C files
COLOR_LIGHT_BLUE = '\033[36m'  # Light blue for C++ files
COLOR_PURPLE = '\033[35m'  # Purple for Java files
COLOR_PINK = '\033[95m'  # Pink for Ruby files
COLOR_WHITE = '\033[97m'  # White for text files
COLOR_GRAY = '\033[90m'  # Gray for other files
COLOR_MAGENTA = '\033[95m'  # Magenta for image files
COLOR_CYAN = '\033[96m'  # Cyan for audio files
COLOR_LIGHT_GREEN = '\033[92m'  # Light green for video files
COLOR_LIGHT_YELLOW = '\033[93m'  # Light yellow for compressed files
COLOR_LIGHT_RED = '\033[91m'  # Light red for executable files
COLOR_LIGHT_PURPLE = '\033[95m'  # Light purple for library directories
UNDERLINE = '\033[4m'  # Underline for symbolic links

def get_color(entry: str) -> str:
    """Returns color based on file type."""
    if os.path.isdir(entry):
        return COLOR_BLUE
    elif entry.endswith('.py'):
        return COLOR_GREEN
    elif entry.endswith('.pyc'):
        return COLOR_YELLOW
    elif entry.endswith('.js'):
        return COLOR_ORANGE
    elif entry.endswith('.c'):
        return COLOR_RED
    elif entry.endswith('.cpp'):
        return COLOR_LIGHT_BLUE
    elif entry.endswith('.java'):
        return COLOR_PURPLE
    elif entry.endswith('.rb'):
        return COLOR_PINK
    elif entry.endswith('.txt'):
        return COLOR_WHITE
    elif entry.endswith('.jpg') or entry.endswith('.png') or entry.endswith('.gif'):
        return COLOR_MAGENTA
    elif entry.endswith('.mp3') or entry.endswith('.wav'):
        return COLOR_CYAN
    elif entry.endswith('.mp4') or entry.endswith('.avi') or entry.endswith('.mkv'):
        return COLOR_LIGHT_GREEN
    elif entry.endswith('.zip') or entry.endswith('.tar') or entry.endswith('.gz'):
        return COLOR_LIGHT_YELLOW
    elif entry.endswith('.exe'):
        return COLOR_LIGHT_RED
    elif os.path.islink(entry):
        return UNDERLINE
    else:
        return COLOR_RESET

def print_tree(directory: str, prefix: str = '', output: Optional[TextIO] = None) -> None:
    # List all entries in the directory, sorting them so that directories come first
    entries = sorted(os.listdir(directory), key=lambda x: (not os.path.isdir(os.path.join(directory, x)), x))

    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = index == len(entries) - 1
        color = get_color(path) if output is None else ''
        reset = COLOR_RESET if output is None else ''

        # Print the current item with the appropriate prefix
        line = f"{prefix}└── {color}{entry}{reset}" if is_last else f"{prefix}├── {color}{entry}{reset}"
        if output:
            output.write(line + '\n')
        else:
            print(line)

        # If the current item is a directory, recursively print its contents
        if os.path.isdir(path):
            new_prefix = f"{prefix}    " if is_last else f"{prefix}│   "
            print_tree(path, new_prefix, output)

def main() -> None:
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Display a color-coded tree-like directory structure")
    parser.add_argument('directory', type=str, nargs='?', default='.', help='The directory to display (default: current directory)')
    parser.add_argument('-o', '--output', type=str, help='The output file to write the diagram to')
    args = parser.parse_args()

    # Get the absolute path of the directory
    directory = os.path.abspath(args.directory)
    if os.path.isdir(directory):
        if args.output:
            try:
                with open(args.output, 'w+') as output_file:
                    output_file.write(directory + '\n')
                    print_tree(directory, output=output_file)
                print(f"\033[32mDirectory structure written to {args.output}\033[0m")
            except IsADirectoryError:
                print(f"\033[31m{args.output} is a directory, please provide a valid file name\033[0m")
            except PermissionError:
                print(f"\033[31mPermission denied to write to {args.output}\033[0m")
        else:
            print(f"\033[1m{directory}\033[0m")
            print_tree(directory)
    else:
        print(f"\033[31m{directory} is not a valid directory\033[0m")

if __name__ == '__main__':
    main()
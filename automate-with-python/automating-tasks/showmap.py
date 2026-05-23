import webbrowser
import sys
import pyperclip

def main():
    # If command line arguments were provided (besides the script name)
    # sys.argv reads command line arguments as a list; first element is the script name.
    if len(sys.argv) > 1:
        # Join all arguments into a single address string (skipping script name)
        address = ' '.join(sys.argv[1:])
    else:
        # Otherwise, get the address from the clipboard (Retrieves the current text from the system clipboard.)
        address = pyperclip.paste()

    # Build the OpenStreetMap search URL
    url = f'https://www.openstreetmap.org/search?query={address}'

    # Open the web browser
    webbrowser.open(url)

if __name__ == '__main__':
    main()
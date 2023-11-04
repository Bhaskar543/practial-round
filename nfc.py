    # We need to install that library using pip install nfcy

import nfc

def on_connect(tag):
    print("Connected to NFC tag:")
    print(tag)

# Create an NFC context manager
clf = nfc.ContactlessFrontend()

try:
    # Connect to the first available NFC device
    clf.open('tty:')

    # Initialize the connection
    clf.connect(rdwr={'on-connect': on_connect})

finally:
    # Close the connection
    clf.close()
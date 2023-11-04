    # We need to install that library using pip install pybluez
import bluetooth

# Search for nearby Bluetooth devices
nearby_devices = bluetooth.discover_devices()

# Print the list of nearby devices
for addr in nearby_devices:
    print("Found device with address: ", addr)

# Choose the device you want to connect to
device_address = nearby_devices[0]  # Replace with the address of your chosen device

# Create a Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Specify the port for communication
port = 1

# Connect to the device
try:
    sock.connect((device_address, port))
    print("Connected successfully to", device_address)

    # Send and receive data with the connected device
    sock.send("Hello, Bluetooth Device!")
    data = sock.recv(1024)
    print("Received message:", data)

    # Close the socket connection
    sock.close()

except bluetooth.btcommon.BluetoothError as err:
    print("An error occurred:", err)



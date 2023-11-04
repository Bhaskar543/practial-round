import ctypes

# Load the shared library
sdk_lib = ctypes.CDLL('/path/to/example_sdk.so')  # Replace with the actual path to your SDK's shared library

# Define the function prototypes
sdk_lib.example_function.argtypes = [ctypes.c_int, ctypes.c_int]
sdk_lib.example_function.restype = ctypes.c_int

# Call the functions from the SDK
result = sdk_lib.example_function(2, 3)  # Replace with actual function call and parameters from your SDK

# Handle the result as needed
print(f"Result from SDK: {result}")

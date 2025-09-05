import stegpy.lsb
import os

# Construct absolute paths for the input files
image_path = "safe_image.png"
message_path = "give-me-the-secret-key.txt"

# Create a HostElement object
host = stegpy.lsb.HostElement(image_path)

# Read the secret message
with open(message_path, "r") as f:
    message = f.read()

# Insert the message into the image
host.insert_message(message.encode('utf-8'), bits=1)

# Save the new image
host.save()

print("Message hidden in _safe_image.png using stegpy.")
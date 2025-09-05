from stegano import lsb

# Read the secret message
with open("give-me-the-secret-key.txt", "r") as f:
    secret_message = f.read()

# Using basic LSB (Least Significant Bit) steganography to hide the message.
secret_image = lsb.hide("safe_image.png", secret_message)

# Save the new image
secret_image.save("stegano_image.png")

print("Message hidden in stegano_image.png using basic LSB.")
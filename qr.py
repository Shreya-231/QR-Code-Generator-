# qr_generator.py
import qrcode
from PIL import Image, ImageDraw

def generate_qr(data, file_name="qr_code.png", scale=10, border=4):
    """
    Generate a styled QR code using qrcode and Pillow.
    :param data: Text or URL to encode
    :param file_name: Output image file name
    :param scale: Pixel size of each QR box
    :param border: Width of the white border
    """

    # Create QRCode object with high error correction
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=scale,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR image
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Optional: add a border / shadow / rounded effect using Pillow
    # Create a slightly larger white background to simulate a card
    border_size = 40
    bg_width = img.width + border_size
    bg_height = img.height + border_size
    background = Image.new("RGB", (bg_width, bg_height), "#f9fafb")

    # Draw rounded rectangle effect
    draw = ImageDraw.Draw(background)
    corner_radius = 20
    draw.rounded_rectangle(
        (0, 0, bg_width, bg_height),
        radius=corner_radius,
        fill="#ffffff",
        outline="#d1d5db",
        width=2
    )

    # Paste the QR image at the center
    pos = ((bg_width - img.width) // 2, (bg_height - img.height) // 2)
    background.paste(img, pos)

    # Save the final QR code image
    background.save(file_name)
    print(f"✅ QR code generated and saved as '{file_name}'")

    # Optional: Show the image
    background.show()

if __name__ == "__main__":
    print("🔹 QR Code Generator 🔹")
    user_data = input("Enter text or URL to generate QR code: ").strip()
    if user_data:
        generate_qr(user_data)
    else:
        print("⚠️ No data entered. Exiting...")

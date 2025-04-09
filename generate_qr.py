import qrcode
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Environment variables with defaults
QR_DATA_URL = os.getenv("QR_DATA_URL", "https://github.com/Raz2997")  
QR_CODE_DIR = os.getenv("QR_CODE_DIR", "qr_codes")
QR_CODE_FILENAME = os.getenv("QR_CODE_FILENAME", "github_qr.png")
FILL_COLOR = os.getenv("FILL_COLOR", "black")
BACK_COLOR = os.getenv("BACK_COLOR", "white")

def generate_qr_code():
    try:
        # Ensure the output directory exists
        if not os.path.exists(QR_CODE_DIR):
            os.makedirs(QR_CODE_DIR)
            logging.info(f"Created directory: {QR_CODE_DIR}")

        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(QR_DATA_URL)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)
        
        # Save the QR code image
        output_path = os.path.join(QR_CODE_DIR, QR_CODE_FILENAME)
        img.save(output_path)
        logging.info(f"QR code generated successfully at {output_path}")
    except Exception as e:
        logging.error(f"Error generating QR code: {e}")

if __name__ == "__main__":
    generate_qr_code()
    
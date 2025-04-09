import qrcode
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_qr_code(url=os.getenv("QR_DATA_URL", "https://github.com/Raz2997"), 
                    output_dir=os.getenv("QR_CODE_DIR", "qr_codes")):
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info(f"Created directory: {output_dir}")

        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Generate the QR code image
        fill_color = os.getenv("FILL_COLOR", "black")
        back_color = os.getenv("BACK_COLOR", "white")
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save the QR code image
        filename = os.getenv("QR_CODE_FILENAME", "github_qr.png")
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)
        logging.info(f"QR code generated successfully at {output_path}")
    except Exception as e:
        logging.error(f"Error generating QR code: {e}")

if __name__ == "__main__":
    generate_qr_code()
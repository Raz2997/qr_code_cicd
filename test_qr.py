import os
from generate_qr import generate_qr_code

def test_qr_generation():
    url = "https://github.com/Raz2997"
    output_dir = "test_qr_codes"
    generate_qr_code(url, output_dir)
    assert os.path.exists(f"{output_dir}/github_qr.png"), "QR code file was not created"
    print("Test passed: QR code generated successfully")

if __name__ == "__main__":
    test_qr_generation()
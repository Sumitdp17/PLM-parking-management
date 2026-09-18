import qrcode
from reportlab.pdfgen import canvas


def generate_receipt(receipt_path, plate_number, hours, amount):
    # Generate QR code content
    qr_data = f"{plate_number}|{hours}|{amount}"
    qr = qrcode.make(qr_data)

    # Save QR to static folder
    qr_path = f"app/static/receipts/{plate_number}.png"
    qr.save(qr_path)

    # Create PDF receipt
    c = canvas.Canvas(receipt_path)
    c.setFont("Helvetica", 14)
    c.drawString(50, 750, "Smart Parking System - Payment Receipt")
    c.drawString(50, 720, f"Vehicle Number: {plate_number}")
    c.drawString(50, 700, f"Total Hours Parked: {hours} hours")
    c.drawString(50, 680, f"Amount Paid: ₹{amount}")
    c.drawString(50, 650, "Scan QR below to validate receipt")

    # Draw QR
    c.drawImage(qr_path, 50, 500, width=120, height=120)

    c.save()

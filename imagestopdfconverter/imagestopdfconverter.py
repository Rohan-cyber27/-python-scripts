import img2pdf
import os

# Specify the directory containing images
img_dir = "C:/Users/rohan/OneDrive/Pictures/Camera Roll"
output_pdf_path = "C:/Users/rohan/OneDrive/Pictures/Camera Roll/image.pdf"

# Collect image file paths
image_files = [os.path.join(img_dir, fname) for fname in os.listdir(img_dir) if fname.endswith(('.jpg', '.jpeg', '.png'))]

# Sort the image files if you need a specific order
image_files.sort()

# Convert images to PDF
pdf_bytes = img2pdf.convert(image_files)

# Write the PDF to a file
with open(output_pdf_path, "wb") as file:
    file.write(pdf_bytes)

print("Successfully created PDF.")

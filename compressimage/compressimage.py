from PIL import Image

def compress_image():
    try:
        image_name = input("Enter the name of the image you want to compress (e.g., image.jpg): ")
        image = Image.open(image_name)
    except FileNotFoundError:
        print("Image not found. Using default image 'default_image.jpg'.")
        image = Image.open('default_image.jpg')
    
    # Get image dimensions
    width, height = image.size
    
    # Maintain aspect ratio and reduce the size by half
    new_width = width // 2
    new_height = height // 2
    
    # Resize the image
    compressed_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    # Save the compressed image with a fixed name
    output_path = 'compressed_image.jpg'
    compressed_image.save(output_path, quality=85)
    
    print(f"Compressed image saved as '{output_path}'.")

# Run the function
compress_image()

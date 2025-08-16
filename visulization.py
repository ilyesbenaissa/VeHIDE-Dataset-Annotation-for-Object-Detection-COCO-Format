import json
import os
import random
from PIL import Image, ImageDraw, ImageFont

def load_coco_data(file_path):
    """Loads a COCO JSON annotation file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file at '{file_path}' is not a valid JSON file.")
        return None

def visualize_coco_annotations(coco_data, image_directory, num_images=5):
    """
    Selects random images from the COCO dataset and draws their
    bounding boxes.
    """
    if not coco_data:
        print("COCO data is empty or not loaded.")
        return

    # Create mappings for easy lookups
    images_dict = {img['id']: img for img in coco_data['images']}
    categories_dict = {cat['id']: cat for cat in coco_data['categories']}
    
    # Group annotations by image_id
    annotations_by_image = {}
    for ann in coco_data['annotations']:
        img_id = ann['image_id']
        if img_id not in annotations_by_image:
            annotations_by_image[img_id] = []
        annotations_by_image[img_id].append(ann)

    # Get a random sample of image IDs that have annotations
    annotated_image_ids = list(annotations_by_image.keys())
    if not annotated_image_ids:
        print("No annotations found in the dataset.")
        return
        
    if len(annotated_image_ids) < num_images:
        print(f"Warning: Requested {num_images} images, but only {len(annotated_image_ids)} have annotations. Visualizing all.")
        num_images = len(annotated_image_ids)

    random_image_ids = random.sample(annotated_image_ids, num_images)

    print(f"Displaying {num_images} random images with annotations...")

    # Generate a color for each category
    category_colors = {cat_id: (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)) for cat_id in categories_dict.keys()}

    for img_id in random_image_ids:
        image_info = images_dict[img_id]
        image_path = os.path.join(image_directory, image_info['file_name'])

        try:
            # Open the image
            with Image.open(image_path) as img:
                draw = ImageDraw.Draw(img)
                
                # Get a font
                try:
                    font = ImageFont.truetype("arial.ttf", 15)
                except IOError:
                    font = ImageFont.load_default()

                # Draw each annotation for this image
                for ann in annotations_by_image[img_id]:
                    bbox = ann['bbox']
                    category_id = ann['category_id']
                    category_info = categories_dict[category_id]
                    class_name = category_info['name']
                    color = category_colors[category_id]

                    # Bbox format is [x_min, y_min, width, height]
                    x_min, y_min, width, height = bbox
                    x_max, y_max = x_min + width, y_min + height

                    # Draw rectangle and label
                    draw.rectangle([x_min, y_min, x_max, y_max], outline=color, width=3)
                    draw.text((x_min + 5, y_min + 5), class_name, fill=color, font=font)

                # Display the image
                img.show(title=f"Image: {image_info['file_name']}")

        except FileNotFoundError:
            print(f"\nError: Image file not found at {image_path}")
        except Exception as e:
            print(f"\nAn error occurred while processing {image_path}: {e}")


if __name__ == "__main__":
    # --- Configuration ---
    # IMPORTANT: Update this path to where your images are stored.
    IMAGE_DIR = "validation/validation"
    COCO_JSON_PATH = "coco_annotations_val.json"

    # Number of random images to display
    IMAGES_TO_SHOW = 5

    if IMAGE_DIR == "path/to/your/images":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! PLEASE UPDATE the 'IMAGE_DIR' variable in the script !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        # You might need to install Pillow: pip install Pillow
        coco_dataset = load_coco_data(COCO_JSON_PATH)
        if coco_dataset:
            visualize_coco_annotations(coco_dataset, IMAGE_DIR, IMAGES_TO_SHOW)

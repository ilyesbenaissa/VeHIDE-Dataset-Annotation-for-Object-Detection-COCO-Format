# VeHIDE Dataset for Object Detection (COCO Format)

This repository contains annotations VeHIDE (Vehicle Hidden) dataset, formatted for object detection tasks using the popular **COCO annotation** style. The dataset is designed for training models to detect various types of vehicle damage.

A Python script is included to help you visualize the bounding box annotations on the images to verify the dataset's integrity.

## About the annotation
- **Format**: COCO (JSON)
- **Task**: Object Detection
- **Content**: Images of vehicles with annotated regions of damage
- **Classes**: vo_kinh, tray_son, thung, mop_lom, be_den, mat_bo_phan, rach

## Prerequisites

Before you begin, ensure you have Python 3 installed. You will also need to install the Pillow library to run the visualization script.

```bash
pip install Pillow
```
## Dataset: 
You can [Download the VeHIDE dataset from Kaggle](https://www.kaggle.com/datasets/hendrichscullen/vehide-dataset-automatic-vehicle-damage-detection/data) and place them in the right directory. (check File Structure section below)

## Setup & Usage

Follow these steps to visualize the dataset annotations.


### 1. File Structure

Organize your project files as follows. The visualization script should be in the same directory as your COCO annotation file.

```
your-project-folder/
├── image/image/                  <-- The folder containing train dataset images
│   ├── train_image1.jpg
│   └── train_image2.jpg
│
├── validation/validation/         <-- The folder containing validation dataset images
│   ├── validation_image1.jpg
│   └── validation_image2.jpg
│
├── coco_annotations.json        <-- The COCO annotation file for the train dataset
├── coco_annotations_val.json    <-- The COCO annotation file for the validation dataset
│
└── visualization.py             <-- The script to check the annotations
```

### 2. Configure the Visualization Script

You must update the `IMAGE_DIR` variable in `visualization.py` to point to the directory where your images are stored.

In `visualization.py`:

```python
# --- Configuration ---
# IMPORTANT: Update this path to where your images are stored.
IMAGE_DIR = "./images" # Or "C:/path/to/your/images"
COCO_JSON_PATH = "coco_annotations.json"
IMAGES_TO_SHOW = 5 # Number of random images to display
```

### 3. Visualize and Verify

Execute the script from your terminal to see the annotations.

```bash
python visualization.py
```

This will open several windows, each showing a random image from the dataset with the bounding boxes and class labels drawn on top. This is the best way to explore the dataset and confirm that the annotations are correct.

## File Descriptions

- **visualization.py**: A utility script to parse the COCO file and display annotated images for verification
- **coco_annotations.json**: The annotation file for the training set, ready for use with object detection models that support the COCO format
- **coco_annotations_val.json**: The annotation file for the validation set, ready for use with object detection models that support the COCO format
- **/image/image** (directory): Contains all the source train images for the dataset
- **/validation/validation** (directory): Contains all the source train images for the dataset

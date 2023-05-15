import cv2
import pickle
import glob2

# Define the paths to the TIFF images and segmentation masks
img_path = "/Users/afoix/Git/phdstuff/allen_dataset_downloader/downloaded_data/crop_dataset/dna/230741/dna_crop_raw_230741_7922e74b69b77d6b51ea5f1627418397ab6007105a780913663ce1344905db5c_raw.ome.tif"
mask_path = "/Users/afoix/Git/phdstuff/allen_dataset_downloader/downloaded_data/crop_dataset/dna/dna_crop_seg_230741_a9a2aa179450b1819f0dfc4d22411e6226f22e3c88f7a6c3f593d0c2599c2529_segmentation.ome.tif"
output_file = "//Users/afoix/Git/phdstuff/tiff2pickle/output.pickle"

# Create empty lists to store the images and masks
images = []
masks = []

# Loop through each image and mask file
for i, file in enumerate(glob2.glob(img_path)):
    # Read in the image and mask files
    img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    mask_file = file.replace("images", "masks").replace(".tiff", "_mask.tiff")
    mask = cv2.imread(mask_file, cv2.IMREAD_UNCHANGED)

    # Append the images and masks to their respective lists
    images.append(img)
    masks.append(mask)

# Combine the images and masks into a dictionary
data = {"images": images, "masks": masks}

# Save the dictionary as a pickle file
with open(output_file, "wb") as f:
    pickle.dump(data, f)
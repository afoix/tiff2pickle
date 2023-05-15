import tiffile as tiff
import numpy as np
import os

"""Create a script that takes .tif files and converts them to .npy files."""

directory = "/Users/afoix/Git/phdstuff/allen_dataset_downloader/downloaded_data/crop_dataset/dna_test"

"""Loop through the directory and load each .tif file."""
for filename in os.listdir(directory):
    if "raw" in filename:
        tif = tiff.imread(os.path.join(directory, filename))
        tif = tif.astype(np.float32)
        tif = (tif - tif.mean()) / tif.std()
        np.save(os.path.join(directory, filename + ".npy"), tif)
    
        continue
    else:
        tifseg = tiff.imread(os.path.join(directory, filename))
        tifseg = (tifseg / 255).astype(np.int64)
        np.save(os.path.join(directory, filename + ".npy"), tifseg)
        continue


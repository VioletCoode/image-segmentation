import numpy as np
import pandas as pd
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from skimage.segmentation import flood


import skimage.data
from skimage.exposure import histogram
from skimage.filters import sobel, threshold_otsu
from skimage.measure import regionprops_table
from skimage.segmentation import watershed,flood
from skimage.color import label2rgb
from matplotlib.widgets import Slider
from skimage import io, color


image = io.imread("Medical_images/image3.png")
gray = color.rgb2gray(image)

plt.figure(figsize=(6,6))
plt.imshow(gray)#, cmap="gray")
plt.title("Original Medical Image")
plt.axis("off")
plt.show()


from skimage import color

gray = color.rgb2gray(image)

# Convert back to 8-bit (0–255)
image = (gray * 255).astype(np.uint8)

print(f"Loaded image in an array of shape: {image.shape} and data type {image.dtype}")
print(f"Intensity range: [{image.min()} - {image.max()}]")

plt.figure(figsize=(6,6))
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Original Medical Image")
plt.axis("off")
plt.show()

hist, hist_centers = histogram(image)
plt.figure(figsize=(8, 4))
plt.plot(hist_centers, hist)
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()


threshold = threshold_otsu(image)


def segment_image(threshold):
    binary_image = image > threshold

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].imshow(image, cmap="gray")
    ax[0].set_title("Original Image")
    ax[0].axis("off")

    img=ax[1].imshow(binary_image, cmap="gray") 
    ax[1].set_title(f"Segmented Image (Threshold = {threshold})")
    ax[1].axis("off")

    slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])
    slider = Slider(
    slider_ax,
    "Threshold",
    image.min(),
    image.max(),
    valinit=threshold,
    valstep=1
    )

    def update(val):                                                      
        threshold =slider.val                                           
        binary_image = image > threshold                                  
        img.set_data(binary_image)                                        
        ax[1].set_title(f"Segmented Image (Threshold = {int(threshold)})")
        fig.canvas.draw_idle()                                           
    slider.on_changed(update)                                            
    plt.show()            

segment_image(threshold)

edges = sobel(image)

#watershead segemntation is displayed
plt.figure(figsize=(6, 6))
plt.imshow(edges, cmap="gray")
plt.title("Sobel Edge Detection")
plt.axis("off")
plt.show()



threshold = threshold_otsu(image)

markers = np.zeros_like(image)

markers[image <= threshold] = 1      # Background
markers[image > threshold] = 2        # Foreground
segmentation = watershed(edges, markers)
print(np.unique(segmentation))

plt.figure(figsize=(6, 6))
plt.imshow(segmentation)
plt.colorbar()
plt.axis("off")
plt.title("Watershed Segmentation")
plt.show()



filled = ndi.binary_fill_holes(segmentation - 1)
plt.figure(figsize=(6,6))
plt.imshow(filled, cmap="gray")
plt.title("Binary Filled Holes")
plt.axis("off")
plt.show()
labeled_segmentation, _ = ndi.label(filled)



plt.figure(figsize=(6, 6))
plt.imshow(labeled_segmentation)
plt.title("Connected Component Labeling")
plt.axis("off")
plt.colorbar()
plt.show()


fig, ax = plt.subplots(figsize=(12, 6))
rgb_composite = label2rgb(
    labeled_segmentation,
    image=image,
    bg_label=0
)

ax.imshow(rgb_composite)
ax.set_title("RGB Colored Segmentation by watershed segmentation")
plt.axis("off")
plt.show()

seed_points = [
    (300, 450),
    (350, 850),
    (450, 1150),
    (550, 700),
    (650, 1350),

    (800, 500),
    (900, 900),
    (1000, 1400),

    (1200, 600),
    (1300, 1050),
    (1450, 1450),

    (1600, 700),
    (1700, 1200)
]
tolerance = 18

region_growing = np.zeros_like(image, dtype=bool)
for seed in seed_points:
    grown = flood(image, seed_point=seed, tolerance=tolerance)
    region_growing = region_growing | grown

#displaying region growing segmentationn
plt.figure(figsize=(6,6))
plt.imshow(region_growing, cmap="gray")
plt.title("Region Growing Segmentation")
plt.axis("off")
plt.show()


region_labels, num_regions = ndi.label(region_growing)

print("Number of regions:", num_regions)

fig, ax = plt.subplots(figsize=(12, 6))


rgb_region = label2rgb(
    region_labels,          # labeled regions
    image=image,            # original grayscale image
    bg_label=0              # keep background as label 0
)

ax.imshow(rgb_region)
ax.set_title("RGB Region Growing Segmentation")
plt.axis("off")
plt.show()

rgb_region = label2rgb(
    region_labels,          # labeled regions
    image=image,            # original grayscale image
    bg_label=0              # keep background as label 0
)



properties= regionprops_table(#regionprops_table calculates every mesurments for every labeled objects and stores them in tabel
    labeled_segmentation,
    intensity_image=image, 
    properties=[
        'label',
        'area',
        'centroid',
        'bbox',
        'eccentricity',
        'intensity_mean'
    ]
)


df = pd.DataFrame(properties)
df.head()
print(df.head())
df.describe()
print(df.describe())
#saving the results to a CSV file
df.to_csv("cell3_watershed_segmentation_analysis.csv", index=False)
print("Watershed Segemntation data saved successfully!")

properties_rg = regionprops_table(
    region_labels,
    intensity_image=image,
    properties=[
        'label',
        'area',
        'centroid',
        'bbox',
        'eccentricity',
        'intensity_mean'
    ]
)

df_rg = pd.DataFrame(properties_rg)

print(df_rg.head())

df_rg.to_csv("cell3_region_growing_analysis.csv", index=False)

print("Region Growing data saved successfully!")



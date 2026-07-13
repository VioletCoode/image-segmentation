
#import ipywidgets not required as we dont use ipynb we use py
import numpy as np
import pandas as pd
import scipy.ndimage as ndi
import matplotlib.pyplot as plt


import skimage.data
from skimage.exposure import histogram
from skimage.filters import sobel, threshold_otsu
from skimage.measure import regionprops_table
from skimage.segmentation import watershed
from skimage.color import label2rgb
from matplotlib.widgets import Slider # used to create a slider for thresholding and segmentation of the image


# Load the sample image
image = skimage.data.coins()

# Print image information
print(f"Loaded image in an array of shape: {image.shape} and data type {image.dtype}")
print(f"Intensity range: [{image.min()} - {image.max()}]")

# Display the image
plt.figure(figsize=(6, 6))
plt.imshow (image,cmap="gray")
plt.title("Original Image")
plt.axis("off")
plt.show()

# Display Histogram
hist, hist_centers = histogram(image)
plt.figure(figsize=(8, 4))
plt.plot(hist_centers, hist)
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()

# Threshold Segmentation


threshold = threshold_otsu(image)       # Calculate Otsu's threshold

def segment_image(threshold):
    binary_image = image > threshold

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].imshow(image, cmap="gray")
    ax[0].set_title("Original Image")
    ax[0].axis("off")

    img=ax[1].imshow(binary_image, cmap="gray")  #It displays the segmented image and stores its image object so it can be updated later
    ax[1].set_title(f"Segmented Image (Threshold = {threshold})")
    ax[1].axis("off")


    # # Create slider(it works only for ipynb)
    # threshold_slider = ipywidgets.IntSlider(
    #     value=threshold,
    #     min=0,
    #     max=255,
    #     step=1,       
    #  description="Threshold:",
    #     continuous_update=True
    # )

    #adds slider to the threshold

    slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])#centered slider below the plots without covering the images
    #[0.1, 0.05, 0.8, 0.03] → Longer slider  [0.3, 0.05, 0.4, 0.03] → Shorter, centered slider   0.2, 0.9, 0.6, 0.03] → Slider at the top of the figure
    
    
    slider = Slider(

    slider_ax,          #slider ax put the slider inside an rectangle
    "Threshold",        #threshold is the text innside the slider
    0,                  #minimum vallue
    255,                #maximum value
    valinit=threshold,  #stores the initial position
    valstep=1           #how much step to move at 1 time

    )

    #prints the threshold image with the slider


    def update(val):                                                      #this function is run whenever the usser moves the slider
        threshold =slider.val                                             #it reads the current value of the slider
        binary_image = image > threshold                                  #create new segmented image
        img.set_data(binary_image)                                        #replaces the old image with the new segmented image
        ax[1].set_title(f"Segmented Image (Threshold = {int(threshold)})")#updates the ax[1] tile
        fig.canvas.draw_idle()                                            #refresh the canvas fig
    slider.on_changed(update)                                             #it connect the slider with the function
    plt.show()                                                            #commands to show the image

segment_image(threshold)


# Interactive widget (Works in Jupyter Notebook)
#ipywidgets.interactive(segment_image, threshold=threshold_slider) - cannot be used as its py not ipynb


#watershead segmentation
edges = sobel(image)

#watershead segemntation is displayed
plt.figure(figsize=(6, 6))
plt.imshow(edges, cmap="gray")
plt.title("Sobel Edge Detection")
plt.axis("off")
plt.show()

#using markers for watershed segmentation
markers = np.zeros_like(image)
markers[image < 30] = 1   #background
markers[image > 150] = 2  #foreground
                          #while unkown region becomes 0
segmentation = watershed(edges, markers)
print(np.unique(segmentation))

plt.figure(figsize=(6, 6))
plt.imshow(segmentation)
plt.colorbar()
plt.axis("off")
plt.title("Watershed Segmentation")
plt.show()

#filling holes in the segmented image
filled = ndi.binary_fill_holes(segmentation - 1)#assigns a unique label to each connected object after the segmentation is complete
plt.figure(figsize=(6,6))
plt.imshow(filled, cmap="gray")
plt.title("Binary Filled Holes")
plt.axis("off")
plt.show()

#connected component labeling;
labeled_segmentation, _ = ndi.label(filled)

plt.figure(figsize=(6, 6))
plt.imshow(labeled_segmentation)
plt.title("Connected Component Labeling")
plt.axis("off")
plt.colorbar()
plt.show()

#mesuring region properties
properties = regionprops_table(labeled_segmentation, intensity_image=image, properties=['label', 'area', 'centroid', 'bbox', 'eccentricity', 'intensity_mean'])

df = pd.DataFrame(properties)

df.head()
print(df.head())
df.describe()
print(df.describe())

#saving the results to a CSV file
df.to_csv("coin_blobs_analysis.csv", index=False)
print("Data saved successfully!")

#rgb coloured segmentation
fig, ax = plt.subplots(figsize=(12, 6))
rgb_composite = label2rgb(labeled_segmentation, image=image, bg_label=0)#label 0 is treated as bg
ax.imshow(rgb_composite)
plt.axis('off')
ax.set_title("RGB Colored Segmentation")
plt.show()


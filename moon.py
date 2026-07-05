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
from matplotlib.widgets import Slider

image=skimage.data.moon() # it loads the image of a moon from skiage library

# Print image information
print(f"Loaded image in an array of shape: {image.shape} and data type {image.dtype}")
print(f"intensity range:[{image.min()} - {image.max()}]") 

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

#Threshold Segmentation


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
    slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])#Python creates an empty rectangle
    
    #adds slider to the threshold
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

#watershead segmentation
edges=sobel(image)
#displaying the sobel image detection image
plt.figure(figsize=(6,6))
plt.imshow(edges, cmap="grey")
plt.title("Sobel image detection")
plt.axis("off")
plt.show()

#using markers for watershed segmentation
markers = np.zeros_like(image)
markers[image < 70] = 1   #background
markers[image > 170] = 2  #foreground
#while unkown region becomes 0
# Different images have different brightness levels, so the marker values are adjusted accordingly.
segmentation = watershed(edges, markers)
print(np.unique(segmentation))

plt.figure(figsize=(6,6))
plt.imshow(segmentation)
plt.title("Watershed Segmentation")
plt.colorbar()
plt.axis("off")
plt.show()

#as binary works for only 0 and 1 we did segmentation -1
filled = ndi.binary_fill_holes(segmentation - 1)
plt.figure(figsize=(6,6))
plt.imshow(filled, cmap="gray")
plt.title("Binary Filled Holes")
plt.axis("off")
plt.show()
labeled_segmentation, _ = ndi.label(filled)
plt.figure(figsize=(6,6))
plt.imshow(labeled_segmentation)
plt.title("Connected Component Labeling")
plt.axis("off")
plt.colorbar()
plt.show()

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
df.to_csv("moon_blobs_analysis.csv", index=False)
print("Data saved successfully!")


#rgb coloured segmentation
fig, ax = plt.subplots(figsize=(12, 6))
rgb_composite = label2rgb(labeled_segmentation, image=image, bg_label=0)#label 0 is treated as bg
ax.imshow(rgb_composite)
plt.axis('off')
ax.set_title("RGB Colored Segmentation")
plt.show()







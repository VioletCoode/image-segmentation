Image Segmentation using Thresholding , Watershed Algorithm and Region Growing Algorithm

Overview-

This project demonstrates classical image segmentation techniques using Python and the scikit-image library. Two sample grayscale images (moon and coins) are processed to identify, separate, and analyze objects using Otsu Thresholding, Sobel Edge Detection, Watershed Segmentation, Region Growing Segmentation, Connected Component Labeling, and Region Property Analysis. The extracted measurements are exported as CSV files for further analysis.

Features-


-Image loading using scikit-image
-Histogram visualization
-Otsu's automatic thresholding
-Interactive/manual threshold adjustment (Moon image)
-Sobel edge detection
-Watershed segmentation
-Region Growing segmentation
-Hole filling using binary_fill_holes
-Connected component labeling
-Region property analysis
-CSV export of object measurements
-RGB visualization of segmented regions




Project Structure-


image-segmentation

├── moon.py

├── coins.py

├── moon_watershed_segmentation_analysis.csv

├── moon_region_growing_analysis.csv

├── coin_blobs_analysis.csv

├── .gitignore

└── README.md




Processing Pipeline-



Watershed Segmentation


1.Load the grayscale image
2.Display the histogram
3.Apply Otsu's thresholding
4.Detect edges using the Sobel filter
5.Generate foreground and background markers
6.Apply Watershed segmentation
7.Fill enclosed holes
8.Label connected components
9.Extract region properties
10.Save the results as CSV files
11.Display the RGB segmented image


Region Growing Segmentation


1.Select one or more seed points
2.Grow regions by grouping neighbouring pixels with similar intensity
3.Label the connected regions
4.Display RGB visualization of segmented regions
5.Extract region properties
6.Export the measurements to CSV






Region Properties Extracted-

- Label
- Area
- Centroid
- Bounding Box
- Eccentricity
- Mean Intensity


Output-

The project generates:

- Segmented images
- Watershed segmentation results
- Region Growing segmentation results
- Connected component labels
- RGB visualization for both segmentation methods
- CSV files containing object measurements




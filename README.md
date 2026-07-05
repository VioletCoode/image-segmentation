Image Segmentation using Thresholding and Watershed Algorithm

Overview-

This project demonstrates image segmentation using Python.
Two sample grayscale images (`moon` and `coins`) are processed to identify and analyze objects using thresholding, watershed segmentation, connected component labeling, and region property analysis.
The project also exports the measured properties of segmented objects into CSV files.

Features- 

- Image loading using **scikit-image**
- Histogram visualization
- Otsu's automatic thresholding
- Interactive/manual threshold adjustment (Moon image)
- Sobel edge detection
- Watershed segmentation
- Hole filling using `binary_fill_holes`
- Connected component labeling
- Region property analysis
- CSV export of object measurements
- Colored visualization of segmented regions



Project Structure-


image-segmentation/

├── moon.py

├── coins.py

├── moon_blobs_analysis.csv

├── coin_blobs_analysis.csv

├── .gitignore

└── README.md




Processing Pipeline-

For both images, the following steps are performed:

1. Load the grayscale image
2. Display the histogram
3. Apply Otsu's thresholding
4. Detect edges using the Sobel filter
5. Generate foreground and background markers
6. Apply watershed segmentation
7. Fill enclosed holes
8. Label connected components
9. Extract region properties
10. Save the results as CSV files
11. Display the RGB segmented image



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
- Connected component labels
- RGB-colored segmented visualization
- CSV files containing object measurements




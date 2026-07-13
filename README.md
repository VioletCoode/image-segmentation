Image Segmentation using Thresholding , Watershed Algorithm and Region Growing Algorithm

Overview-

This project demonstrates classical image segmentation techniques using Python and the scikit-image library. The project applies image segmentation to both sample grayscale images (coins and moon) and medical microscopy images.

The implemented techniques include Otsu Thresholding, Sobel Edge Detection, Watershed Segmentation, Region Growing Segmentation, Connected Component Labeling, and Region Property Analysis. The extracted measurements are exported as CSV files for further analysis.

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



-Application of segmentation techniques on medical microscopy images



DATASET



Sample Images

Coins Image – Used for demonstrating Watershed Segmentation on touching objects.


Moon Image – Used for demonstrating Region Growing Segmentation on gradual intensity variations.



Medical Images-



The project also includes segmentation of four medical microscopy images obtained from the Warwick Micronet dataset.



The implemented segmentation pipeline was applied to each medical image to analyze tissue structures using:



Watershed Segmentation


Region Growing Segmentation


Connected Component Labeling


Region Property Analysis




Project Structure-


image-segmentation/

│
├── coins.py

├── moon.py

├── medical1.py

├── medical2.py

├── medical3.py

├── medical4.py

│
├── Medical_images/

│   ├── image1.png

│   ├── image2.png

│   ├── image3.png

│   └── image4.png

│
├── coin_blobs_analysis.csv

├── moon_watershed_segmentation_analysis.csv

├── moon_region_growing_analysis.csv

│
├── cell1_watershed_segmentation_analysis.csv

├── cell1_region_growing_analysis.csv

│
├── README.md

└── .gitignore


Processing Pipeline-



1.Loading the grayscale



2.Display the histogram



3.Apply Otsu Thresholding



4.Perform Sobel Edge Detection




5.Generate foreground and background markers




6.Apply Watershed Segmentation




7.Fill holes (where applicable)




8.Label connected components



9.Extract region properties



10.Export measurements to CSV




11.Display RGB segmentation









Region Growing Segmentation-





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

-Thresholded images

-Sobel edge images


- Watershed segmentation results

  
- Region Growing segmentation results


- Connected component labels


- RGB visualization for both segmentation methods



- CSV files containing object measurements




Medical Image Results

The implemented segmentation techniques were also tested on four medical microscopy images.

The results demonstrate the application of classical image segmentation methods on complex biological images. Due to the dense arrangement of cells and overlapping tissue structures, the segmentation quality depends heavily on marker selection, threshold values, and seed point placement. This highlights the challenges of applying traditional segmentation techniques to real-world medical datasets.



Technologies Used
Python
NumPy
Pandas
Matplotlib
SciPy
scikit-image





OUTPUTS OF MEDICAL IMAGES-




<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/a1ac0512-c44a-45dc-9b5e-843de0bac0c8" />




<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/9481e7cd-ea3b-440e-8874-dfd17e898c08" />



<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/1a5d76e5-7596-4358-957d-64b9fb29ac31" />



<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/1fd04486-dd0a-41a5-b67e-b7de5557bd26" />


<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/d22eef65-9483-4f00-b42e-64c6b1888a95" />






<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/5d1a439c-e1eb-49e0-ba5c-a5c51cec005d" />





<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/6b8ddcb3-be90-42a6-9015-76dbc67d09e4" />




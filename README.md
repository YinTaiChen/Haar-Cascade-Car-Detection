# Haar-Cascade-Car-Detection

以 Haar Cascade 實現車輛偵測

Reference 1: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

Reference 2: https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html

Reference 3: https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf

## Steps
  1. Download positive and negative images from ImageNet (resized and converted to grayscale)
  2. Remove missing/error images
  3. Build a description file for negative images (bg.txt) 
  4. Build a vector file for positive images (info.dat) 
  5. Merge positive and negative images to create trainning examples
  6. Train cascades and collect the .xml files
  7. Let the cascade classifiers (.xml files) do object detection jobs for you!
  
## Results: using single haar cascade
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_36.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_22.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_723.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_342.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_39.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_187.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_42.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_13.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_11.jpg)
![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/result_1.jpg)
 
 ## Results: using multiple haar cascades
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_1.jpg)
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_2.jpg)
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_3.jpg) 
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_4.jpg) 
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_5.jpg) 
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_6.jpg) 
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_7.jpg) 
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_8.jpg) 
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_9.jpg) 
 ![alt text](https://github.com/YinTaiChen/Haar-Cascade-Car-Detection/blob/master/result/sample_10.jpg)
 
## GUI

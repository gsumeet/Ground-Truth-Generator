# Ground-Truth-Generator
By Ankush Saini & Sumeet Gupta

Tool to help mark ground truth in images

Shortcuts:
Key R - Resets the image
Key S - Saves the image
Key Q - Quits the current image selection
For continuous shapes - Select beginning point, hover to form shape & double right click.
For polygons - Select all vertices & double right click.

Motivation :
In any application of Computer vision, there is a strong need for ground truth. 
Ground truth is basically an observational output as compared to any inference that one may get from a computer’s algorithm. It is essential for this ground truth to be the most accurate. The motivation of this project is the need for ground truth marking and course project for CISC642. Creating ground truth is a tedious job when you consider the large number of images, the types of objects to mark and the colors to fill in. Through this project, we try to reduce the effort of a person who has to mark ground truth for his application.

Requirements :
1. User interface that supports easy upload of images, modification & export.
2. Selection of roads & buildings.
3. Selection of multiple points.
4. Filling up of shapes with solid color.

Tools/Libraries : 
1. Tinkr
2. Opencv 
3. Numpy

Instructions :
Key R - Resets the image
Key S - Saves the image
Key Q - Quits the current image selection
For continuous shapes - Select beginning point, hover to form shape & double right click. For polygons - Select all vertices & double right click.

Result :
The user is expected to select an image from his directory structure and then decide whether he wants to create curves or straight-line objects. Upon selecting from one of these, the user starts selecting boundary on the image. Upon completion, user enters the escape character. After this, the ground truth marked image is stored in the image directory. Below is a view showing the original image and the Ground truth marked image.

Conclusion :
The purpose of this project is to reduce manual time and effort needed for creating ground truths. Through this implementation, we aim at reducing the time needed by user to mark and color the ground truth. The difference is not noticeable at per image basis, but with increase in number of images, we should be able to see a significant decrease in the time required for creating ground truth. The user is allowed to continue selecting and modifying images till he likes, so there is no need for exiting the application and re-running it over and over again. Also, since our application is not heavy, we can neglect the execution time.

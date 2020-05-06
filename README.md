# Diagram-Vectorization

## Description

The aim of this project is to use deep-learning along with OpenCV to vectorize hand-drawn diagrams. The program uses OpenCV to detect shapes in an image, and then exports these shapes to a deep-learning program that classifies these shapes into geometrical ones. Next, the position, size, and orientation of the shapes is exported and used along with the classified shape type to redraw the diagram using vectors.

## How to setup

Firstly, you will need to install the required dependencies to start Tensorflow and Keras.
NOTE: We are using Python 3 in this project.

	$ git clone https://github.com/omar-dahrawy/Diagram-Vectorization.git
  	$ cd Diagram-Vectorization
	$ pip install -r requirements.txt
  
## How to run

To run this project, simply run export_shapes.py script using the following command:

  	$ python export_shapes.py --image 'image_path'
  
We added a sample hand-drawn diagram to test the code on: diagram-test-01.png
The export_shapes.py script detects the shapes in the image, and then exports the shapes, their coordinates, dimensions, and orientation to the .txt files found in Data folder. Note that the Data folder is created once you run the script. After that, predict.py script is run, which classifies each of the exported shapes and writes the categories in categories.txt also found in Data. Finally, draw_shapes.py is run, which reads the exported categories, coordinates, dimensions, and orientations, and then draws each shape in a new image as specified. The output image can be found in the Data folder, named "new_diagram.jpg".

## How it works

The script export_shapes.py uses contours and image moments to detect shapes drawn on a black background. It then crops these shapes, and exports them as separate images in Data/Cropped Shapes. It also exports the center coordinates of each shape to Data/centers.txt, the dimensions (top left x, top left y, width, height) to Data/dimensions.txt, and the orientaions to Data/orientations.txt . Then, the script calls on the predict.py script.

The predict.py script reads in the images in Data/Cropped Shapes, and classifies each shape according to the trained model, named drawing_classification.h5 . The model is trained on the dataset found inside the Shapes folder. The dataset includes 4 classes: Circle, Square, Triangle, and Line. You can retrain the model by running the cnn.py script using the following command:
	
		$ python cnn.py
		
After the predict.py script classifies the shapes, it exports the categories to Data/categories.txt, and calls on the draw_shapes.py .

The draw_shapes.py script reads the data from the categories, centers, dimensions, and orientations .txt files and redraws each shape as desired on a new image, and exports it to Data/new-diagram.jpg .

.
.
.
.

More info will be added as the project develops.

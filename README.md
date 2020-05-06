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
The export_shapes.py script detects the shapes in the image, and then exports the shapes, their coordinates, size, and orientation to the .txt files found in Data folder. Note that the Data folder is created once you run the script. After that, predict.py script is run, which classifies each of the exported shapes and writes the categories in categories.txt also found in Data. Finally, draw_shapes.py is run, which reads the exported categories, coordinates, sizes, and orientations, and then draws each shape in a new image as specified. The output image can be found in the Data folder, named "new_image.jpg".

.
.
.
.

More info will be added as the project develops.

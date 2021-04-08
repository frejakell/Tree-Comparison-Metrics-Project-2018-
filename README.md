# Tree-Comparison-Metrics-Project-2018-
Tree metric comparison Project 

Notes:
• Keep all code files in same directory to run GUI
• The GUI needs PyQt5 installed to run

## There are three main pages in the GUI
Front Page/Main page: Lets you create and upload tree data and configure your distance metrics
Result page: Shows the results of the distance metric in the form of a table
Center tree page: shows the result of the center tree analysis
To start GUI simply click the GUI.py module or type “GUI.py” into command prompt 


### Main Page 
![main_page](https://user-images.githubusercontent.com/8816121/114090623-84647c80-986c-11eb-8914-b899f3f88dd5.JPG)

#### If creating trees for scratch
1. Select mode: Full creates all trees of with the number of leaves indicated.
1.a. If you change the Random the screen will change to let you set number of trees as
well. 


![tree_intro](https://user-images.githubusercontent.com/8816121/114090870-d5747080-986c-11eb-95db-49f98a010b12.JPG)

 1.b. After picking mode set the number of trees and leaves you want (number of leaves
limited to 20 for Full mode). Also decide whether you want to build Rooted or Unrooted trees by
selecting the accurate radio button.
 1.c. you can choose to save your data in an output file if prefer otherwise simply check
“Store Results” and hit “OK”
 1.d. If you selected “Store Results” then the resulting trees should appear in the Newick
tree field. 

![tree_random2](https://user-images.githubusercontent.com/8816121/114092717-0eade000-986f-11eb-9e83-294ff05795d3.JPG)




#### If Uploading trees from file
Use the “Find File” button to open file explorer. Then navigate and open desired file. The content of the
file will display in the Newick trees field

![trees_File2](https://user-images.githubusercontent.com/8816121/114092553-ddcdab00-986e-11eb-8813-3a2a97bbbf28.JPG)


### Selecting Metric
When you have your trees simply select you desired metric:
![metric_selection2](https://user-images.githubusercontent.com/8816121/114092886-4157d880-986f-11eb-86ee-d64803033c51.JPG)


Do this by selecting the radio button that corresponds to the metric of interest.
• if you select more then one then the program will pick whichever comes first in its code.
• Also make sure to set Lambda if using KC metric.
Select “ok” at the bottom of the page(next to “Reset”) when ready to compute distances.

### Results page

![form](https://user-images.githubusercontent.com/8816121/114092347-a232e100-986e-11eb-9e50-2de3403d52bb.JPG)



The results page contains the results of the selected distance metric in the form of a table.
From here you can produce visuals of the data:
For the MDS plots pick either 2D or 3D and select whether you want labels on the data points and
colouring for the clusters.
Select “Plot” when ready.
A figure window(like the one shown below) will open and displayed the requested data. 

![results_page](https://user-images.githubusercontent.com/8816121/114091946-2a64b680-986e-11eb-9e93-12f1c84d2e74.JPG)






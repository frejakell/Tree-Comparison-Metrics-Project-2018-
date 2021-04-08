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

![tree_random](https://user-images.githubusercontent.com/8816121/114091081-14a2c180-986d-11eb-8ff6-86d99bdb7eb5.JPG)



#### If Uploading trees from file
Use the “Find File” button to open file explorer. Then navigate and open desired file. The content of the
file will display in the Newick trees field

![trees_File](https://user-images.githubusercontent.com/8816121/114091277-52074f00-986d-11eb-8404-e41e5e3d3a00.JPG)


### Selecting Metric
When you have your trees simply select you desired metric:
![metric_selection](https://user-images.githubusercontent.com/8816121/114091395-7ebb6680-986d-11eb-8715-9aa81a104129.JPG)





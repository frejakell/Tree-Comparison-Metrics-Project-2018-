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
![download - 2021-05-03T203117 678](https://user-images.githubusercontent.com/8816121/116958382-42eaa580-ac4f-11eb-9332-1f1291a203d6.png)

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

![download - 2021-05-03T203348 418](https://user-images.githubusercontent.com/8816121/116958451-88a76e00-ac4f-11eb-85c1-c8d87f5a91fc.png)


When done, simply close window and produce more plots if desired. 
For the Heatmaps select include dendrogram if you wish to see a dendrogram at the side of the
heatmap. Then simply select plot.

![heatmaps](https://user-images.githubusercontent.com/8816121/114093122-972c8080-986f-11eb-8b97-ccd93480f251.JPG)


Likewise, for the Distribution plots you can chose to let the code auto scale the histogram(select the
Auto-Scale checkbox) or use a constant value of 8 bins (Leave it unchecked). Then select “Plot ”.

![denogram](https://user-images.githubusercontent.com/8816121/114093183-a7dcf680-986f-11eb-88fb-e3bcc8d793c2.JPG)


The last available feature is the Center Trees option.
First select Cluster if you want the code to considered center trees for individual clusters as well the
complete set. Otherwise it will only look at the total set of input trees.
After that, select “Compute”. This will open to the Center Tree Summary page and the requested data
should be shown in the field on the page

![center_tree](https://user-images.githubusercontent.com/8816121/114093377-e4a8ed80-986f-11eb-9068-2865003ec920.JPG)



If you wish to save this data:
1. Type in output filename
2. Select Save. 




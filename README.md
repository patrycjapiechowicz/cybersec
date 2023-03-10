# WORK IN PROGRESS


# Malware detection system built using the EMBER dataset of 1.1 million PE(Portable Executable) Windows files.

![image](https://user-images.githubusercontent.com/66388735/217641205-39df832a-c783-48ff-b5b5-7047cc0c3fc3.png)


## This paper describes many more details about the dataset:  [paper](https://arxiv.org/abs/1804.04637)


## List of contents:
1. [Overview](#Overview)
2. [Purpose](#Purpose)
3. [Motivation](#Motivation)
4. [Technical Aspect](#Technical)
5. [Installation](#Installation)
6. [Technologies Used](#Technologies)

- ### Overview
This project is a part of the Data Science Working Group - FellowshipPL, Krakow.  A group founded by people passionate about Machine Learning. 
They regularly (twice per year) give students the opportunity to learn.
Malware detection system was built based on the EMBER dataset - a collection of features from PE Windows files.

- ### Purpose
The purpose of this project is to identify useful features for Malware Detection. Features include a handpicked selection of 100 PE libraries, boolean file properties (has_imports, has_exports, has_tls, etc.), 64 bytes of the PE entry point (used as a signature), and other features relevant to malware detection.


- ### Motivation
After graduation I wanted to hobbistically do some project, to know people from DS world and that is how I have found FellowshipPL. I was reponsible for exploratory data analysis, model training and model evaluation. My work can be found in 'pati' branch as below:

- ### Technical Aspect
This project is divided into few parts. 
1. Extracting data using MongoDB. More information can be found here: [MongoDB](https://github.com/patrycjapiechowicz/cybersec/tree/MongoDB-connection/notebooks)
2. Exploratory Data Analysis. More information can be found here: [EDA](https://github.com/patrycjapiechowicz/cybersec/tree/pati/notebooks) 
3. Model training and model evaluation. More information can be found here : [ETL](https://github.com/patrycjapiechowicz/cybersec/tree/ConnectionETL/notebooks) 

- ### Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

pip install -r requirements.txt

- ### Technologies Used

![image](https://user-images.githubusercontent.com/66388735/217648171-abdb5f02-2dcb-4999-9cb8-95620f046748.png)


<img src="https://www.kindpng.com/picc/m/159-1595924_python-logo-clipart-easy-pandas-python-logo-hd.png" alt="Python Logo Clipart Easy - Pandas Python Logo, HD Png Download@kindpng.com">

![scikit-learn-seeklogo com](https://user-images.githubusercontent.com/66388735/217648821-16755b8d-9637-4209-a3bc-be06b28dddea.svg)


![image](https://user-images.githubusercontent.com/66388735/217649145-17d3cb18-da3a-4592-95dc-942e2365da53.png)



















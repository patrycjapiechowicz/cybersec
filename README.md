## Malware detection system built using the EMBER dataset of 1.1 million PE (Portable Executable) Windows files.

![image](https://user-images.githubusercontent.com/66388735/217641205-39df832a-c783-48ff-b5b5-7047cc0c3fc3.png)


Table of Content:

<a href=”[www.facebook.com](https://arxiv.org/abs/1804.04637)”>paper</a>



This project is a part of the Data Science Working Group - FellowshipPL, Krakow.  A group founded by people passionate about Machine Learning. 
They regularly (twice per year) give students the opportunity to learn.
Based on the EMBER dataset - a collection of features from PE Windows files.


The purpose of this project is to identify useful features for Malware Detection. Features include a handpicked selection of 100 PE libraries, boolean file properties (has_imports, has_exports, has_tls, etc.), 64 bytes of the PE entry point (used as a signature), and other features relevant to malware detection.


I was reponsible for exploratory data analysis, model training and model evaluation. My work can be found in 'pati' branch as below:

https://github.com/patrycjapiechowicz/cybersec/tree/pati/notebooks

This paper describes many more details about the dataset: https://arxiv.org/abs/1804.04637



#minions

Team members: Chirag Jain, Sharmin Pathan

Project 4 - Neuron Finding

Approach: NMF and median filtering to find neurons in calcium imaging data

Technologies Used:
-----------------
    Python 2.7
    Thunder
    Matplotlib
    Median Filtering
    NMF

Introduction:
------------
Calcium Imaging is a dominant technique in modern neuroscience for measuring activity of large population of neurons. Several challenges remain in how to best process and extract signals from these data.

![alt tag](http://neurofinder.codeneuro.org/components/assets/movie.gif)        ![alt tag](http://neurofinder.codeneuro.org/components/assets/zooming.gif)

Problem Statement: 
-----------------
The challenge is to take the time varying images (left) and extract regions of interest (right) that correspond to individual neurons.

Preprocessing:
-------------
- A structured matrix factorization approach to analyzing calcium imaging recordings of large neuronal ensembles.
- Demix spatially overlapping regions
- Denoise and deconvolve spiking activity of each neuron
- Median filtering of the images
- NMF (Non-negative matrix factorization) to express the spatiotemporal fluorescence activity as a product of two matrices: a spatial matrix that encodes location of each neuron, and a temporal matrix that characterizes the calcium concentration of each neuron over time.


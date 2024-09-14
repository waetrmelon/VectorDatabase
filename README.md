# VectorDatabase
 
A vector database is a type of database that stores data as high-dimensional vectors, which are mathematical representations of features or attributes.

Why use a Vector Database?
- A vector database offers more complex search capabilities

What is a Vector in a Vector Database?
- A vector database cares about vectors, which are just numeric arrays representing a value.

How to use it?
- Each function declared inside of VecDB has an allocated file describing it's usage, find the file by looking at the Python file with the function name + "Test" at the end of the name.

Features:
- Display Graph of Vector Data
- Find the nearest Node from another Data Node on the graph.
- Generating a Graph value for the following supported Datatypes; String, Integer, Float. (Lists and Dictionaries are not supported yet).
- Generating a Node to be plot on the Graph, from a vector.
- Generating a Vector to applied into a Node, from data.
- Find nearest range of Nodes from a starting point within a certain value threshold.
- Calculating Similarity Between two Vector Node Values as a percentage.

NOTE: This is just the basis of a vector database and handling it data(s) this repo does not contain code to store the database which you can do in several ways, but instead of how to
manipulate and form vector data.

This image represents data being plotted on a Graph as Vector-Node Values.
Each increment by 1 on the X axis is a new Node containing a value, the value is calculated from it's data.
![Alt text](images/Image1.PNG?raw=true)
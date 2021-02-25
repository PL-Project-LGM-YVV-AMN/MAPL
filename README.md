# Matrix & Matrix Operations Programming Language
_Lenier Gerena Meléndez, Yadiel Vélez Vargas, Aramis Matos Nieves_

Universidad de Puerto Rico, Mayagüez

[Link to Phase I document](https://docs.google.com/document/d/1dfvMnkUe5Wjo51EHsakjpaxmlbP3l3K8RXAxQnGUtbM/edit?usp=sharing)
[Link to Documentation](https://github.com/PL-Project-LGM-YVV-AMN/PL-Project/blob/main/PreliminaryDocumentation.md)

## I. Introduction
Currently, several programming languages are capable and very well implemented to work with linear algebra methods, being MATLAB, R, and Python the biggest players. 

R is widely used for statistical computing and graphics, and it is open source, and hence completely free. However, its learning curve is somewhat steep, mostly because of its syntax. For example, (1) shows how we create a vector v with four elements 1, 2, 3, and 4.

1.	x <- c(1, 2, 3, 4)

Python is again widely used for statistical computing, graphics, and practically for everything. Even though Python is considered one of the best programming languages for beginners due to its simplicity in its syntax, when it comes to linear algebra, it is not that simplistic. The primary reason for that claim comes from its general-purpose nature. Python wasn’t designed to support matrices natively, so it has to rely on third-party libraries such as NumPy. For example, (2) illustrates how to create a simple vector with three elements:

2.	x = numpy.array([1, 2, 3])

Linear algebra is essentially MATLAB’s specialty, even its name is an abbreviation for “matrix laboratory”. It allows users not only to perform matrix manipulations, but also to plot functions and data, to create UIs, and even to interface with programs written in other languages. However, it also has some caveats. MATLAB is not free and being that the case, it holds a closed community. It nonetheless, to our knowledge, has the most simple syntax for performing linear algebra tasks. For example, (3) shows how a vector is declared.

3.	v = [1 2 3 4 5]

After this short overview through the most widely used programming languages for linear algebra methods we conclude that we seek to create a programming language with a readable, and intuitive syntax, is open-source, and finally, is designed with linear algebra in mind.

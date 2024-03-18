This is meant to become a library application where users can search for books 
by genre and format. If one submits the name of a book and their home address, then
the app is supposed to compute the closest library that has that book. This app isn't quite
ready yet. The hardest thing next is to somehow use the address and book name (submitted by a user)
in order to compute the optimal library, in the file result.html. This could take many rows. Would placing the required code inside {{ }} be the only option? Or could the submitted data be transferred to an external python file for use in computation, and then back to result.html?

A database could be used for storing the locations (perhaps 2D coordinates) 
of home addresses and of libraries, as well as for storing the different books in each library
(in different but related tables).

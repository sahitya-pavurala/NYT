1) To run the solution, Download the data file and the findstars.py and type from the terminal

    gunzip hygdata_v3.csv.gz | python findstars.py hygdata_v3.csv 5



2) How might your solution change if we wanted to create a findstars service
that can respond quickly to requests for distance from an arbitrary point
with no memory restrictions, and we want to query it to return the nearest
K stars from arbitrary point X=(x,y,z) ?

==> For the find star service, generate whole random numbers for the three coordinates
that replaces the (0,0,0) in the distance calculation function and calculate the distance
of the stars that are closer to this coordinate by sorting and slicing the dictionary
to capture the number coordinates of coordinates closer to this random point.
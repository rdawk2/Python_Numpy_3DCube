"""
590PR Spring 2018
Assignment 4, on Numpy
I provide you both a small and a large 3-D ndarray of signed numbers.
Their dimensions are such that they are cubes.
For the small array, you can see the expected output results in
the Doctest.
You are to complete the function that will search all sub-cubes of the
full ndarray, to find the sub-cube having the largest sum. Borrowing
terminology from set theory, where a set is still an 'improper' subset
of itself, the full cube has to be checked as a possibility as well as
all possible smaller subcubes within it.
Additionally, it should print the intermediate results for each size of
subcube, as shown in the example output.
"""

import numpy as np

def find_max_subcube(a: np.ndarray, show_intermediate_results=True) -> np.ndarray:
    """Given a cubical ndarray, search all subcubes (all proper
    and the improper one), to find which one has the maximum sum.
    Since there are negative numbers in the values, there's no
    way to predict where it will be, and there's no theoretical
    advantage for largest subcubes vs medium ones.
    :param a: the whole array to search
    :param show_intermediate_results: whether to print results per subcube size
    :return: the subcube ndarray that had max sum
    >>> cube = np.load(file='A4_cube_size5_example.npy', allow_pickle=False, mmap_mode=None)
    >>> cube[4,4,4]
    -97.094082653629087
    >>> m = find_max_subcube(cube)
    searching cube of width 5
    checking all subcubes of width  1, of which     125 exist.  Highest sum    95.15 found at position (3, 4, 2)
    checking all subcubes of width  2, of which      64 exist.  Highest sum   355.41 found at position (1, 3, 3)
    checking all subcubes of width  3, of which      27 exist.  Highest sum   433.42 found at position (0, 0, 1)
    checking all subcubes of width  4, of which       8 exist.  Highest sum   310.35 found at position (0, 1, 1)
    checking all subcubes of width  5, of which       1 exist.  Highest sum   -38.25 found at position (0, 0, 0)
    <BLANKLINE>
    Total number of subcubes checked: 225
    Highest sum found was 433.415033731 in a subcube of width 3 at position (0, 0, 1)
    """
    if (show_intermediate_results == True):
        print("searching cube of width",len(a))
    pos1 = [0, 0, 0] * len(a)
    b = []
    c = []
    f = []
    e = []
    length = 0
    for i in range(a.shape[0]):         #Loop to count subcubes
        for j in range(a.shape[0]):
            for k in range(a.shape[1]):
                for l in range(a.shape[2]):
                    if j + i + 1 <= a.shape[0] and k + i + 1 <= a.shape[1] and l + i + 1 <= a.shape[2]:
                        x1 = a[j:j + i + 1, k:k + i + 1, l:l + i + 1].sum()         #Calculate sums of all subcubes
                        pos1[i] = (j, k, l)                                         #Calculate positions and save in it list c
                        b.append(x1)                                                #Form list b with sums of all subcubes
                        c.append(pos1[i])
        index = b.index(max(b))         #Find index of max value from list
        e.append(max(b))
        position = c[index]             #Find position of max value
        f.append(position)
        length = length + len(b)        #Find number of subcubes 1x1x1, 2x2x2, and so on
        if (show_intermediate_results == True):
            print(("checking all subcubes of width  "+str(i+ 1)+","+" of which"+"%8d"+" exist.  Highest sum %8.2f found at position "+ str(c[index]))%(len(b),round(max(b), 2)))
        b.clear()
        c.clear()

    index_e = e.index(max(e))
    position1 = f[index_e]
    print("\nTotal number of subcubes checked:", length)
    print("Highest sum found was", (round(max(e),9)), "in a subcube of width", index_e + 1, "at position", position1)

    pos_highestcube = np.array(position1)
    count_max = len(pos_highestcube)
    x_coor = pos_highestcube.item(0)        #x coordinate of max cube
    y_coor = pos_highestcube.item(1)        #y coordinate of max cube
    z_coor = pos_highestcube.item(2)        #z coordinate of max cube

    return (a[x_coor:x_coor+count_max,y_coor:y_coor+count_max,z_coor:z_coor+count_max])     #return np array of coordinates with maximum subcube

if __name__ == '__main__':
    cube = np.load(file='A4_cube_size5_example.npy', allow_pickle=False, mmap_mode=None)
    sc = find_max_subcube(cube)
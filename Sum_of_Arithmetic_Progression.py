#等差数列

a=list(range(1,100,2))
print(a)

#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
#43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81,
#83, 85, 87, 89, 91, 93, 95, 97, 99]






#等差数列の和

def sum_of_arithmetics_progression(a,b):
    return (a+b)*(b-a+1)/2   #(初項+末項)*項数/2

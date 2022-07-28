def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print(source," --> ",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(source," --> ",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
# Driver code
n = 3
TowerOfHanoi(n,1,3,2) 
# 1, 2, 3 are the name of Towers

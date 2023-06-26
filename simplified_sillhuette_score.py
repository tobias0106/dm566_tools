import sys
# data =  [[[1,5],[2,3],[3,4],[10,1]],[[7,7],[7,8],[7,9],[6,8]]]
# data =  [[[1,5],[2,3],[3,4],[7,7],[7,8],[7,9],[6,8]],[[10,1]]]
# data =  [[[1,5],[2,3],[3,4]],[[7,7],[7,8],[7,9],[6,8],[10,1]]]
# data = [[[1],[3],[5]],[[7],[10],[11],[12]]]
# data = [[[1],[3]],[[5],[7]],[[10],[11],[12]]]
data = [[[1],[3]], [[5], [7]], [[10],[11],[12]]]

def mean(data):
    centroids = []
    for i in range(len(data)):
        cluster = data[i]
        cords = []
        n = len(cluster)
        print(cluster)
        for j in range(len(cluster[0])):
            cord = 0
            for p in cluster:
                cord = cord + p[j]
            cords.append(cord/n)
        centroids.append(cords)
    return centroids

def dist(mu, point):
    d = 0.0
    for i in range(len(mu)):
        d = d + (mu[i] - point[i])**2
    return d**0.5

def cfcr(cen, lst, idx):
    index = 0
    length = sys.maxsize 
    for i in range(len(lst)):
        if (i != idx and length > dist(cen, lst[i])):
            index = i
    return lst[index]

def ssc(data):
    score = 0
    n = 0
    print("------------------------------------------------------------------------------------------------------------------")
    print("Clusters:")
    centroids = mean(data)
    print("------------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------------")
    print("centroids: " + str(centroids))
    print("------------------------------------------------------------------------------------------------------------------")
    for i in range(len(centroids)):
        this = centroids[i]
        other = cfcr(this, centroids, i)
        points = data[i]
        n = n + len(points)
        print("------------------------------------------------------------------------------------------------------------------")
        print("Current cluster centroid: " + str(this))
        print("Closest other cluster centroid: " + str(other))
        print("------------------------------------------------------------------------------------------------------------------")
        for p in points:
            b = dist(other, p)
            a = dist(this, p)
            s = ((b-a) / max(a,b))
            score = score + s
            print("------------------------------------------------------------------------------------------------------------------")
            print("Distance from point " + str(p) + " to own cluster " + str(this) + ": " + str(a)) 
            print("Distance from " + str(p) + " to other closest cluster " + str(other) + ": " + str(b))
            print("Silhouette score for point " + str(p) + ": " + str(s))
            print("------------------------------------------------------------------------------------------------------------------")
    return score/n

print("Final silhouette coefficient for clustering: " + str(ssc(data)))
print("------------------------------------------------------------------------------------------------------------------")
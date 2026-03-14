class KNN:
    def __init__(self, k=3, distance_metric='euclidean'):
        self.k = k
        self.distance_metric = distance_metric
        self.X_train = None
        self.y_train = None
    
    def __str__(self):
        return "Voici mon KNN"
    
    def _distance_euclidienne(self, x1, x2):
        s = 0
        for i in range(len(x1)):
            s += (x1[i] - x2[i]) ** 2
        return s**(0.5)

    def _distance(self, x1, x2):
        return self._distance_euclidienne(x1, x2)
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        pred = []
        for e in X:
            distance = [(self._distance(e, x_train), y_train) for x_train, y_train in zip(self.X_train, self.y_train)]
            distance.sort(key=lambda x: x[0])
            kn = distance[:self.k]
            D = {}
            for e in kn:
                if e[1] not in D.keys():
                    D[e[1]] = 1
                else:
                    D[e[1]]+=1
            pred.append(max(D))
        return pred   




def stdscal(X, reference_data):
    X_scaled = []
    for i in range(len(X)):
        row = []
        for j in range(len(X[0])):
            col_ref = [row[j] for row in reference_data]
            moyenne = sum(col_ref) / len(col_ref)
            variance = sum((x - moyenne) ** 2 for x in col_ref) / len(col_ref)
            ecart_type = variance ** 0.5
            if ecart_type == 0:
                ecart_type = 1
            row.append((X[i][j] - moyenne) / ecart_type)
        X_scaled.append(row)
    return X_scaled




    
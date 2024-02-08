import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

def train_model(data, target):
    x = np.array(data)
    y = np.array(target)

    imputer = SimpleImputer(strategy='mean')
    x = imputer.fit_transform(x)

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x)

    model = LinearRegression()

    model.fit(x_train_scaled, y)

    return scaler, model
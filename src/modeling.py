from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

def train_model(data):
    X = data[['feature1', 'feature2']]  # Substituir com as features reais
    y = data['target']  # Substituir com a variável alvo
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'MSE: {mse}')

if __name__ == "__main__":
    data = pd.read_csv('../data/clean_energy_consumption.csv')
    train_model(data)

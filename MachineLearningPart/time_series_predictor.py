from pandas import Series
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from math import sqrt
import recommender
# create a differenced series
def difference(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return diff


# invert differenced value
def inverse_difference(history, yhat, interval=1):
    return yhat + history[-interval]


# load data
def predict(item_name):
    index=-1
    curr_stocks=[80,90,50,100,75,82,150,10,16,25]
    for i in range(len(recommender.dictionary)):
        if item_name==recommender.dictionary[i]:
            index=i
            break

    series = Series.from_csv('analyser/mlutils/data/item-' + str(index) + '.csv')
    # prepare data
    X = series.values
    X = X.astype('float32')
    train_size = int(len(X) * 0.50)
    train, test = X[0:train_size], X[train_size:]
    # walk-forward validation
    history = [x for x in train]
    predictions = list()

    interval = 12
    diff = difference(history, interval)
    model = ARIMA(diff, order=(1, 1, 1))
    model_fit = model.fit(trend='nc', disp=0)
    predicted = model_fit.forecast()[0]
    predicted = inverse_difference(history, predicted, interval)
    return int(curr_stocks[index] / predicted)

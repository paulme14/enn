import numpy as np
from IPython.display import IFrame

def embed_lecture_slides(path, width="100%", height="600"):
    lecture_host = "https://www.uni-muenster.de/AISystems/courses/nn_course/"
    #  lecture_host = "http://localhost:8888/OnlineWebsite/"
    return IFrame(f"{lecture_host}{path}", width=width, height=height)

apartment_data = [
    {"size": 50, "price": 450, "rooms": 2, "distance_to_center": 5, "district": "Gievenbeck"},
    {"size": 25, "price": 500, "rooms": 1, "distance_to_center": 3.5, "district": "Sentrup"},
    {"size": 35, "price": 770, "rooms": 1, "distance_to_center": 3, "district": "Wienburg"},
    {"size": 80, "price": 800, "rooms": 3, "distance_to_center": 8, "district": "Nienberge"},
    {"size": 62, "price": 800, "rooms": 2, "distance_to_center": 5, "district": "Coerde"},
    {"size": 70, "price": 820, "rooms": 3, "distance_to_center": 4.5, "district": "Gievenbeck"},
    {"size": 19, "price": 440, "rooms": 1, "distance_to_center": 7, "district": "Nienberge"},
    {"size": 73, "price": 1127, "rooms": 3.5, "distance_to_center": 5, "district": "Wienburg"},
    {"size": 20, "price": 769, "rooms": 1, "distance_to_center": 1, "district": "Zentrum"},
]
sizes = np.array([apt['size'] for apt in apartment_data], dtype=float)
distances = np.array([apt['distance_to_center'] for apt in apartment_data], dtype=float)
prices = np.array([apt['price'] for apt in apartment_data], dtype=float)
rooms = np.array([apt['rooms'] for apt in apartment_data], dtype=float)

def mean_squared_error(y_true, y_pred, verbose=True):
    """
    Calculate the Mean Squared Error between the actual and predicted values.

    Parameters:
    y_true :    array-like
                actual values (ground truth)
    y_pred :    array-like
                predicted values
    """
    # Ensure inputs are 1D numpy arrays
    y_true = np.array(y_true).squeeze()
    y_pred = np.array(y_pred).squeeze()

    mse = ((y_true - y_pred) @ (y_true - y_pred)) / len(y_true)
    if verbose:
        print(f"MSE: {mse: ,.1f}")
    return mse


def plot_1d(ax, x, y, predictions, x_mesh=None, predictions_mesh=None):
    """
    Plot scalar y against scalar x values.

    Parameters:
    ax : matplotlib Axes object
    x : numpy array, shape (n_samples,)
        The independent variable.
    y : numpy array, shape (n_samples,)
        The dependent variable.
    predictions : numpy array, shape (n_samples,)
        The predictions.
    x_mesh : optional, numpy array, shape (n_mesh,)
        Input meshgrid. Enables plotting of smooth prediction curves.
        If None, `x` is used.
    predictions_mesh : optional, numpy array, shape (n_mesh,)
        Predictions meshgrid. Enables plotting of smooth prediction curves.
        If None, `predictions` is used.
    """
    # Ensure dimensions are correct
    x = x.squeeze()
    y = y.squeeze()
    predictions = predictions.squeeze()
    if x_mesh is not None:
        x_mesh = x_mesh.squeeze()
        predictions_mesh = predictions_mesh.squeeze()
    else:
        x_mesh = x
        predictions_mesh = predictions

    sorted_indices = np.argsort(x_mesh)
    ax.plot(x_mesh[sorted_indices], predictions_mesh[sorted_indices], color='red', label='Predicted Values')
    ax.scatter(x, y, color='blue', label='Actual Values')
    for x_val, y_true, y_hat in zip(x, y, predictions):
        ax.plot([x_val, x_val], [y_true, y_hat], color='red', linestyle='--', linewidth=0.8)
    ax.set_xlabel('x values')
    ax.set_ylabel('y values')
    return ax

import numpy as np
from IPython.display import IFrame

def embed_lecture_slides(path, width="100%", height="600"):
    lecture_host = "https://www.uni-muenster.de/AISystems/courses/nn_course/"
    # lecture_host = "http://localhost:8889/OnlineWebsite/"
    return IFrame(f"{lecture_host}{path}", width=width, height=height)

# ======================================================
# Dataset Preparation
# ======================================================

# Define the dataset
data = [
    {"size": 19, "price": 440, "rooms": 1, "distance_to_center": 7, "location": "Nienberge"},
    {"size": 32, "price": 500, "rooms": 1, "distance_to_center": 5.5, "location": "Gremmendorf"},
    {"size": 69, "price": 810, "rooms": 3, "distance_to_center": 5.5, "location": "Münster-Südost"},
    {"size": 60, "price": 900, "rooms": 2, "distance_to_center": 5.5, "location": "Münster-West"},
    {"size": 20, "price": 500, "rooms": 1, "distance_to_center": 1.5, "location": "Hansaviertel"},
    {"size": 18, "price": 660, "rooms": 1, "distance_to_center": 2.5, "location": "Münster Mitte-Nordost"},
    {"size": 52, "price": 790, "rooms": 3, "distance_to_center": 1, "location": "Münster City Center"},
    {"size": 45, "price": 1795, "rooms": 2, "distance_to_center": 1, "location": "Boeselagerstraße"},
    {"size": 50, "price": 1895, "rooms": 2, "distance_to_center": 1, "location": "Julius-Leber-Straße"}
]

# Extract the features (size and distance_to_center) and target (price)
sizes = np.array([apt['size'] for apt in data])                     # Feature 1: size of the apartment
distances = np.array([apt['distance_to_center'] for apt in data])   # Feature 2: distance to city center
prices = np.array([apt['price'] for apt in data])                   # Target variable: price of the apartment
rooms = np.array([apt['rooms'] for apt in data])                    # Target variable: number of rooms in the apartment

# Create the input matrix X with a column of 1s for the intercept
X = np.column_stack((np.ones(sizes.shape[0]), sizes, distances))
Y = np.column_stack((prices, rooms))

DATASET = (X, Y)


# ======================================================
# Utility Functions
# ======================================================

def mean_squared_error(y_true, y_pred):
    """
    Calculate the Mean Squared Error between the actual and predicted values.

    Parameters:
    - y_true: array-like, actual values (ground truth)
    - y_pred: array-like, predicted values

    Returns:
    - mse: float, the mean squared error
    """
    # Ensure inputs are NumPy arrays for element-wise operations
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Calculate the squared differences
    squared_differences = (y_true - y_pred) ** 2
    
    # Return the mean of the squared differences
    mse = np.mean(squared_differences)
    return mse
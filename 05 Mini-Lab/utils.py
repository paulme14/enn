from IPython.display import IFrame
import numpy as np
import pandas as pd

np.random.seed(42)

def embed_lecture_slides(path, width="100%", height="600"):
    lecture_host = "https://www.uni-muenster.de/AISystems/courses/nn_course/"
    # lecture_host = "http://localhost:8889/OnlineWebsite/"
    return IFrame(f"{lecture_host}{path}", width=width, height=height)


def create_real_estate_dataset(n_samples: int = 1000):
    # Generate synthetic but realistic housing data
    cities = np.random.choice(['Münster', 'Osnabrück', 'Hamburg', 'Berlin', 'Frankfurt'], n_samples)
    living_space = np.random.normal(65, 25, n_samples).clip(20, 200)
    rooms = np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.15, 0.35, 0.30, 0.15, 0.05])
    year_built = np.random.randint(1950, 2024, n_samples)
    has_balcony = np.random.choice([True, False], n_samples, p=[0.6, 0.4])
    heating_type = np.random.choice(['gas', 'oil', 'district', 'electric'], n_samples)
    distance_from_center = np.random.exponential(5, n_samples).clip(0.5, 30)  # Distance in km

    # Calculate rent with realistic relationships
    base_rent = (
        8 * living_space +  # Base price per sqm
        50 * rooms +  # Extra for more rooms
        (2023 - year_built) * -0.5 +  # Newer = more expensive
        100 * has_balcony +  # Balcony premium
        -30 * distance_from_center +  # Farther from center = cheaper (negative correlation)
        np.random.normal(0, 100, n_samples)  # Random noise
    ).clip(300, 3000)

    service_charge = base_rent * 0.15 + np.random.normal(0, 30, n_samples)
    total_rent = base_rent + service_charge

    # Introduce some missing values (realistic!)
    living_space_missing = living_space.copy()
    living_space_missing[np.random.choice(n_samples, 20, replace=False)] = np.nan

    service_charge_missing = service_charge.copy()
    missing_service_charge_ids = np.random.choice(n_samples, 15, replace=False)
    service_charge_missing[missing_service_charge_ids] = np.nan

    # Introduce some outliers (data errors!)
    total_rent_outliers = total_rent.copy()
    total_rent_outliers[np.random.choice(n_samples, 10, replace=False)] = np.random.uniform(5000, 10000, 10)
    total_rent_outliers[np.random.choice(n_samples, 6, replace=False)] = np.random.uniform(50, 200, 6)
    
    # Introduce some missing values for total rent, ensuring no overlap with missing service charge
    total_rent_missing = total_rent_outliers.copy()
    available_ids = np.setdiff1d(np.arange(n_samples), missing_service_charge_ids)
    missing_total_rent_ids = np.random.choice(available_ids, 10, replace=False)
    total_rent_missing[missing_total_rent_ids] = np.nan

    # Create DataFrame
    df = pd.DataFrame({
        'city': cities,
        'totalRent': total_rent_missing,
        'baseRent': base_rent,
        'serviceCharge': service_charge_missing,
        'livingSpace': living_space_missing,
        'noRooms': rooms,
        'yearBuilt': year_built,
        'hasBalcony': has_balcony,
        'heatingType': heating_type,
        'distanceFromCenter': distance_from_center
    })

    return df
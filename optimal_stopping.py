import streamlit as st
import random
import math
import pyreadr
import matplotlib.pyplot as plt

# By: Helen Guo
# Replace 'file.rds' with the path to your RDS file
result = pyreadr.read_r('wine_ratings.RDS')
wine_ratings = result[None]

def generate_candidates(distribution_type, num_candidates, **kwargs):
    if distribution_type == 'Wine Ratings Example':
        ratings = kwargs.get('ratings', [])
        return random.sample(ratings, num_candidates)  # Sampling without replacement 
    elif distribution_type == 'Beta':
        alpha = kwargs.get('alpha', 2)
        beta = kwargs.get('beta', 5)
        return [random.betavariate(alpha, beta) for _ in range(num_candidates)]
    elif distribution_type == 'Normal':
        mu = kwargs.get('mu', 0)
        sigma = kwargs.get('sigma', 1)
        return [random.normalvariate(mu, sigma) for _ in range(num_candidates)]
    elif distribution_type == 'Gamma':
        shape = kwargs.get('shape', 2)
        scale = kwargs.get('scale', 1)
        return [random.gammavariate(shape, scale) for _ in range(num_candidates)]
    elif distribution_type == 'Custom':
        custom_values = kwargs.get('custom_values', [])
        random.shuffle(custom_values)  # Shuffle the custom values
        return custom_values
    else:
        raise ValueError("Invalid distribution type")

def secretary_problem(distribution_type, distribution_params, train_fraction, num_trials, num_candidates):
    total_quality = 0
    num_selected = 0
    candidate_values = []  # List to store candidate values for plotting
    for _ in range(num_trials):
        candidates = generate_candidates(distribution_type, num_candidates, **distribution_params)
        candidate_values.extend(candidates)  # Add candidate values to the list
        
        train_candidates = candidates[:int(train_fraction * num_candidates)]
        best_candidate = max(train_candidates)
        for candidate in candidates[int(train_fraction * num_candidates):]:
            if candidate > best_candidate:
                total_quality += candidate
                num_selected += 1
                break  # Break the loop once a candidate is selected
    if num_selected > 0:
        return total_quality / num_selected, candidate_values
    else:
        return candidates[-1], candidate_values  # Return the value of the last candidate if no candidate is selected

def main():
    st.title("Optimal Stopping Problem Simulator")

    st.sidebar.header("Parameters")
    distribution_type = st.sidebar.selectbox("Distribution Type", ['Wine Ratings Example', 'Beta', 'Normal', 'Gamma', 'Custom'])
    if distribution_type == 'Wine Ratings Example':
        distribution_params = {'ratings': wine_ratings['points'].tolist()}
    elif distribution_type == 'Beta':
        alpha = st.sidebar.slider("Alpha", min_value=1, max_value=100, value=2)
        beta = st.sidebar.slider("Beta", min_value=1, max_value=100, value=5)
        distribution_params = {'alpha': alpha, 'beta': beta}
    elif distribution_type == 'Normal':
        mu = st.sidebar.slider("Mu", min_value=-10, max_value=10, value=0)
        sigma = st.sidebar.slider("Sigma", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
        distribution_params = {'mu': mu, 'sigma': sigma}
    elif distribution_type == 'Gamma':
        shape = st.sidebar.slider("Shape", min_value=1, max_value=100, value=2)
        scale = st.sidebar.slider("Scale", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
        distribution_params = {'shape': shape, 'scale': scale}
    elif distribution_type == 'Custom':
        custom_values_input = st.sidebar.text_input("Enter custom values separated by commas")
        if custom_values_input:  # Check if data is entered
            custom_values = [float(value.strip()) for value in custom_values_input.split(',')]
            num_candidates = len(custom_values)  # Get the number of custom values entered
            distribution_params = {'custom_values': custom_values}
        else:
            st.write("# Enter data")
            return  # Exit the function if no data is entered

    train_fraction = st.sidebar.slider("Train Fraction", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    num_trials = st.sidebar.number_input("Number of Trials Averaged Over", min_value=1, value=1000, step=1)

    if distribution_type != 'Custom':  # If not custom, get the number of candidates from the sidebar
        num_candidates = st.sidebar.number_input("Number of Candidates to Select from", min_value=1, value=100, step=1)

    average_quality, candidate_values = secretary_problem(distribution_type, distribution_params, train_fraction, num_trials, num_candidates)

    st.write("## Average score of selected candidate:", average_quality)

    # Plot distribution of candidate values
    st.write("## Distribution of candidate values")
    fig, ax = plt.subplots()
    ax.hist(candidate_values, bins='auto', alpha=0.7, color='blue')
    st.pyplot(fig)

if __name__ == "__main__":
    main()

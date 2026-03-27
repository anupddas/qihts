import numpy as np

# Function to retrieve benchmark functions and their parameters
def get_benchmark_function(func_name):
    """
    Retrieves the benchmark function and its associated parameters based on the function name.

    Args:
    - func_name (str): The name of the benchmark function (e.g., 'F1').

    Returns:
    - tuple: The function, lower bound, upper bound, global optimum cost, and problem dimension.
    """
    if func_name == 'F1':
        return (lambda x: np.sum(x**2, axis=1), -10, 10, 0, 100)  # Sum of squares function for minimization
    elif func_name == 'F2':
        return (lambda x: np.sum(np.abs(x), axis=1), -10, 10, 0, 30)  # Sum of absolute values (Manhattan norm)
    elif func_name == 'F3':
        return (lambda x: np.sum(x**4 - 16*x**2 + 5*x, axis=1), -5, 5, 0, 30)  # Quartic function
    elif func_name == 'F4':
        return (lambda x: np.sum(np.sin(x)**2, axis=1), -5, 5, 0, 2)  # Sinusoidal function
    elif func_name == 'F5':
        return (lambda x: np.sum(np.abs(x) + 10 * np.sin(x), axis=1), -5, 5, 0, 30)  # Sine and absolute value
    elif func_name == 'F6':
        return (lambda x: np.sum(x**2 - 10*np.cos(2*np.pi*x) + 10, axis=1), -5, 5, 0, 2)  # Rosenbrock function
    elif func_name == 'F7':
        return (lambda x: np.sum(np.sin(x)**2 + 0.1*(x**2 - 1)**2, axis=1), -5, 5, 0.737, 30)  # Sine and squared deviations
    elif func_name == 'F8':
        return (lambda x: np.sum(np.exp(x) - x**2, axis=1), -5, 5, 1.535, 10)  # Exponential minus squared
    elif func_name == 'F9':
        return (lambda x: np.sum((x - 1)**2 * (np.sin(x) + np.cos(x)), axis=1), -5, 5, 0, 2)  # Custom function with sine and cosine
    
    if func_name == 'F10':  # Sum Square Function
        return (lambda x: np.sum(np.arange(1, x.shape[1] + 1) * x**2, axis=1), -100, 100, 0, 10)
    if func_name == 'F11':  # Dixon Function
        return (lambda x: (x[:, 0] - 1)**2 + np.sum(np.arange(2, x.shape[1] + 1) * (2 * x[:, 1:]**2 - x[:, 1:] - 1)**2, axis=1), -10, 10, 0, 10)
    if func_name == 'F12':  # Zakharov Function
        return (lambda x: np.sum(x**2, axis=1) + np.sum(0.5 * np.arange(1, x.shape[1] + 1) * x, axis=1)**2 + np.sum(0.5 * np.arange(1, x.shape[1] + 1) * x, axis=1)**4, -5, 5, 0, 30)
    
    else:
        raise ValueError("Unknown function name")  # Error if function name is not recognized

# Chaos function to generate chaotic vectors (e.g., Gaussian distribution)
def chaos(map_no, num_years):
    """
    Generates a chaotic vector based on a specified map.

    Args:
    - map_no (int): The map number (1 for Gaussian chaos).
    - num_years (int): The length of the chaos vector.

    Returns:
    - np.ndarray: A chaotic vector.
    """
    if map_no == 1:  # Gaussian chaos generation
        return np.random.normal(0, 1, num_years)
    else:
        return np.random.uniform(-1, 1, num_years)  # Uniform chaos

# Function to create the initial forest (population) of trees
def create_forest(algorithm_params, problem_params):
    """
    Creates the initial population (forest) of trees with random positions within the search space.

    Args:
    - algorithm_params (dict): The algorithm parameters, including the number of trees.
    - problem_params (dict): The problem parameters, including the variable bounds.

    Returns:
    - np.ndarray: A matrix representing the initial population of trees.
    """
    return np.random.uniform(problem_params['VarMin'], problem_params['VarMax'], (algorithm_params['NumOfTrees'], problem_params['NPar']))

# Growth mechanism simulating quantum-inspired population expansion
def growth(population, problem_params, alpha, year):
    """
    Simulates the quantum-inspired growth of the population in each iteration, with a decreasing growth factor.

    Args:
    - population (np.ndarray): The current population of trees.
    - problem_params (dict): The problem parameters, including variable bounds and cost function.
    - alpha (float): The quantum growth factor.
    - year (int): The current year (iteration) in the algorithm.

    Returns:
    - np.ndarray: The new population after growth and cost evaluation.
    """
    growth_factor = alpha / (year + 1)  # Growth factor decreases with each year
    mutated_population = population[:, :-1] + growth_factor * np.random.uniform(-1, 1, population[:, :-1].shape)
    mutated_population = np.clip(mutated_population, problem_params['VarMin'], problem_params['VarMax'])  # Bound within search space
    return np.hstack((mutated_population, problem_params['CostFuncName'](mutated_population).reshape(-1, 1)))

# Quantum-inspired fruit scattering mechanism for diversity enhancement
def quantum_fruit_scattering(temp, problem_params, best_solution, alpha):
    """
    Simulates a probabilistic scattering mechanism that creates diversity in the population 
    based on the best solution and a scattering range.

    Args:
    - temp (np.ndarray): The temporary population for scattering.
    - problem_params (dict): The problem parameters, including variable bounds and cost function.
    - best_solution (np.ndarray): The best solution found so far in the population.
    - alpha (float): The scattering influence factor.

    Returns:
    - np.ndarray: The scattered population with new solutions and their associated costs.
    """
    phi = np.random.uniform(0, 1)  # Randomly select a blending factor
    scattering_range = alpha * np.random.uniform(0, 1, temp[:, :-1].shape)  # Scattering range based on alpha
    scattered_population = phi * best_solution + (1 - phi) * scattering_range * np.random.uniform(-1, 1, temp[:, :-1].shape)
    scattered_population = np.clip(scattered_population, problem_params['VarMin'], problem_params['VarMax'])  # Bound within search space
    return np.hstack((scattered_population, problem_params['CostFuncName'](scattered_population).reshape(-1, 1)))

# Quantum-inspired root spreading mechanism using chaotic influence
def quantum_root_spreading(temp, problem_params, alpha, chaos_vec, best_solution):
    """
    Simulates a root spreading mechanism with chaotic influence and a probabilistic factor to enhance population diversity.

    Args:
    - temp (np.ndarray): The temporary population for spreading.
    - problem_params (dict): The problem parameters, including variable bounds and cost function.
    - alpha (float): The spreading influence factor.
    - chaos_vec (np.ndarray): The chaos vector used to influence the root spreading.
    - best_solution (np.ndarray): The best solution found so far in the population.

    Returns:
    - np.ndarray: The updated population after root spreading and cost evaluation.
    """
    phi = np.random.uniform(0, 1)  # Randomly select a blending factor
    spread_factor = (alpha * chaos_vec[:temp.shape[0]])[:, np.newaxis] * np.random.uniform(-1, 1, temp[:, :-1].shape)
    root_population = phi * best_solution + (1 - phi) * (temp[:, :-1] + spread_factor)
    root_population = np.clip(root_population, problem_params['VarMin'], problem_params['VarMax'])  # Bound within search space
    return np.hstack((root_population, problem_params['CostFuncName'](root_population).reshape(-1, 1)))

# Main script
problem_params = {
    'CostFuncName': get_benchmark_function('F1')[0],  # Set the cost function to F1 (sum of squares)
    'VarMin': np.array([-5] * 100),  # Lower bounds for the search space
    'VarMax': np.array([5] * 100),    # Upper bounds for the search space
    'NPar': 100                     # Dimensionality of the problem
}

# Algorithm parameters
alpha = 0.2  # Quantum influence factor
alpha_damp = 0.98  # Damping factor for the alpha value
algorithm_params = {
    'NumOfTrees': 100,  # Number of trees (solutions) in the population
    'NumOfYears': 100000  # Number of iterations (years) for the algorithm
}

# Initialize chaos vector based on the specified map number (1 for Gaussian chaos)
chaos_vec_no = 1
chaos_vec = chaos(chaos_vec_no, algorithm_params['NumOfYears'])

# Initialize population of trees (solutions)
initial_trees = create_forest(algorithm_params, problem_params)
initial_cost = problem_params['CostFuncName'](initial_trees)
population = np.hstack((initial_trees, initial_cost.reshape(-1, 1)))  # Add the cost column to the population

# Minimum cost tracking
minimum_cost = np.zeros(algorithm_params['NumOfYears'])

# Main optimization loop
for year in range(algorithm_params['NumOfYears']):
    costs = population[:, -1]
    minimum_cost[year] = np.min(costs)  # Track the minimum cost for this iteration
    best_solution = population[np.argmin(costs), :-1]  # Best solution (tree) in the current population

    # Apply quantum-inspired mechanisms for population improvement
    temp = growth(population, problem_params, alpha, year + 1)
    temp = quantum_fruit_scattering(temp, problem_params, best_solution, alpha)
    temp = quantum_root_spreading(temp, problem_params, alpha, chaos_vec, best_solution)

    # Update population with improved solutions
    for i in range(algorithm_params['NumOfTrees']):
        if temp[i, -1] < population[i, -1]:
            population[i, :] = temp[i, :]

    # Decrease alpha to reduce quantum influence over time
    alpha *= alpha_damp

    # Print progress every 500 iterations
    if (year + 1) % 1000 == 0:
        print(f'Minimum Cost in Iteration {year + 1} is {minimum_cost[year]}')

# Final best solution found
print("Best solution found:", population[np.argmin(population[:, -1])])
print("Best cost:", np.min(population[:, -1]))
import numpy as np

# Function: get_benchmark_function
# Purpose: Returns the benchmark function details based on a specified name.
# - Includes commonly used functions (e.g., sum of squares, quartic, Rosenbrock)
# - Each function is provided with the function formula, bounds, global minimum, and dimension.
def get_benchmark_function(func_name):
    # Benchmark functions for optimization
    if func_name == 'F1':
        return (lambda x: np.sum(x**2, axis=1), -10, 10, 0, 30)  # Sphere function for minimization
    elif func_name == 'F2':
        return (lambda x: np.sum(np.abs(x), axis=1), -10, 10, 0, 30)  # Sum of absolute values (Manhattan norm)
    # Additional benchmark functions, each with unique objective function and bounds
    elif func_name == 'F3':
        return (lambda x: np.sum(x**4 - 16*x**2 + 5*x, axis=1), -5, 5, 0, 30)  # Quartic function
    elif func_name == 'F4':
        return (lambda x: np.sum(np.sin(x)**2, axis=1), -5, 5, 0, 30)  # Sinusoidal function
    elif func_name == 'F5':
        return (lambda x: np.sum(np.abs(x) + 10 * np.sin(x), axis=1), -5, 5, 0, 30)  # Sine and absolute value
    elif func_name == 'F6':
        return (lambda x: np.sum(x**2 - 10*np.cos(2*np.pi*x) + 10, axis=1), -5, 5, 0, 30)  # Rosenbrock function
    elif func_name == 'F7':
        return (lambda x: np.sum(np.sin(x)**2 + 0.1*(x**2 - 1)**2, axis=1), -5, 5, 0, 30)  # Sine and squared deviations
    elif func_name == 'F8':
        return (lambda x: np.sum(np.exp(x) - x**2, axis=1), -5, 5, 0, 30)  # Exponential minus squared
    elif func_name == 'F9':
        return (lambda x: np.sum((x - 1)**2 * (np.sin(x) + np.cos(x)), axis=1), -5, 5, 0, 30)  # Custom function with sine and cosine
    
    if func_name == 'F10':  # Sum Square Function
        return (lambda x: np.sum(np.arange(1, x.shape[1] + 1) * x**2, axis=1), -10, 10, 0, 30)
    if func_name == 'F11':  # Dixon Function
        return (lambda x: (x[:, 0] - 1)**2 + np.sum(np.arange(2, x.shape[1] + 1) * (2 * x[:, 1:]**2 - x[:, 1:] - 1)**2, axis=1), -10, 10, 0, 2)
    if func_name == 'F12':  # Zakharov Function
        return (lambda x: np.sum(x**2, axis=1) + np.sum(0.5 * np.arange(1, x.shape[1] + 1) * x, axis=1)**2 + np.sum(0.5 * np.arange(1, x.shape[1] + 1) * x, axis=1)**4, -5, 5, 0, 30)
    
    else:
        raise ValueError("Unknown function name")  # Error if function name is not recognized

# Function: chaos
# Purpose: Generates a chaotic sequence vector based on the chosen map type.
# - Different maps (e.g., Gaussian or uniform) provide diversity in randomization.
def chaos(map_no, num_years):
    if map_no == 1:  # Gaussian as an example
        return np.random.normal(0, 1, num_years)
    else:
        return np.random.uniform(-1, 1, num_years)

# Function: create_forest
# Purpose: Initializes the population (forest) of trees as potential solutions within the search space.
def create_forest(algorithm_params, problem_params):
    # Initialize population within search space bounds
    return np.random.uniform(problem_params['VarMin'], problem_params['VarMax'], (algorithm_params['NumOfTrees'], problem_params['NPar']))

# Function: growth
# Purpose: Executes the growth phase where solutions (trees) evolve within the bounds, driven by a decreasing growth factor.
# - Mutations of solutions occur with the growth factor to explore the solution space.
def growth(population, problem_params, alpha, year):
    growth_factor = alpha / (year + 1)
    mutated_population = population[:, :-1] + growth_factor * np.random.uniform(-1, 1, population[:, :-1].shape)
    mutated_population = np.clip(mutated_population, problem_params['VarMin'], problem_params['VarMax'])
    return np.hstack((mutated_population, problem_params['CostFuncName'](mutated_population).reshape(-1, 1)))

# Function: fruit_scattering
# Purpose: Generates new solutions around the current best solution, adding small random variations.
def fruit_scattering(temp, problem_params, best_solution, alpha):
    scattering_range = alpha * np.random.rand(*temp[:, :-1].shape)
    scattered_population = best_solution + scattering_range * np.random.uniform(-1, 1, temp[:, :-1].shape)
    scattered_population = np.clip(scattered_population, problem_params['VarMin'], problem_params['VarMax'])
    return np.hstack((scattered_population, problem_params['CostFuncName'](scattered_population).reshape(-1, 1)))

# Function: root_spreading
# Purpose: Applies chaotic influence to spread solutions, promoting exploration and diversification.
def root_spreading(temp, problem_params, alpha, chaos_vec):
    spread_factor = alpha * chaos_vec[:temp.shape[0]]  # Apply chaos vector influence
    spread_population = temp[:, :-1] + spread_factor[:, np.newaxis] * np.random.uniform(-1, 1, temp[:, :-1].shape)
    spread_population = np.clip(spread_population, problem_params['VarMin'], problem_params['VarMax'])
    return np.hstack((spread_population, problem_params['CostFuncName'](spread_population).reshape(-1, 1)))

# Main script
# Purpose: Initializes problem parameters, chaos, and population, then performs iterative search to optimize solutions.

# Set problem parameters
problem_params = {}
problem_params['CostFuncName'] = 'F12'  # Name of cost function to minimize
func_name = problem_params['CostFuncName']

# Retrieve benchmark function properties
fobj, lowerbound, upperbound, global_cost, dimension = get_benchmark_function(func_name)
problem_params['CostFuncName'] = fobj
problem_params['lb'] = lowerbound
problem_params['ub'] = upperbound
problem_params['NPar'] = dimension
problem_params['gcost'] = global_cost

# Define search space and calculate maximum bounds
problem_params['VarMin'] = np.full(problem_params['NPar'], problem_params['lb'])
problem_params['VarMax'] = np.full(problem_params['NPar'], problem_params['ub'])
problem_params['SearchSpaceSize'] = problem_params['VarMax'] - problem_params['VarMin']
problem_params['dmax'] = np.linalg.norm(problem_params['VarMax'] - problem_params['VarMin'])

# Set algorithm parameters
alpha = 0.2
alpha_damp = 0.98
algorithm_params = {
    'NumOfTrees': 100,
    'NumOfYears': 10000
}

# Initialize chaos vectors for diversification
chaos_vec_no = 1  # Chooses a chaotic map
chaos_vec = np.zeros((30, algorithm_params['NumOfYears']))
for i in range(30):
    chaos_vec[i, :] = chaos(i + 1, algorithm_params['NumOfYears'])

# Initialize population and calculate initial costs
initial_trees = create_forest(algorithm_params, problem_params)
initial_cost = problem_params['CostFuncName'](initial_trees)
initial_trees = np.hstack((initial_trees, initial_cost.reshape(-1, 1)))  # Append costs as new column
population = initial_trees

# Main optimization loop
minimum_cost = np.zeros(algorithm_params['NumOfYears'])
for year in range(algorithm_params['NumOfYears']):
    algorithm_params['SeedingRate'] = (0.4) * np.random.rand(1) + 0.1
    algorithm_params['year'] = year + 1  # 1-based indexing

    # Track minimum cost and best solution
    costs = population[:, -1]
    minimum_cost[year] = np.min(costs)
    best_index = np.where(costs == minimum_cost[year])[0][0]
    best_solution = population[best_index, :-1]

    # Apply growth, fruit scattering, and root spreading phases
    temp = growth(population, problem_params, alpha, year + 1)
    temp = fruit_scattering(temp, problem_params, best_solution, alpha)
    temp = root_spreading(temp, problem_params, alpha, chaos_vec[chaos_vec_no, :])

    # Update population with improved solutions
    for i in range(algorithm_params['NumOfTrees']):
        if temp[i, -1] < population[i, -1]:
            population[i, :] = temp[i, :]

    # Gradually decrease alpha for convergence
    alpha *= alpha_damp

    # Update minimum cost for each iteration
    costs = population[:, -1]
    minimum_cost[year] = np.min(costs)
    
    # Print progress at intervals
    if (year + 1) % 500 == 0:
        print(f'Minimum Cost in Iteration {year + 1} is {minimum_cost[year]}')
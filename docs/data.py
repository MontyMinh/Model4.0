class Data:
  
"""
    Attributes:
    -----------
    product_list: list (preprocessing)
        List of products to optimize. Used in 
        - generate_demand_matrix
        - generate_combination_matrices
    factory_list: list (preprocessing)
        List of factories to optimize. Used in:
        - generate_combination_matrices
    factory_sizes: dict (preprocessing)
        Dictionary containing the number of factories for all products. Used in:
        - generate_demand_matrix
    customer_sizes: dict (preprocessing)
        Dictionary containing the number of customer for all products. Used in:
        - generate_demand_matrix
    factory_names: dict (preprocessing)
        Dictionary of factory names for all products. Used in:
        - generate_combination_matrices
    dimF: int (preprocessing)
        Σ|F| (total number of factories across all products). Used in:
        - generate_objective_vector
        - generate_demand_matrix
        - generate_combination_matrices
        - generate_capacity_matrix
        - generate_supply_matrix
        - generate_constraints_matrix
    dimC: int (preprocessing)
        Σ|C| (total number of customers across all products). Used in:
        - generate_objective_vector
        - generate_demand_matrix
        - generate_constraints_matrix
        - generate_constraints_vector
    dimFC: int (preprocessing)
        Σ|FxC| (total number of factories x customers across all products). Used in:
        - generate_objective_vector
        - generate_demand_matrix
        - generate_combination_matrices
        - generate_capacity_matrix
        - generate_supply_matrix
        - generate_demand_matrix
    inbound_cost_per_product: dict (preprocessing)
        Dictionary containing the inbound cost to factories for all products. Used in:
        - generate_objective_vector
    outbound_cost_per_product: dict (preprocessing)
        Dictionary containing the outbound cost to factories for all products. Used in:
        - generate_objective_vector
    objective_vector: numpy.ndarray (output)
        Objective vector to minimize function value. Used in:
        - generate_objective_vector
    demand_matrix: numpy.ndarray (both)
        Demand matrix to realize customers' demand, made by horizontally
        concatenate the inbound and outbound demand matrix. Used in:
        - generate_demand_matrix (output)
        - generate_constraints_matrix (input)
    efficiency_per_product: dict (preprocessing)
        Dictionary of efficiency of all factories for all products. Used in:
        - generate_combination_matrices
    inbound_combination_matrices: dict (both)
        Dictionary of block diagonal matrices containing the production
        efficiency of a factory {product: associated matrix}. Each
        product corresponds to a matrix with:
            - #Columns: ∑|F| (total number of factories across all products)
            - #Rows: # Factories (total number of factories)
        Used in:
        - generate_combination_matrices (output)
        - generate_supply_matrix (input)
    outbound_combination_matrices: dict (both)
        Dictionary of block diagonal matrices to apply outbound constraints
        on a per-factory basis. {product: associated matrix}. Each product
        corresponds to a matrix with:
            - #Column: ∑|FxC| (total number of factories x customers
            across all products)
            - #Rows: # Factories (total
            number of factories)
        Used in:
        - generate_combination_matrices (output)
        - generate_capacity_matrix (input)
        - generate_supply_matrix (input)
    capacity_constraints: list (preprocessing)
        List of capacity constraints for by product combinations. Used in:
        - generate_capacity_matrix
    capacity_matrix: numpy.ndarray (both)
        Capacity matrix to realize the factories' production capacity,
        made by concatenating the inbound and outbound capacity matrix.
        - generate_capacity_matrix (output)
        - generate_constraints_matrix (input)
    capacity_rows: int (both)
        Dimension of the capacity part of the constraints vector,
        calculate by taking the union of all the factories across
        all products. Used in:
        - generate_capacity_matrix (output)
        - generate_constraints_matrix (input)
        - generate_constraints_vector (input)
    supply_constraints: list (preprocessing)
        List of supply constraints for by product combinations. Used in:
        - generate_supply_matrix
    supply_matrix: numpy.ndarray (both)
        Supply matrix to realize the factories' production supply,
        made by concatenating the inbound and outbound supply matrix.
        - generate_supply_matrix (output)
        - generate_constraints_matrix (input)
    supply_rows: int (both)
        Dimension of the supply part of the constraints vector,
        calculate by taking the union of all the factories across
        all products. Used in:
        - generate_supply_matrix (output)
        - generate_constraints_matrix (input)
        - generate_constraints_vector (input)
    demand_volume: numpy.ndarray (preprocessing)
        Vector defining the demand constraints associated with
        the demand matrix.
        #Dimension: Σ|C| (number of customers across all products)
        Used in: 
        - generate_constraints_vector
    capacity_volume: numpy.ndarray (preprocessing)
        Vector defining the capacity constraints associated with
        the capacity matrix
        #Dimension: #cap_rows (calculate by taking the union of all
        the factories across all products)
        Used in:
        - generate_constraints_vector
    constraints_vector: numpy.ndarray (output)
        Vector associated with the constraints matrix, defining
        the constraints for demand, capacity and supply.
        #Dimension: Σ|C| + #cap_rows + #sup_rows (number of rows
        of the constraints matrix)
        Used in:
        - generate_constraints_vector    
    """

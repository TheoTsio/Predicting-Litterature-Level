import itertools
from math import comb

def compute_shapley_values(group_data, metric="F1 Score (Weighted)"):
    """
    Computes the Shapley values for each group based on a specified metric.
    Here we consider that our value is the metric, so the negative shapley value will mean that this group reduces the metric
    and the positive increases. This is why we implemented this function from scratch instead of using the SHAP module.

    Parameters:
    - group_data (dict): A dictionary with keys as group combinations and values as metric scores.
    - metric (str): The metric key to calculate Shapley values for.

    Returns:
    - dict: Shapley values for each group.
    """
    # Extract all individual groups
    all_groups = sorted({g for key in group_data.keys() for g in key.replace("group ", "").split(" + ")})
    
    # Helper function to get the metric score for a subset of groups
    def get_metric_score(subset):
        key = " + ".join(f"group {g}" for g in sorted(subset))
        return group_data.get(key, {metric: 0})[metric]

    # Initialize Shapley values for each group
    shapley_values = {group: 0 for group in all_groups}

    # Calculate Shapley value for each group
    for group in all_groups:
        # Loop over all coalition sizes
        for i in range(len(all_groups)):
            # All subsets (coalitions) of size `i` that do not contain the current group
            for coalition in itertools.combinations([g for g in all_groups if g != group], i):
                coalition_with_group = set(coalition) | {group}
                # Calculate the marginal contribution of adding `group` to `coalition`
                marginal_contribution = get_metric_score(coalition_with_group) - get_metric_score(coalition)
                # Weight the contribution by the size of the coalition
                weight = 1 / (len(all_groups) * comb(len(all_groups) - 1, len(coalition)))
                # Accumulate the weighted contribution to the Shapley value of the group
                shapley_values[group] += weight * marginal_contribution

    return shapley_values
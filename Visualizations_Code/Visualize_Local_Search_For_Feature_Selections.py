import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath('../Results'))

# Provided F1 scores
f1_scores = [
    0.5831, 
    0.5866, 0.6085, 0.5806, 0.6413, 0.6154, 0.5440, 0.5541, 0.5868, 0.5760, 0.5740, 0.5880, 0.5924, 0.6011, 0.5542, 0.5897, 0.5540, 0.5890, 0.5986, 0.6413,
    0.6301, 0.6043, 0.5780, 0.6941, 0.6123, 0.6151, 0.6375, 0.6301, 0.5886, 0.6299, 0.6471, 0.6306, 0.6204, 0.5947, 0.6156, 0.6113, 0.6941,
    0.6726, 0.6709, 0.6869, 0.6812, 0.6372, 0.6997, 0.6875, 0.6512, 0.6846, 0.7090, 0.7195, 0.6538, 0.6869, 0.7031, 0.6641, 0.7195,
    0.6722, 0.6519, 0.6700, 0.6536, 0.6539, 0.6700, 0.6771, 0.6511, 0.6647, 0.6823, 0.6266, 0.6664, 0.6700, 0.6839, 0.6413
]

# Peaks for annotations (only those you want to display)
peaks = {
    "HRS_M": (4, f1_scores[4]),
    "HRS_F": (23, f1_scores[23]),
    "HRSWORK_M": (47, f1_scores[47])
}

# Provided feature combinations
feature_combinations_str = """A
A + URBANITY 
A + NR_CHILDREN 
A + BIRTHORDER 
A + HOURSMOTHER 
A + HOURSFATHER 
A + TOTAL_HLE
A + NRBOOKS 
A + TOTAL_ISBR 
A + EDUCATION_1 
A + EDUCATION_2 
A + WORKSTATUS_1 
A + WORKSTATUS_2
A + hoursworkmother 
A + hoursworkfather 
A + ECONOMIC
A + BIRTHORDER 
A + GESTWEEK
A + SEX
A + HOURSMOTHER
A + HOURSMOTHER + URBANITY 
A + HOURSMOTHER + NR_CHILDREN 
A + HOURSMOTHER + BIRTHORDER 
A + HOURSMOTHER + HOURSFATHER 
A + HOURSMOTHER + TOTAL_HLE
A + HOURSMOTHER + NRBOOKS 
A + HOURSMOTHER + TOTAL_ISBR 
A + HOURSMOTHER + EDUCATION_1 
A + HOURSMOTHER + EDUCATION_2 
A + HOURSMOTHER + WORKSTATUS_1 
A + HOURSMOTHER + WORKSTATUS_2
A + HOURSMOTHER + hoursworkmother 
A + HOURSMOTHER + hoursworkfather 
A + HOURSMOTHER + BIRTHORDER
A + HOURSMOTHER + GESTWEEK
A + HOURSMOTHER + SEX
A + HOURSMOTHER + HOURSFATHER
A + HOURSMOTHER + HOURSFATHER + URBANITY 
A + HOURSMOTHER + HOURSFATHER + NR_CHILDREN 
A + HOURSMOTHER + HOURSFATHER + BIRTHORDER 
A + HOURSMOTHER + HOURSFATHER + TOTAL_HLE
A + HOURSMOTHER + HOURSFATHER + NRBOOKS 
A + HOURSMOTHER + HOURSFATHER + TOTAL_ISBR 
A + HOURSMOTHER + HOURSFATHER + EDUCATION_1 
A + HOURSMOTHER + HOURSFATHER + EDUCATION_2 
A + HOURSMOTHER + HOURSFATHER + WORKSTATUS_1 
A + HOURSMOTHER + HOURSFATHER + WORKSTATUS_2
A + HOURSMOTHER + HOURSFATHER + hoursworkmother
A + HOURSMOTHER + HOURSFATHER + hoursworkfather 
A + HOURSMOTHER + HOURSFATHER + BIRTHORDER
A + HOURSMOTHER + HOURSFATHER + GESTWEEK
A + HOURSMOTHER + HOURSFATHER + SEX
A + HOURSMOTHER + HOURSFATHER + hoursworkmother
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + URBANITY 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + NR_CHILDREN 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + BIRTHORDER 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + TOTAL_HLE
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + NRBOOKS 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + TOTAL_ISBR 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + EDUCATION_1 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + EDUCATION_2 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + WORKSTATUS_1 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + WORKSTATUS_2
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + hoursworkfather 
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + ECONOMIC
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + BIRTHORDER
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + GESTWEEK
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + SEX
A + HOURSMOTHER + HOURSFATHER + hoursworkmother + URBANITY
"""

feature_combinations = feature_combinations_str.split('\n')

# Identify the end indices of each round
round_ends = [19, 36, 52, 67]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(f1_scores, marker='o', linestyle='-', color='#00429d', alpha=0.7, label="F1 Score")
plt.xlabel("Feature Combinations")
plt.ylabel("F1 Score")
plt.title("F1 Scores for Different Feature Combinations")

# Add vertical lines at the end of each round
for end in round_ends:
    plt.axvline(x=end, color='#17becf', linestyle='-', alpha=1)

# Add round labels
round_labels = ["Round 0", "Round 1", "Round 2", "Round 3"]
for i, end in enumerate(round_ends):
    plt.text(end-2.6, 0.54, round_labels[i], color='#333333', ha='center', va='bottom', fontsize=10)

# Annotate only selected peaks
for label, (idx, score) in peaks.items():
    plt.annotate(label, xy=(idx, score), textcoords="offset points", 
                 xytext=(0,9.5), ha='center', fontsize=8, color="#333333", rotation=0)

# Add horizontal lines at the peaks
for label in peaks:
    plt.axhline(y=peaks[label][1], color='purple', linestyle='--', alpha=1)

# Add horizontal lines for best scores
plt.text(x=len(f1_scores)-0.4, y=f1_scores[4] + 0.003, s='Best: Round 0', color='purple')

plt.text(x=len(f1_scores)-0.4, y=f1_scores[23] + 0.003, s='Best: Round 1', color='purple')

plt.text(x=len(f1_scores)-0.4, y=f1_scores[47] + 0.003, s='Best: Round 2', color='purple')


plt.legend()
plt.xticks(range(len(f1_scores)), range(len(f1_scores)), rotation=90, fontsize=10)
plt.tight_layout()
plt.grid(True, linestyle="-", alpha=0.3)

plt.savefig("Results\local_search_result.pdf", format="pdf", bbox_inches="tight")
plt.show()
import pandas as pd

file_path1 = 'path_to_result_of_ERNIE4.0'
file_path2 = 'path_to_result_of_GPT3.5'
file_path3 = 'path_to_result_of_GLM4'

df1 = pd.read_excel(file_path1)
df2 = pd.read_excel(file_path2)
df3 = pd.read_excel(file_path3)

#Individual weights
weights1 = {'Informativeness': 0.368, 'Comprehensibility': 0.372, 'Helpfulness': 0.414, 'Consistency': 0.427, 'Coherence': 0.343, 'Safety': 0.384}
weights2 = {'Informativeness': 0.163, 'Comprehensibility': 0.19, 'Helpfulness': 0.36, 'Consistency': 0.126, 'Coherence': 0.135, 'Safety': 0.257}
weights3 = {'Informativeness': 0.364, 'Comprehensibility': 0.317, 'Helpfulness': 0.385, 'Consistency': 0.313, 'Coherence': 0.265, 'Safety': 0.311}

df1['weighted average score'] = df1[list(weights1.keys())].mul(list(weights1.values())).sum(axis=1)
df2['weighted average score'] = df2[list(weights2.keys())].mul(list(weights2.values())).sum(axis=1)
df3['weighted average score'] = df3[list(weights3.keys())].mul(list(weights3.values())).sum(axis=1)

df_combined = pd.DataFrame()

for aspect in weights1.keys():
    weight_sum = weights1[aspect] + weights2[aspect] + weights3[aspect]
    df_combined[f'{aspect} average_point'] = (df1[aspect]*weights1[aspect] + df2[aspect]*weights2[aspect] + df3[aspect]*weights3[aspect]) / weight_sum

output_file_path = 'path_to_result_of_FEEL'
df_combined.to_excel(output_file_path, index=False)

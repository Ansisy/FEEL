import pandas as pd
from scipy.stats import spearmanr, kendalltau, pearsonr

def load_data(*file_paths):
    dataframes = [pd.read_excel(fp).set_index(pd.read_excel(fp).columns[0]) for fp in file_paths]
    return dataframes

def is_arithmetic_sequence(scores):
    sorted_scores = sorted(scores)
    differences = [sorted_scores[i+1] - sorted_scores[i] for i in range(len(sorted_scores) - 1)]
    return all(diff == differences[0] for diff in differences) and differences[0] == 1


def find_annotator_differences(df1, df2, df3):
    specific_differences = {'Annotator1': {}, 'Annotator2': {}, 'Annotator3': {}}
    for column in df1.columns:
        for index in df1.index:
            score1, score2, score3 = df1.at[index, column], df2.at[index, column], df3.at[index, column]
            scores = [score1, score2, score3]
            diffs = [abs(score1 - score2), abs(score1 - score3), abs(score2 - score3)]

            if all(diff >= 1 for diff in diffs):
                for i in range(3):
                    other_scores = scores[:i] + scores[i+1:]
                    specific_differences[f'Annotator{i+1}'].setdefault(column, []).append((index, other_scores[0], other_scores[1]))

            elif any(diff > 1 for diff in diffs):
                sorted_scores = sorted(scores)
                middle_score = sorted_scores[1]
                diffs_to_middle = [abs(score - middle_score) for score in scores]
                max_diff_index = diffs_to_middle.index(max(diffs_to_middle))
                other_scores = scores[:max_diff_index] + scores[max_diff_index+1:]
                specific_differences[f'Annotator{max_diff_index + 1}'].setdefault(column, []).append(
                    (index, other_scores[0], other_scores[1]))

    return specific_differences




def main():
    file_path_1 = 'Labeled dataset for staff worker 1'
    file_path_2 = 'Labeled dataset for staff worker 3'
    file_path_3 = 'Labeled dataset for staff worker 3'

    df1, df2, df3 = load_data(file_path_1, file_path_2, file_path_3)

    annotator_differences = find_annotator_differences(df1, df2, df3)

    # Print the differences for each annotator
    print("\nAnnotator Differences:")
    for annotator, aspects in annotator_differences.items():
        if annotator != 'ArithmeticSequence':
            print(f"\n{annotator}:")
            for aspect, diffs in aspects.items():
                print(f"{aspect}:")
                for diff in diffs:
                    print(f"{diff[0]}: Other Scores ： {diff[1]}, {diff[2]}")

if __name__ == "__main__":
    main()

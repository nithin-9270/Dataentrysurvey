import pandas as pd
import matplotlib.pyplot as plt

def data_analysis_survey():
    df = pd.read_csv('survey_results.csv')

    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Count of participants by gender
    gender_counts = df['Gender'].value_counts()
    print("\nCount of participants by gender:")
    print(gender_counts)

    # Feedback analysis
    feedback_counts = df['Feedback'].value_counts()
    print("\nFeedback Analysis:")
    print(feedback_counts)

    # Visualization: Bar chart for feedback analysis
    plt.bar(feedback_counts.index, feedback_counts.values)
    plt.title("Feedback Analysis")
    plt.xlabel("Feedback")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    data_analysis_survey()

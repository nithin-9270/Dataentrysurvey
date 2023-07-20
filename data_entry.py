import pandas as pd

def data_entry_survey():
    survey_data = []

    print("Data Entry for Survey Results")
    while True:
        name = input("Enter participant's name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        age = input("Enter participant's age: ")
        gender = input("Enter participant's gender (M/F/O): ")
        feedback = input("Enter participant's feedback: ")

        survey_data.append({'Name': name, 'Age': age, 'Gender': gender, 'Feedback': feedback})

    df = pd.DataFrame(survey_data)
    df.to_csv('survey_results.csv', index=False)

    print("Data entry completed. Survey results saved to 'survey_results.csv'.")

if __name__ == "__main__":
    data_entry_survey()

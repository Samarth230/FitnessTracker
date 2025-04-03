import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_and_clean_data(file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = df.columns.str.strip()

        # Print dataset info for debugging
        print(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns")

        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
def prepare_exercise_fitness_data(df):
    if df is None:
        return None

    # Create a copy to avoid modifying the original
    df_copy = df.copy()

    # Standardize column values by stripping spaces
    for col in ["How often do you exercise?", "How do you describe your current level of fitness ?"]:
        if col in df_copy.columns:
            df_copy[col] = df_copy[col].str.strip()

    # Display unique values before mapping (for debugging)
    print("Unique exercise frequency values:", df_copy["How often do you exercise?"].unique())
    print("Unique fitness level values:", df_copy["How do you describe your current level of fitness ?"].unique())

    # Enhanced mapping for exercise frequency
    exercise_mapping = {
        "Never": 0,
        "1 to 2 times a week": 1,
        "2 to 3 times a week": 1, 
        "3 to 4 times a week": 2,
        "5 to 6 times a week": 3,  
        "5 or more times a week": 3,
        "Everyday": 3
    }

    # Enhanced mapping for fitness levels
    fitness_mapping = {
        "Unfit": 1,
        "Not very good": 2,
        "Average": 2, 
        "Good": 3,
        "Very good": 4,
        "Perfect": 5,  
        "Excellent": 5
    }

    # Apply the mappings using replace to handle slight variations
    df_copy["exercise_frequency"] = df_copy["How often do you exercise?"].replace(exercise_mapping)
    df_copy["fitness_level"] = df_copy["How do you describe your current level of fitness ?"].replace(fitness_mapping)

    # Convert to numeric and handle unexpected values
    df_copy["exercise_frequency"] = pd.to_numeric(df_copy["exercise_frequency"], errors='coerce')
    df_copy["fitness_level"] = pd.to_numeric(df_copy["fitness_level"], errors='coerce')

    # Drop rows with missing values in the mapped columns
    df_cleaned = df_copy.dropna(subset=["exercise_frequency", "fitness_level"])

    # Convert to integer
    df_cleaned["exercise_frequency"] = df_cleaned["exercise_frequency"].astype(int)
    df_cleaned["fitness_level"] = df_cleaned["fitness_level"].astype(int)

    print(f"Cleaned data contains {df_cleaned.shape[0]} rows")

    return df_cleaned

def create_exercise_fitness_boxplot(df_cleaned):
    if df_cleaned is None or df_cleaned.empty:
        print("No data available for visualization")
        return

    plt.figure(figsize=(10, 6))

    # Create boxplot with improved styling
    sns.boxplot(
        x="exercise_frequency",
        y="fitness_level",
        data=df_cleaned,
        palette="Blues"
    )

    # Set custom x-axis labels
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Never", "1-3x/week", "3-4x/week", "5+ times/week"]
    )

    # Set y-axis labels
    plt.yticks(
        ticks=[1, 2, 3, 4, 5],
        labels=["Unfit", "Average", "Good", "Very Good", "Excellent"]
    )

    plt.xlabel("Exercise Frequency", fontsize=12)
    plt.ylabel("Perceived Fitness Level", fontsize=12)
    plt.title("Relationship Between Exercise Frequency and Perceived Fitness Level", fontsize=14)

    # Add grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add mean values as points
    means = df_cleaned.groupby('exercise_frequency')['fitness_level'].mean()
    plt.plot(means.index, means.values, 'ro-', linewidth=2, markersize=8, label='Mean Fitness Level')

    plt.legend()
    plt.tight_layout()
    plt.show()

def create_additional_visualizations(df_cleaned, df_original):
    if df_cleaned is None or df_cleaned.empty:
        print("No data available for visualization")
        return

    # 1. Distribution of fitness levels
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    fitness_counts = df_cleaned['fitness_level'].value_counts().sort_index()
    labels = ["Unfit", "Average", "Good", "Very Good", "Excellent"]
    colors = sns.color_palette("Blues_d", len(fitness_counts))
    plt.pie(fitness_counts, labels=[labels[i-1] for i in fitness_counts.index],
            autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Distribution of Fitness Levels')

    # 2. Distribution of exercise frequency
    plt.subplot(1, 2, 2)
    exercise_counts = df_cleaned['exercise_frequency'].value_counts().sort_index()
    labels = ["Never", "1-3x/week", "3-4x/week", "5+ times/week"]
    colors = sns.color_palette("Greens_d", len(exercise_counts))
    plt.pie(exercise_counts, labels=[labels[i] for i in exercise_counts.index],
            autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Distribution of Exercise Frequency')

    plt.tight_layout()
    plt.show()

    # 3. Correlation between age and fitness level (if age data is available)
    if "Your age " in df_original.columns:
        plt.figure(figsize=(10, 6))
        age_groups = df_original["Your age "].unique()

        # Create a temporary dataframe with age and fitness level
        temp_df = pd.DataFrame({
            'age': df_original["Your age "],
            'fitness_level': df_cleaned['fitness_level']
        })

        sns.boxplot(x='age', y='fitness_level', data=temp_df, palette="viridis")
        plt.title('Fitness Level by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Fitness Level')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """Main function to run the fitness analysis"""
    # Load and clean data
    file_path = "fitness_analysis.csv"
    df = load_and_clean_data(file_path)

    if df is not None:
        # Prepare data for analysis
        df_cleaned = prepare_exercise_fitness_data(df)

        if df_cleaned is not None:
            # Create visualizations
            create_exercise_fitness_boxplot(df_cleaned)
            create_additional_visualizations(df_cleaned, df)

            # Print summary statistics
            print("\nSummary Statistics for Fitness Level by Exercise Frequency:")
            print(df_cleaned.groupby('exercise_frequency')['fitness_level'].describe())

            # Calculate correlation
            correlation = df_cleaned['exercise_frequency'].corr(df_cleaned['fitness_level'])
            print(f"\nCorrelation between Exercise Frequency and Fitness Level: {correlation:.2f}")

if __name__ == "__main__":
    main()

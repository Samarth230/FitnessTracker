# Fitness Analysis Project

## Overview
This project analyzes fitness data to explore the relationship between exercise frequency and perceived fitness levels. It includes data cleaning, visualization, and statistical analysis to understand fitness patterns.

## Features
- Data loading and cleaning from CSV files
- Standardization of exercise frequency and fitness level categories
- Visualization of relationships between exercise habits and fitness perception
- Statistical analysis including correlation calculations
- Age-based fitness level analysis

## Visualizations
The project generates several visualizations:
1. Boxplot showing the relationship between exercise frequency and perceived fitness level
2. Pie charts displaying the distribution of fitness levels and exercise frequencies
3. Age group analysis of fitness levels (when age data is available)

## Technical Details
- **Language**: Python
- **Libraries**:
  - pandas (data manipulation)
  - matplotlib & seaborn (visualization)
  - numpy (numerical operations)

## How to Use
1. Ensure you have Python installed with the required libraries
2. Place your fitness data in a CSV file named "fitness_analysis.csv"
3. Run the script:
   ```
   python fitness_analyser.py
   ```

## Data Format
The script expects a CSV file with the following columns:
- "How often do you exercise?"
- "How do you describe your current level of fitness ?"
- "Your age " (optional for age-based analysis)

## Results
The analysis provides insights into:
- How exercise frequency correlates with perceived fitness levels
- Distribution of fitness levels across the dataset
- Distribution of exercise habits
- Statistical summary of fitness levels by exercise frequency group
- Correlation coefficient between exercise frequency and fitness level

## Future Improvements
- Add more advanced statistical analysis
- Incorporate additional fitness metrics
- Develop predictive models for fitness outcomes
- Create interactive visualizations

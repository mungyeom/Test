# README for Airport Baggage Handling Analysis

This project involves analyzing the baggage handling system at an airport, focusing on two key aspects: the number of bags on conveyor belts and passenger waiting times. The analysis utilizes an Excel file named "Interview task.xlsx" containing two sheets: "2.1. Bags on the belt" and "2.2. Passengers waiting". The objective is to understand the efficiency of baggage handling, identify any bottlenecks, and evaluate the passenger experience in terms of waiting times.

## Installation

Before running the analysis, ensure you have the following Python libraries installed. You can install them using pip:

```bash
pip install pandas matplotlib seaborn numpy
```

- `pandas`: For data manipulation and analysis.
- `matplotlib` and `seaborn`: For creating visualizations.
- `numpy`: For numerical operations.

## Data Overview

The Excel file contains two sheets:

- **2.1. Bags on the belt**: Records the number of bags on each conveyor belt at different times.
- **2.2. Passengers waiting**: Logs the start and end times of passengers waiting for their baggage.

## Analysis Steps

1. **Data Loading**: The Excel sheets are loaded into pandas DataFrames for analysis.

    ```python
    bags_on_belts_df = pd.read_excel(file_path, '2.1. Bags on the belt')
    passengers_waiting_df = pd.read_excel(file_path, '2.2. Passengers waiting')
    ```

2. **Data Exploration**: Initial exploration to understand the structure and content of the data.

    ```python
    bags_on_belts_df.head(), passengers_waiting_df.head()
    ```

3. **Bags on Belts Analysis**: Analyze the instances when conveyor belts are at full capacity, taking into account the specific capacities of each belt.

    ```python
    full_capacity_instances = bags_on_belts_df[bags_on_belts_df.apply(lambda row: row['Bags'] >= belt_capacities[row['Processor']], axis=1)]
    ```

4. **Passenger Waiting Time Analysis**: Calculate the waiting times for passengers and identify peak times with the maximum number of waiting passengers.

    ```python
    passengers_waiting_df['Waiting Time'] = passengers_waiting_df.apply(
        lambda row: calculate_time_difference(row['Start Time'], row['End Time']), axis=1)
    ```

5. **Visualization**: Generate plots to visualize the data, including the distribution of bags on belts, instances of full capacity, and passenger waiting times.

    ```python
    plt.hist(passengers_waiting_df['Waiting Time'], bins=30)
    ```

## Results

The analysis provides insights into the efficiency of the baggage handling system and the passenger experience at the airport. Key findings include:

- The specific times when each conveyor belt reaches full capacity.
- The peak times for passenger waiting, highlighting potential bottlenecks in the baggage handling process.
- The distribution of passenger waiting times and the percentage of passengers who waited within the IATA standard of 15 minutes.

## Conclusion

This project highlights areas for potential improvement in the airport's baggage handling system, with the aim of enhancing the overall efficiency and passenger experience. Further analysis could explore the correlation between the number of bags on belts and passenger waiting times, and assess the impact of various factors such as flight delays or operational inefficiencies.

## Contributing

Contributions to improve the analysis or extend the scope are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-source and available under the MIT License.
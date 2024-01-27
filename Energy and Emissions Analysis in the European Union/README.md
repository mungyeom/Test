# README for Energy and Emissions Analysis in the European Union

This repository contains a Python-based analysis of energy consumption, carbon dioxide emissions, and the use of various energy sources in the European Union (EU) from 1982 to 2022. The analysis focuses on trends in the consumption of coal, gas, nuclear, oil, and renewable energy sources, as well as the implications for carbon dioxide emissions.

## Data Sources

The data used in this analysis comes from several CSV files:

- `Statistical Review of World Energy Data.csv`: Contains energy consumption data.
- `Carbon Dioxide Emissions from Energy.csv`: Contains data on carbon dioxide emissions from energy consumption.
- `Oil Consumption.csv`, `Coal_consumption.csv`, `gas_consumption.csv`, `nuclear_consumption.csv`, `renewable_consumption.csv`, `solar.csv`, `wind.csv`, `geothermal_biomass_other.csv`: Each file contains data on the consumption of the respective energy source in the EU.

## Installation

To run the analysis, ensure you have Python installed on your system along with the following packages:

- `pandas`: For data manipulation and analysis.
- `matplotlib`: For creating static, interactive, and animated visualizations in Python.
- `seaborn`: For making statistical graphics in Python.
- `numpy`: For support to large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

You can install these packages using pip:

```bash
pip install pandas matplotlib seaborn numpy
```

## Analysis Overview

The analysis includes:

- **Energy Consumption Trends**: Examines the overall energy consumption in the EU over the years, highlighting trends in different energy sources.
- **Carbon Dioxide Emissions**: Analyzes the carbon dioxide emissions resulting from energy consumption, indicating environmental impacts.
- **Renewable Energy Growth**: Focuses on the growth of renewable energy consumption, including solar and wind energy, compared to traditional energy sources.
- **Energy Source Comparison**: Compares the use of coal, gas, nuclear, and oil over the years, showing shifts in energy preferences.
- **Visualizations**: Includes time-series plots and pie charts to illustrate trends and compositions of energy consumption and emissions.

## Key Findings

The analysis reveals significant trends and data points, such as:

- The shift towards renewable energy sources in the EU, with notable increases in solar and wind energy consumption.
- Changes in carbon dioxide emissions corresponding to shifts in energy consumption patterns.
- The comparison between energy consumption in 1982 and 2022, showing the EU's progress in energy diversification and sustainability.

## Usage

To replicate the analysis:

1. Clone the repository or download the Python script and CSV files.
2. Ensure all the required packages are installed.
3. Run the Python script. The script will read the data from the CSV files, perform the analysis, and generate plots to visualize the findings.

## Contributing

Contributions to this analysis are welcome. Suggestions for additional data sources, analysis methods, or visualizations to enhance the insights are appreciated.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

This analysis is made possible by the availability of public data on energy consumption and emissions. Acknowledgement goes to the organizations and entities that collect and make such data accessible.
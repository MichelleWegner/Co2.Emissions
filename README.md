# CO2 Emissions, Temperature, and Population Analysis

## Topic and reason for selection
We chose the topic of CO2 emissions and their correlation with temperature and population because it is crucial for understanding climate change and its global impact. This topic is particularly relevant as it addresses both environmental and socio-economic issues, providing insights into global disparities and potential policy actions.
We worked with earth's average temperature, unlike daily local readings, which reflects the planet's overall climate health. This single value, encompassing land and sea, acts as a vital sign for our planet. Even slight increases can significantly impact weather, precipitation, and ecosystems globally. While local temperatures show variations across the day and seasons, the Earth's average temperature tracks long-term trends, crucial for understanding climate change.


## Project Structure
The project is organized into the following directories:
- **Clean Data**: Contains the cleaned and processed data files.
- **Raw Data**: Contains the original, unprocessed data files available for download from the internet.
- **Notebooks**: Contains Jupyter notebooks used for data analysis and visualization, where we did most of our work.


## Original Dataset and Hypotheses
### Original Dataset
Our dataset includes global CO2 emission data, earth temperature, and population statistics for various countries over 20 years, from 1999 to 2019. This allows us to analyze trends over time.

### Hypotheses
1. Countries in the Global North produce more CO2 emissions.
2. Countries that produce the most CO2 emissions are the least impacted by the effects by temperature raise.
3. Global temperature rise is strongly correlated with the increase in CO2 emissions over the past century.

#### Data Cleaning
- **Missing Values**: Filled missing values using interpolation or mean substitution.
- **Inconsistent Formats**: Standardized units for CO2 emissions and temperature.
- **Outliers**: Identified and managed outliers using statistical methods like z-scores.

#### Data Integration
- Merged datasets based on country names and years to create a unified dataset.
- Ensured consistency in country names and timeframes across datasets.

#### Analysis
- **Descriptive Statistics**: Calculated averages, medians, and standard deviations for CO2 emissions, temperature changes, and population.
- **Comparative Analysis**: Compared CO2 emissions and temperature changes between the Global North and Global South.
- **Correlation Analysis**: Examined relationships between CO2 emissions and temperature changes.

## Unique Data Cleaning Techniques
### Unique Techniques
#### Geospatial Aggregation
- Classified countries into Global North and Global South based on geographic and socio-economic criteria.
- Aggregated data at regional levels for comparative analysis.

#### Data Normalization
- Normalized CO2 emissions and temperature data to account for population differences, allowing fair comparisons between countries of different sizes.

## Results and Conclusions
### Hypothesis 1
- **Analysis**: The bar plot showing average CO2 emissions by region indicates higher emissions in the Global North compared to the Global South.
- **Conclusion**: The analysis supports Hypothesis 1, confirming that countries in the Global North produce more CO2 emissions on average.

### Hypothesis 2
- **Analysis**: Comparison of temperature changes in top CO2 emitters revealed varied impacts, with some high emitters experiencing significant temperature rises.
- **Conclusion**: The results provide partial support for Hypothesis 2, suggesting that while some top emitters are less impacted by temperature rise, others are not, indicating a more complex relationship.


## How to Use
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/michelle30303/third.project.git
   cd third.project
   
# Navigate the Directories:

Raw Data: Explore the original datasets.

Clean Data: Access the cleaned and processed datasets.

Notebooks: Open and run Visual Studio Code for analysis and visualizations.

Contributing
We welcome contributions from the community.

License
This project currently does not have a specific license.

### Authors and Acknowledgements

# Authors: Mustafa Aldabbas, Daniela Trujillo, Michelle Wegner


# Acknowledgements: A huge thank you to our entire team for their excellent collaboration and hard work on this project.

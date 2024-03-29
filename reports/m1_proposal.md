## 1. Motivation and purpose

### Our role: 
A team of UNEP (UN Environment Programme) officers and Intergovernmental Panel on Climate Change (IPCC) officers who want to raise awareness about CO2 emissions.

### Target audience: 
The general public with an interest in the environment.

### The problem the target audience is facing and how important it is:
The target audience faces the problem of increasing CO2 emissions, leading to climate change, air pollution, ocean pollution, health problem issues and lastly social-economic impacts. It's crucial to solve this issue to protect the environment, human health, and ensure a sustainable future for all.

### How our dashboard assist in solving this problem:
Our Global CO2 Emissions Tracker can give our target audience overview by providing time-series information on global CO2 emissions, sources and trends. This dashboard will help individuals to understand and feel the magnitude of this problem. They can track progress and be informed and can use it to assist on making decisions about personal and collective actions to reduce emissions. The CO2 data dashboard helps people understand CO2 emissions better by showing information in an easy-to-understand way. This makes people more aware of the problem, encourages them to take responsibility, and gets them involved in finding solutions to reduce CO2 emissions.


## 2. Description of the data
In our proposal, we will leverage a robust dataset focusing on carbon dioxide (CO2) emissions data from various countries and regions. Our dataset contains 239 rows and, after omitting the "Indicator Name" and "Indicator Code" columns, we will utilize 33 columns which consist of the 'Country Name', 'Country Code', and annual CO2 emissions data spanning from 1990 to 2020.

This data will be helpful to achieve our goal of creating an interactive dashboard to visualize CO2 emissions worldwide. By interacting with this dataset, our target audience, such as environmental policymakers, researchers, and educators, will be able to recognize patterns, trends, and outliers in emissions. Hopefully this can help them making decisions and strategies to mitigate climate change.

To enhance the utility of our visualizations, we will engineer new variables that include:

**Continent:** Assigning countries to their respective continents for regional analysis.
**Average Emissions:** Calculating the average emissions per year for all countries to identify global trends.
**Standard Deviation:** Providing insights into the year-by-year variability of emissions among countries.
**Maximum and Minimum Emissions:** Highlighting the highest and lowest CO2 emitting countries annually to pinpoint specific areas for policy intervention.
**Total Emission:** Summing up the emissions over a selected time period to understand the cumulative impact and guide long-term environmental planning.

Mean carbon emission trend plot:
<img src="../img/global_mean_emissions.png">

Top10 country in carbon emission:
<img src="../img/top_emitters_bar.png">

These engineered variables will enrich our analysis, enabling us to create more insightful and impactful visualizations. By examining the distribution, trends, and outliers in carbon emissions, we aim to provide valuable insights that can help our target audience in their efforts to address climate change.

## 3. Research questions

## 4. App sketch and description
The dashboard of the Global CO2 Emission Tracker is composed of five components, designed to enrich user engagement and understanding. On the left, users are greeted with intuitive controls that allow for customization of data, including the selection of the specific range of years, countries, and continents of interest to CO2 emissions. Central to the dashboard is a dynamic map that highlights the chosen continents or countries, offering a visual representation of the user’s focus. Below this, a line chart unfolds the historical narrative of CO2 emission through a time series analysis, illustrating the trend of emissions by year. To the right, a pie chart offers perspectives on the selected region’s CO2 emissions, placed within the global context to underscore its relative impact. On the bottom right, there is a bar chart that displays the five highest CO2-emitting countries or regions within the same continent as the selected area. This chart provides a clear comparison of the total CO2 emissions, helping users understand how the selected country or region ranks among its continental peers.

<img src="https://github.com/UBC-MDS/DSCI-532_2024_17_carbon-emissions/blob/App_sketch/img/dashboard.png?raw=true">

# The Global CO2 Emissions Tracker: Visualizing Carbon Footprints Worldwide

***Transform Our World: Raise CO2 Emission Awareness to Spark Positive Action.***

[![GitHub issues](https://img.shields.io/github/issues/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker)](https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker/issues/41) [![release](https://img.shields.io/github/release-date/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker)] ![version](https://img.shields.io/github/v/release/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/) [![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)


## Welcome!

Welcome to The Global CO2 Emissions Tracker Dashboard!! :tada: :tada: :tada:

Thank you for stopping by The Global CO2 Emissions Tracker project repository. 

This document (README.md) serves as your guide to understanding the project and its components. 

Feel free to explore the sections below to learn more about the project and its objectives.


## Table of Contents

- [About](#about)
- [Dashboard Purpose](#dashboard-purpose)
- [Dashboard Link and Demo](#dashboard-link-and-demo)
- [Dashboard Features](#dashboard-features)
- [How to Locally Running the Dashboard](#how-to-locally-running-the-dashboard)
- [How to Contribute](#how-to-contribute)
- [Contributors](#contributors)
- [License](#license)
- [References](#references)


## About

**The Global CO2 Emission Tracker Dashboard** is an interactive platform designed to visualize and analyze carbon emissions data on a global scale. With the growing concern over climate change and its impact on the environment, understanding and tracking CO2 emissions is crucial for policymakers, researchers, and the general public.

This dashboard aims to provide accessible and informative visualizations that shed light on the patterns and trends of CO2 emissions worldwide. By offering filtering options, comparison tools, and up-to-date data sources, users can delve into the complexities of carbon footprints across different regions and countries.

Whether you're a student researching environmental issues, a policymaker crafting regulations to reduce emissions, or a concerned citizen seeking to understand the carbon impact of various activities, this dashboard serves as a valuable resource for exploring and gaining insights into global CO2 emissions data.

Join us in our mission to raise awareness and promote informed decision-making towards a more sustainable future for our planet. Together, we can work towards mitigating climate change and preserving the health of our environment for generations to come.


## Dashboard Purpose:

The Global CO2 Emissions Tracker dashboard has created as a tool that's main goal is for raising public awareness and to help people understand global CO2 emissions better. It collects data from different countries and shows it in simple charts and graphs. This helps to see which countries emit more CO2 and how it affects the environment. By making this information easy to understand, the dashboard helps everyone, including ordinary people, leaders, and organizations, to make smarter choices. It encourages people to take action to reduce their carbon footprint and fight climate change. With its easy-to-use features, the dashboard encourages people to get involved and work together for a cleaner, greener future.


## Dashboard Link and Demo

Deployed dashboard in [render.com](https://render.com): Explore the dashboard here: [Global CO2 Emissions Tracker Dashboard](https://dsci-532-2024-17-global-co2-emissions.onrender.com/)

![Dashboard Demo](https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker/blob/main/img/demo.gif)


## Dashboard Features

***Dashboard visualizing the Global CO2 Emissions Data.***

**Features include:**

- **Data Range Slider:** Adjust the data range from 1990 to 2020 with adjustments in 5-year intervals. This slider provides flexibility in analyzing CO2 emissions trends over specific time periods.

- **Global Map View:** Spot CO2 Emission from the selected countries with hovering data and compare with color's shade on the world map.

- **Line Trend Graph:** Visualize the trajectory of CO2 emissions of selected countries over time using an interactive line graph. Track fluctuations, control data range via slider, identify patterns, and gain insights into long-term trends.

- **Pie Chart for regional CO2 Emissions:** View CO2 emissions from selected regions represented in a pie chart format. The chart displays the top 5 emitting regions individually, while aggregating the remaining emissions into an "Others" category for clearer visualization.

- **Bar Chart for regional CO2 Emissions:** View CO2 emissions from selected regions represented in a bar chart format. The chart displays the top 5 emitting regions individually.


## How to Locally Running the Dashboard

To run the dashboard locally, follow these steps:

1. Clone the repository: You can do this by using the `git clone` command followed by the repository URL. For example:

   ```
   git clone https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker.git
   ```
2. Navigate to the project directory: Use the `cd` command to change your current directory to the project directory. For example:

   ```
   cd DSCI-532_2024_17_Global-CO2-Emissions-Tracker
   ```

3. Create Conda environment from environment.yaml: You'll use the `conda env create` command to create a Conda environment based on the specifications in the `environment.yaml` file.

   ```
   conda env create -f environment.yaml
   ```

   This command will read the dependencies specified in `environment.yaml` and install them into a new Conda environment.

4. Activate the Conda environment: Once the environment is created, activate it using the following command:

   ```
   conda activate co2_emission
   ```

5. Navigate to the src folder: Use `cd` to navigate into the `src` folder.

   ```
   cd src
   ```

6. Run the app.py file: Finally, execute the `app.py` file to run the application.

   ```
   python app.py
   ```

   This command will run the Python script `app.py` located in the `src` folder.

7. Please utilize the provided URL to access the dashboard. The URL follows this format: http://127.0.0.1:8050/


## How to Contribute:

If you believe you can lend a hand in any of the mentioned areas (and we have faith you can), or perhaps even in unexplored territories (we're confident you can surprise us), we encourage you to delve into our [`CONTRIBUTING guidelines`](https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker/blob/main/CONTRIBUTING.md) and feel free to jump in and share your ideas, propose new features, or discuss any aspect of the project you're interested in contributing to in this ['Open Issue for Contributions'](https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker/issues/41).

Maintaining a nurturing and encouraging atmosphere for all participants is paramount to us. We kindly request that you adhere to our [Code of Conduct](https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker/blob/main/CODE_OF_CONDUCT.md), ensuring positive interactions both online and offline.

Your involvement is not only valued but essential to our collective success. Let's embark on this journey together!


## Contributors: 

The Global CO2 Emissions Tracker dashboard has created by 
* Kittipong Wongwipasamitkun (Jo) - @jokittipong
* Jing Wen - @Jing-19
* Yili Tang - @tangyl92
* Hancheng Qin - @hchqin


## License:

`Global-CO2-Emissions-Tracker` is licensed under the terms of the MIT license for software code part including source code examples in the documentation and it is licensed under the terms of the Attribution-NonCommercial 4.0 International (CC BY-NC 4.0), for Parts Other than the Software Code (Package Documentation, Data, Text, and any Media). See [`LICENSE`](https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker/blob/main/LICENSE).


## References:

1. Dataset Reference: World Bank. (n.d.). CO2 emissions (metric tons per capita) Data 1990-2020. Retrieved from https://data.worldbank.org/indicator/EN.ATM.CO2E.PC
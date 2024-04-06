## Dashboard implementation
All features outlined in the 'App Sketch and Description' section of the proposal have been implemented. These include:
**Three controlers:** Year, Country, Region.
**Four charts:** Emission Map, Time-Series Line Chart, Emission Percentage Pie Chart, and Top Emission Countries Bar Chart.

Additionally, the audience can hover over the selected country on the map to see different statistics of the country's emission data.

## Implementation differences
The dashboard layout has been restructured to help the audience navigate through it more effectively. The dashboard currently has a two-column layout.
In the left column, the audience can select countries and years to retrieve corresponding emission data. The Emission Map will provide a comparison of the emission data with the nearest data, and from the Time-Series Line Chart, the emission data history for the selected countries will be provided. In the right column, the audience can select a region to see the current top emitters and the emission breakdown within the selected region.

The layout is different from the original proposition because the previous layout could be confusing for audiences. Not all controllers affect the four charts, and it will be more explicit to showcase which controllers can modify which graph.

## Merit and limitation
With the current structure, audiences can easily compare emission data among countries of interest or see the top emission countries within a particular region. The two-column layout divides the dashboard into two sections, ensuring audiences are not overwhelmed by the number of controllers and charts.

However, there are some limitations. For instance, the current color palette of the dashboard is not very appealing. We also plan to make a few modifications to improve the user-friendly design. Feedback from peer reviews will be considered in the following milestones.
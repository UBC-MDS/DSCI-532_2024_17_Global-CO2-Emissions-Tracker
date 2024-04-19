## Milestone 4 Reflection

### Dashboard modification

**Map country selection**: Based on feedback, we introduced a feature that allows country selection on the map in this release. Currently, the audience can select a country from the map and see the country's name, emission statistics, and its emission history on the line chart. After selecting a country, either from the drop-down list or by clicking, users can click the country again to deselect it.

**Showing all countries as defalut**: The 'select all countries' checkbox has been removed based on feedback. Instead, the current dashboard displays emission data for all countries by default. If audiences want to focus on specific countries, they can select the countries on the map or from the dropdown list. We believe this makes the map less confusing for users.

**Pie chart and bar chart color alignment**: Colors have been adjusted for the pie chart and bar chart. Now, the same country has the same color in both charts, allowing for easy comparison between the two visualizations.

**Other updates**: Some minor updates have also been implemented in Milestone 4, such as the line chart displaying a 'please select a country' notice when first launching the dashboard. There are also several updates to enhance the dashboard's performance, including using caching when calling functions and using a Parquet data file, among others.

### Limitations
Due to difficulties in synchronizing inputs from the country dropdown list and map selection, the emission map currently allows only for single country selection. We have tried various solutions to address this issue, but none have been successful. For selecting multiple countries, audiences can use the dropdown list and can use the map to deselect any countries.

## Overall reflection
After completing four milestones, we've come to believe that the most important aspect of a dashboard is its storytelling capability, rather than just the graphical visualizations. The dashboard needs to guide audiences on how to read it; otherwise, they will get lost among the different visualizations. It is also crucial to include guidance on where to start reading the dashboard and what order they should follow.

We also realized the limitations of using Dash in developing the dashboard. The styling options are limited, and further modifications require direct CSS changes.
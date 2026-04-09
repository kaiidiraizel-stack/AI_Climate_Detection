## AI Climate Change Detection & Forecasting## Project Overview
This project demonstrates how Artificial Intelligence can be used to analyze environmental data. Using Linear Regression, the model identifies long-term temperature trends from 1900 to the present and generates a predictive forecast for the next 50 years. It also visualizes the statistical shift in climate patterns to show the increasing frequency of extreme heat.
## Features

* Trend Detection: Uses Scikit-Learn to find the "line of best fit" through messy historical data.
* Predictive Modeling: Forecasts global temperature anomalies up to the year 2075.
* Statistical Analysis: A distribution plot (KDE) comparing the early 20th century to modern times to visualize the "Climate Shift."

## Built With

* Python 3
* Scikit-Learn: For the Linear Regression AI model.
* Matplotlib: For the primary trend visualization.
* Seaborn: For advanced statistical data distribution.
* NumPy: For mathematical array processing.

##  Installation & Usage

   1. Install the required modules:
   
   pip install matplotlib scikit-learn seaborn numpy
   
   2. Run the script:
   
   python Climate_Trend_Analysis_AI.py
   
   
## Results Explained

* Graph 1 (Trend): Shows a clear upward trajectory in temperatures. The dashed line represents the AI’s prediction of future warming.
* Graph 2 (Distribution): Shows that "normal" temperatures have shifted significantly to the right (warmer) compared to 100 years ago, making extreme heat more common.




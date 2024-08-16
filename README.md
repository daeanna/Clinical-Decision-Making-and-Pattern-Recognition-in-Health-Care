# Clinical Decision Making and Pattern Recognition in Health Care

This repository contains a project focused on clinical decision making and pattern recognition in health care. The project includes a written report and a hackathon proof of concept demonstrating the use of machine learning techniques to analyze health data.

Video Presentation: https://drive.google.com/file/d/1cEcpd1DjkmTyxadJQmbGP5CbHhs-GilW/view?usp=drive_link
POC Video Presentation: https://drive.google.com/file/d/1ppDwyZhJUgth0v_rTAxDNJ-F1MydML7I/view?usp=drive_link
## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Analysis](#data-analysis)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project explores the use of chain reasoning, agentic generative AI, classification, prediction, inference, clustering, and time-series anomaly detection for treatment, payment, and operations (TPO) in health care. The goal is to improve patient outcomes, enhance operational efficiency, and reduce costs through advanced data analysis techniques.

## Project Structure
- `data/`: Contains the simulated health data used for analysis.
- `notebooks/`: Jupyter notebooks with detailed analysis and visualizations.
- `scripts/`: Python scripts for data processing and model training.
- `report/`: The written report in Microsoft Word format.
- `README.md`: This file.

## Installation
To run the code in this repository, you need to have Python installed. You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/healthcare-decision-making.git
   cd healthcare-decision-making
   ```

2. Run the data analysis script:
   ```bash
   python scripts/data_analysis.py
   ```

3. Open the Jupyter notebooks to explore the analysis and visualizations:
   ```bash
   jupyter notebook notebooks/
   ```

## Data Analysis
The data analysis includes:
- Simulating health data for heart rate, steps taken, and body temperature.
- Analyzing trends and detecting anomalies in the data.
- Visualizing the relationships between different health metrics.
- Building a linear regression model to predict heart rate based on steps taken and body temperature.

## Results
The results of the analysis are presented in the form of visualizations and a predictive model. Key findings include:
- Average heart rate, steps taken, and body temperature over the simulated period.
- Detection of anomalies in heart rate data.
- Visualization of the relationship between heart rate and other health metrics.
- Comparison of actual vs. predicted heart rate using the linear regression model.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.


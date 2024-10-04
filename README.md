## Cobblestone Project


# Efficient Data Stream Anomaly Detection

## Project Overview

**Efficient Data Stream Anomaly Detection** is a Python-based project designed to detect anomalies in continuous data streams in real-time. This project simulates a real-time data stream, processes each data point on-the-fly, and identifies unusual patterns such as sudden spikes or deviations from the norm. It adapts to concept drift and seasonal variations, ensuring robust and accurate anomaly detection over time.

## Objectives

1. **Algorithm Selection:**  
   Implement a moving window Z-score algorithm capable of adapting to concept drift and seasonal variations.

2. **Data Stream Simulation:**  
   Design a function to emulate a data stream with regular patterns, seasonal elements, and random noise.

3. **Anomaly Detection:**  
   Develop a real-time mechanism to accurately flag anomalies as the data is streamed.

4. **Optimization:**  
   Ensure the algorithm is optimized for both speed and efficiency using appropriate data structures and methods.

5. **Visualization:**  
   Create a straightforward real-time visualization tool to display both the data stream and any detected anomalies.

## Features

- **Real-Time Processing:**  
  Processes data points one at a time, allowing immediate detection of anomalies.

- **Adaptive Algorithm:**  
  Utilizes a moving window approach to adapt to changes in data patterns (concept drift) and seasonal variations.

- **Efficient Data Handling:**  
  Employs `deque` for efficient management of the moving window.

- **Live Visualization:**  
  Provides a dynamic plot that updates in real-time, highlighting detected anomalies.

- **CLI Output:**  
  Displays live data point values in the command line, indicating whether each point is normal or an anomaly.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- `pip` package manager.

### Steps

1. **Clone the Repository:**  
   Clone this repository to your local machine or download the script directly.

2. **Navigate to the Project Directory:**  
   ```bash
   cd path_to_project_directory
   ```

3. **Create a Virtual Environment (Optional but Recommended):**  
   ```bash
   python3 -m venv venv
   ```
   Activate the virtual environment:
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script:**  
   Execute the Python script using the following command:
   ```bash
   python app.py
   ```

2. **Observe the Output:**  
   - **CLI:**  
     The command line will display each data point as it's processed, indicating whether it's normal or an anomaly. Anomalies will be highlighted in red.
   - **Visualization:**  
     A real-time plot will appear, showing the data stream with anomalies marked in red.

## Algorithm Explanation

### Moving Window Z-Score Method

The anomaly detection algorithm implemented in this project is based on the **Z-score** method enhanced with a **moving window** approach. Here's how it works:

1. **Moving Window:**  
   A fixed-size window (e.g., 50 data points) maintains the most recent data points. This allows the algorithm to adapt to changes in the data over time, handling concept drift effectively.

2. **Z-Score Calculation:**  
   For each new data point, the algorithm calculates the Z-score, which measures how many standard deviations the point is away from the mean of the data in the moving window.

3. **Anomaly Detection:**  
   If the absolute Z-score of a data point exceeds a predefined threshold (e.g., 2.5), the point is flagged as an anomaly.

**Effectiveness:**  
This method is simple yet effective for real-time anomaly detection in streaming data. The moving window ensures that the statistical parameters (mean and standard deviation) remain relevant to the most recent data, allowing the algorithm to adapt to trends and seasonal changes. This adaptability makes it suitable for environments where data patterns evolve over time.

## Error Handling and Data Validation

- **Input Validation:**  
  The `AnomalyDetector` class includes checks to ensure that the threshold is numeric and the window size is a positive integer. Similarly, data points are validated to be numeric before processing.

- **Exception Handling:**  
  The main function wraps the execution in a try-except block to catch and display any unexpected errors gracefully.

## Optimization

- **Efficient Data Structures:**  
  The use of `deque` with a fixed maximum length ensures that adding and removing data points from the moving window is done efficiently, maintaining optimal performance even with large data streams.

- **Minimal External Dependencies:**  
  The project relies only on essential libraries (`numpy` and `matplotlib`), reducing overhead and potential compatibility issues.

## Limitations and Future Improvements

- **Threshold Sensitivity:**  
  The Z-score threshold is manually set and may require tuning based on the specific data characteristics.

- **Advanced Algorithms:**  
  For more complex scenarios, integrating machine learning-based algorithms like Isolation Forests or Autoencoders could enhance detection capabilities.

- **Scalability:**  
  While optimized for efficiency, handling extremely high-frequency data streams may necessitate further optimizations or leveraging asynchronous processing.

## Conclusion

This project provides a foundational framework for real-time anomaly detection in data streams, balancing simplicity and effectiveness. By adapting to concept drift and seasonal variations, it offers reliable performance in dynamic environments. Future enhancements can build upon this foundation to tackle more complex and large-scale data scenarios.

---

## 4. Running the Project

### Step-by-Step Instructions

1. **Ensure Python 3.x is Installed:**  
   Verify that Python 3.x is installed by running:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

2. **Set Up Virtual Environment (Optional):**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script:**  
   ```bash
   python anomaly_detection_realtime.py
   ```
   *(Ensure the script filename matches)*

5. **Observe Output:**  
   - **CLI Output:**  
     Each data point will be printed in the console, indicating whether it's normal or an anomaly. Anomalies will appear in red.
   - **Real-Time Plot:**  
     A matplotlib window will display the data stream, updating in real-time with anomalies highlighted in red.

---

## 5. Additional Notes

- **Customization:**  
  You can adjust parameters such as `threshold`, `window_size`, `noise_level`, `seasonal_period`, and `drift` in the script to better fit different data characteristics.

- **Extensibility:**  
  The current framework allows for easy integration of more sophisticated anomaly detection algorithms or additional features like logging detected anomalies to a file.

- **Learning Opportunity:**  
  This project serves as a practical introduction to real-time data processing, anomaly detection algorithms, and real-time visualization in Python.

---

Feel free to reach out if you have any questions or need further assistance with your project. Happy coding!
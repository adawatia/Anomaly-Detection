import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
from collections import deque
import logging

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 1. Data Stream Simulation Function
def generate_data_stream(length=1000, noise_level=0.5, seasonal_period=50, drift=0.001, seed=None):
    """
    Generate a simulated data stream with seasonal patterns, random noise, and gradual drift.
    
    Parameters:
        length (int): Total number of data points to generate.
        noise_level (float): Standard deviation of the random noise.
        seasonal_period (int): Periodicity of the seasonal pattern.
        drift (float): Gradual change applied to the mean to simulate concept drift.
        seed (int, optional): Seed for the random number generator for reproducibility.
        
    Returns:
        numpy array: Simulated data stream.
    """
    if seed is not None:
        np.random.seed(seed)  # For reproducibility
    
    x = np.arange(length)
    seasonal_pattern = np.sin(2 * np.pi * x / seasonal_period)
    noise = np.random.normal(0, noise_level, length)
    drift_component = drift * x
    data_stream = seasonal_pattern + noise + drift_component
    logging.info(f"Generated data stream with length={length}, noise_level={noise_level}, "
                 f"seasonal_period={seasonal_period}, drift={drift}")
    return data_stream

# 2. Anomaly Detection Class with Moving Window for Concept Drift
class AnomalyDetector:
    """
    Detects anomalies in a data stream using a moving window to adapt to concept drift and seasonal variations.
    
    Attributes:
        threshold (float): Z-score threshold to flag an anomaly.
        window_size (int): Number of recent data points to consider for statistics.
        data_window (deque): Sliding window of recent data points.
        anomalies_count (int): Total number of anomalies detected.
    """
    def __init__(self, threshold=3, window_size=30):
        """
        Initializes the AnomalyDetector with a specified threshold and window size.
        
        Parameters:
            threshold (float): The Z-score limit for flagging anomalies.
            window_size (int): The size of the moving window for calculating statistics.
        """
        if not isinstance(threshold, (int, float)):
            raise ValueError("Threshold must be a numeric value.")
        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("Window size must be a positive integer.")
        
        self.threshold = threshold
        self.window_size = window_size
        self.data_window = deque(maxlen=self.window_size)
        self.anomalies_count = 0  # Initialize anomaly counter
        logging.info(f"Initialized AnomalyDetector with threshold={threshold} and window_size={window_size}")
    
    def add_data_point(self, value):
        """
        Adds a data point to the window and checks if it's an anomaly.
        
        Parameters:
            value (float): The new data point to add.
        
        Returns:
            bool: True if the data point is an anomaly, False otherwise.
        """
        if not isinstance(value, (int, float, np.number)):
            raise ValueError("Data point must be a numeric value.")
        
        self.data_window.append(value)
        logging.debug(f"Added data point: {value}")
        
        if len(self.data_window) < self.window_size:
            logging.debug("Not enough data to determine anomaly.")
            return False  # Not enough data to determine anomaly
        
        mean = np.mean(self.data_window)
        std_dev = np.std(self.data_window)
        
        if std_dev == 0:
            logging.warning("Standard deviation is zero. Cannot compute Z-score.")
            return False  # Avoid division by zero
        
        z_score = (value - mean) / std_dev
        is_anomaly = abs(z_score) > self.threshold
        if is_anomaly:
            self.anomalies_count += 1
            logging.info(f"Anomaly detected at value={value} with Z-score={z_score:.2f}")
        return is_anomaly

# 3. Real-Time Visualization and CLI Output
def plot_data_stream_realtime(data_stream, detector, interval=100):
    """
    Visualize the data stream in real-time and display anomalies. Also, print live values to the CLI.
    
    Parameters:
        data_stream (numpy array): The simulated data stream.
        detector (AnomalyDetector): An instance of the anomaly detector.
        interval (int): Time delay between updates in milliseconds.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    line, = ax.plot([], [], lw=2, label='Data Stream')
    anomaly_points, = ax.plot([], [], 'ro', label='Anomalies')
    anomaly_count_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    
    ax.set_xlim(0, len(data_stream))
    buffer = 200  # Number of points to display at once for better visibility
    ax.set_ylim(np.min(data_stream) - 1, np.max(data_stream) + 1)
    ax.set_title('Real-Time Data Stream with Anomalies')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    
    data = []
    anomaly_indices = []
    
    def update(frame):
        nonlocal data, anomaly_indices
        
        if frame >= len(data_stream):
            logging.info("All data points have been processed.")
            ani.event_source.stop()
            return line, anomaly_points, anomaly_count_text
        
        value = data_stream[frame]
        data.append(value)
        
        try:
            is_anomaly = detector.add_data_point(value)
        except ValueError as e:
            logging.error(f"Error processing data point {frame}: {e}")
            is_anomaly = False
        
        if is_anomaly:
            anomaly_indices.append(frame)
            print(f"\033[91mData Point {frame}: {value:.2f} (Anomaly Detected)\033[0m")
        else:
            print(f"Data Point {frame}: {value:.2f} (Normal)")
        
        # Update plot data
        if frame < buffer:
            ax.set_xlim(0, buffer)
        else:
            ax.set_xlim(frame - buffer, frame)
        
        line.set_data(range(len(data)), data)
        anomaly_points.set_data(anomaly_indices, [data_stream[i] for i in anomaly_indices])
        anomaly_count_text.set_text(f'Total Anomalies Detected: {detector.anomalies_count}')
        
        return line, anomaly_points, anomaly_count_text
    
    ani = FuncAnimation(fig, update, frames=range(len(data_stream)),
                        interval=interval, blit=True, repeat=False)
    
    plt.tight_layout()
    plt.show()

# 4. Main Function to Run the Real-Time System
def main():
    """
    Main function to execute the real-time anomaly detection system.
    """
    try:
        print("Initializing the data stream and anomaly detector...\n")
        logging.info("Starting the anomaly detection system.")
        
        # Generate a simulated data stream with a fixed seed for reproducibility
        data_stream = generate_data_stream(length=1000, noise_level=0.5, seasonal_period=50, drift=0.001, seed=42)
        
        # Introduce some anomalies for demonstration purposes
        num_anomalies = 20
        anomaly_indices = np.random.choice(range(100, 900), size=num_anomalies, replace=False)
        data_stream[anomaly_indices] += np.random.choice([10, -10], size=num_anomalies)  # Adding large deviations
        logging.info(f"Introduced {num_anomalies} anomalies into the data stream.")
        
        # Initialize the anomaly detector with threshold 2.5 and window size 50
        detector = AnomalyDetector(threshold=2.5, window_size=50)
        
        # Start real-time plotting and CLI output
        plot_data_stream_realtime(data_stream, detector, interval=50)
        
        print(f"\nTotal Anomalies Detected: {detector.anomalies_count}")
        logging.info(f"Total Anomalies Detected: {detector.anomalies_count}")
    
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

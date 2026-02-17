# 🔥 AI-Powered Real-Time Fire Detection System

An end-to-end Computer Vision project featuring **YOLOv8** object detection integrated with an **Arduino Nano** hardware alert system.

## 📌 Project Overview

This project utilizes a custom-trained YOLOv8 model to detect fire and smoke in real-time. The system doesn't just "see" the fire; it calculates the **Fire Intensity** based on bounding box area and triggers a physical alarm via Arduino once a danger threshold is met.

### Key Features

* **Custom YOLOv8 Model**: Trained for 50 epochs on a dataset of ~9,000 images.
* **Dynamic UI**: The bounding box and labels only appear on the screen when fire is actually detected, keeping the monitor clean.
* **Intensity Logic**: Automatically calculates the percentage of the frame covered by fire.
* **Hardware-in-the-Loop**: Real-time Serial communication (9600 baud) between Python and Arduino Nano.
* **Physical Alerts**: 0.96" OLED display provides status updates while a Piezo Buzzer provides audible warnings.

---

## 🛠️ Hardware Requirements & Pinout

| Component | Arduino Nano Pin | Connection |
| --- | --- | --- |
| **OLED VCC** | **5V** | Power |
| **OLED GND** | **GND** | Ground |
| **OLED SCL** | **A5** | I2C Clock Line |
| **OLED SDA** | **A4** | I2C Data Line |
| **Buzzer (+)** | **D2** | Digital Output |

---

## 💻 Software Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Fire_Detector_Project.git
cd Fire_Detector_Project

```

### 2. Install Dependencies

Ensure you are using **Python 3.11.0**.

```bash
pip install -r requirements.txt

```

### 3. Upload Firmware

Open the `sketch_feb17a/` folder in the Arduino IDE and upload the code to your **Arduino Nano**.

---

## 🚀 How to Run

1. Connect your Arduino Nano via USB.
2. Identify your COM port (e.g., `COM3`) in the Arduino IDE.
3. Update the port in `main.py`:
```python
arduino = serial.Serial(port='COM3', baudrate=9600)

```


4. Run the application:
```bash
python main.py

```



---

## 📊 Model Performance

The model was trained in Google Colab using a Tesla T4 GPU.

* **Training Time**: ~2.9 Hours.
* **Precision (Fire)**: 68.9%.
* **Recall (Fire)**: 56.3%.

---

## 📁 Repository Structure

* `Fire_Detection.ipynb`: Full training history and logs from Google Colab.
* `best.pt`: The optimized weights for the YOLOv8 model.
* `main.py`: Main Python execution script for PC-side AI and Serial bridge.
* `sketch_feb17a/`: C++ source code for the Arduino Nano.

---

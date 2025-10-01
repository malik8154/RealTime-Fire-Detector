# Real-Time Fire Detector

![Python](https://img.shields.io/badge/python-3.10+-blue)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.12+-orange)
![OpenCV](https://img.shields.io/badge/opencv-4.12-green)
![License](https://img.shields.io/badge/license-MIT-blue)

A real-time fire detection system using a Convolutional Neural Network (CNN) trained on fire and non-fire images. Detects fire instantly from live camera feed, triggers an alarm, and logs fire events automatically.

---

## 📁 Project Structure

```

RealTime-Fire-Detector/
│
├── dataset_sample/           # Small sample images (fire / non-fire)
├── models/
│   └── forest_fire_cnn.h5    # Trained CNN model (from models.rar)
├── notebooks/
│   └── train_fire_model.ipynb
├── fire_detection.py          # Real-time detection code
├── requirements.txt
├── README.md
└── LICENSE

````

---

## 🎥 Demo

![Fire Detection Demo](images/demo.gif)  
*Replace with your own GIF or screenshot of detection in action.*

- Works with a laptop webcam or an Android phone IP camera.  
- Triggers an audible alert when fire is detected.  
- Logs events in `fire_alerts.log`.

---

## 🛠️ Requirements

- Python 3.10+  
- TensorFlow >= 2.12.0  
- Keras >= 2.12.0  
- OpenCV >= 4.12.0  
- NumPy >= 1.26.0  
- Matplotlib >= 3.8.0  
- scikit-learn >= 1.3.0  
- Jupyter >= 1.0.0  
- ipykernel >= 6.30.0  

Install dependencies:

```bash
pip install -r requirements.txt
````

Or with Conda:

```bash
conda create -n ds_env python=3.10
conda activate ds_env
pip install -r requirements.txt
```

---

## 🚀 Usage

### **1. Laptop Webcam**

```bash
python fire_detection.py
```

### **2. Android Phone Camera (IP Webcam)**

1. Install **IP Webcam** app on your phone.
2. Connect your PC and phone to the **same Wi-Fi network**.
3. Start IP Webcam → choose **MJPEG / Browser stream**.
4. Update the URL in `fire_detection.py`:

```python
url = "http://<your-phone-ip>:8080/video"
```

5. Run the script:

```bash
python fire_detection.py
```

6. Press **`q`** to quit.

---

## 📥 Download the Trained Model

Download the trained CNN model for real-time fire detection:
[models.rar](https://github.com/malik8154/RealTime-Fire-Detector/releases/download/v1.0/models.rar)

> Extract the `.rar` file to get `forest_fire_cnn.h5` before running `fire_detection.py`.

---

## ⚠️ Notes

* Any small flame (candle, lighter, fire video) works for testing.
* No need for an actual forest fire.
* Ensure good lighting and camera clarity for the best detection.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

---

## 📌 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

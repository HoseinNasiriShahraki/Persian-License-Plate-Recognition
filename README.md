# Persian License Plate Recognition System

This repository showcases the **Persian License Plate Recognition** (PLPR) system, developed to accurately identify and process Persian license plates from various image and video sources. The system demonstrates its functionality through pre-recorded videos, illustrating model performance in different scenarios.

## Project Overview

The PLPR system leverages state-of-the-art machine learning techniques for accurate detection and recognition of Persian license plates, enabling high performance in challenging conditions. Key components and features include:

- **Image Preprocessing**: Includes resizing, grayscale conversion, and noise reduction to improve recognition accuracy.
- **Deep Learning Model**: A customized mT5 model fine-tuned for Persian license plate recognition.
- **Pipeline for Processing**: Efficiently handles video streams, identifies plates, and decodes characters.

### Model Highlights
- **Language-Specific Optimization**: Fine-tuned specifically for Persian language license plates.
- **Real-Time Recognition**: Fast processing for practical application in real-time traffic monitoring.
- **Adaptability**: Demonstrates robustness to varying lighting, orientation, and occlusion.

## Results

| Metric                        | Value |
|-------------------------------|-------|
| Plate Detection Accuracy      | 97.7%   |
| Character Recognition Accuracy| 99.8%   |
| Overall Accuracy                  | 98.8%   |
| Plate Detection Inference Speed | 20 ms  |
| Character Recognition Inference Speed Per Character| 44 ms  |
| FPS Speed with CPU         | 17 FPS|
| FPS Speed with GPU         | TBT|
## Showcasing Videos

Below are two videos demonstrating the PLPR system in action:

https://github.com/user-attachments/assets/332e5c6a-b945-4054-ba76-7ec2e13fa3b3

https://github.com/HoseinNasiriShahraki/Persian-License-Plate-Recognition/assets/145256807/5bbeeac8-9d3b-43d9-bd79-70619bdeef2d


These videos highlight the system's accuracy and speed under different conditions, reflecting real-world performance.

## System Architecture

The PLPR system's architecture includes the following modules:

1. **Preprocessing**: Resizes, normalizes, and applies noise reduction.
2. **Detection Model**: Leverages a YOLO backbone for plate localization.
3. **Recognition Model**: A ResNET CNN model tailored for Persian text decoding.

## Contact

For further inquiries about the PLPR system, please contact:

- **Email**: [hosein.nasiri@outlook.com]
- **LinkedIn**: [[LinkedIn Profile Link](https://www.linkedin.com/in/hosein-nasiri-shahraki)]

---

> **Note:** This README is crafted for presentation purposes and is not designed for public deployment or open-source contributions.

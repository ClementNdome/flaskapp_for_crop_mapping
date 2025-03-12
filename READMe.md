# Early Warning System for Crop Yield and Soil Moisture Monitoring

## Overview
This project is a Flask-based Early Warning System (EWS) designed to help farmers and Community Forest Associations (CFAs) monitor crop yield, soil moisture levels, and prevailing weather conditions in real-time. The system integrates machine learning models, remote sensing data, and real-time weather forecasts to generate alerts and provide actionable recommendations.

## Features
- Real-time weather and soil moisture monitoring
- Machine learning-based crop yield prediction
- Automated alert system when critical thresholds are exceeded
- Integration with PostgreSQL/PostGIS for spatial data management
- Communication via text messages and mobile app notifications

## Technologies Used
- Flask (Python web framework)
- PostgreSQL + PostGIS (spatial database management)
- Google Earth Engine (remote sensing data processing)
- Machine Learning (Scikit-learn, TensorFlow)
- Leaflet.js (interactive mapping)
- Twilio API / Firebase (for text message and mobile app notifications)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ClementNdome/flaskapp_for_crop_mapping.git
   cd flaskapp_for_crop_mapping
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up PostgreSQL and PostGIS:
   - Install PostgreSQL and PostGIS.
   - Create a database and enable PostGIS extension:
     ```sql
     CREATE DATABASE crop_ews;
     CREATE EXTENSION postgis;
     ```
   - Update `config.py` with your database credentials.

5. Run the application:
   ```bash
   python main.py
   ```
6. Open a web browser and go to `http://localhost:5000`.

## Usage
- View real-time crop yield predictions and soil moisture data.
- Receive alerts when critical thresholds are exceeded.
- Access recommendations for mitigating risks.
- Visualize spatial data on an interactive map.

## Deployment
This project can be deployed using:
- Docker for containerized deployment.
- AWS/GCP for cloud-based hosting and processing.
- Render, Heroku, or DigitalOcean for web hosting.

## License
**This project is proprietary and confidential.**
- Unauthorized use, distribution, or modification is strictly prohibited.
- The code and associated materials belong to the respective company.
- Access is restricted to authorized personnel only.

## Author
[Clement Ndome](https://github.com/ClementNdome)


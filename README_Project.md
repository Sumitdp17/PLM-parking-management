# PLM Parking Management System

A Flask-based smart parking solution that simulates vehicle entry, space allocation, exit processing, fees, and real-time dashboard monitoring for a parking lot.

## Project Details

- Project ID: P21
- Course: UE23CS341A
- Academic Year: 2025
- Semester: 5th Sem
- Campus: RR
- Branch: AIML
- Section: D
- Team: Tech Titans

## Overview

This project is designed to model a modern parking facility with:

- Vehicle entry simulation through an entry kiosk
- Automatic slot assignment and occupancy tracking
- Barrier control simulation for entry and exit
- Exit fee calculation based on parking duration
- Mock payment support using cash, card, or QR code
- Receipt generation in PDF format
- Maintenance and dashboard views for monitoring

The application is built with Python and Flask, and organizes logic into reusable modules for parking, payment, dashboard, and barrier simulation.

## Features

### 1. Vehicle Entry Management
- Accepts vehicle number plate input
- Opens the simulated entry barrier
- Assigns an available slot from the parking lot
- Records the entry in the parking data store

### 2. Occupancy Dashboard
- Tracks number of occupied vs available slots
- Provides a dashboard summary for parking operators
- Supports real-time data queries via Flask routes

### 3. Exit and Billing
- Locates active parked vehicles by plate number
- Calculates parking fee based on duration
- Updates parking status and slot availability
- Generates a downloadable PDF receipt

### 4. Payment Processing
- Cash payment
- Card payment validation
- QR payment validation
- Mock transaction responses for testing/demo workflows

### 5. Maintenance Monitoring
- Loads maintenance records
- Offers a dedicated maintenance dashboard page
- Helps track operational issues or service data

## Tech Stack

- Python 3
- Flask
- Jinja2
- JSON-based state storage
- ReportLab for receipt PDF generation
- QR code support for mock payment processing
- Pytest for testing

## Repository Structure

```text
PLM-parking-management/
├── .github/
│   └── workflows/
├── Deliverables/
│   └── User Stories.docx
├── app/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── utils.py
├── modules/
│   ├── anpr/
│   ├── barrier/
│   ├── dashboard/
│   ├── parking/
│   ├── payment/
│   └── security/
├── tests/
├── .gitignore
├── __init__.py
├── config.py
├── README.md
├── README_Project.md
├── requirements.txt
├── run.py
└── data/   # Runtime-generated parking and receipt data
```

## Application Workflow

1. User visits the entry page and submits a vehicle plate number.
2. The system opens the simulated entry barrier.
3. An available parking slot is assigned and stored.
4. The dashboard updates occupancy information.
5. Vehicle exits are processed with a fee calculation.
6. A payment method is used for the final transaction process.
7. A receipt is generated and presented to the user.

## API and Routes

The Flask app exposes the following core routes:

- `/` - App health check
- `/auth/login` - Authentication route
- `/entry/` - Entry kiosk page
- `/entry/simulate_entry` - Simulated parking entry
- `/exit/` - Exit processing page and vehicle exit flow
- `/dashboard/` - Dashboard view
- `/dashboard/data` - Occupancy data JSON
- `/payment/pay` - Payment processing endpoint
- `/maintenance` - Maintenance page

## Installation

### Prerequisites

- Python 3.9+
- pip
- Virtual environment tool (optional but recommended)

### Setup

```bash
git clone https://github.com/Sumitdp17/PLM-parking-management.git
cd PLM-parking-management
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

```bash
python run.py
```

Once started, the app runs on the default Flask development server and exposes the parking management endpoints.

## Testing

```bash
pytest
```

The repository contains tests for dashboard, entry, exit, payment, and parking workflow behavior.

## Development Team

- @PES1UG23AM195 - Scrum Master
- @PES1UG23AM191 - Developer Team
- @pes1ug23am212 - Developer Team
- @PES1UG23AM209 - Developer Team

## Faculty and Mentors

- @Amrutha-PES - Teaching Assistant
- @VenomBlood1207 - Teaching Assistant
- @Arpitha035 - Faculty Supervisor

## License

This project is developed for academic and educational purposes as part of PES University coursework.

---

Course: UE23CS341A  
Institution: PES University  
Academic Year: 2025  
Semester: 5th Sem

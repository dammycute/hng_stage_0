# HNG12 Stage 0 - Public API

## Description
This is a simple public API developed for the HNG12 internship Stage 0 backend task. The API returns basic information in JSON format, including:
- The registered email used on the HNG12 Slack workspace.
- The current date and time in ISO 8601 format (UTC).
- The GitHub URL of the project repository.

## Technology Stack
- **Backend:** Django (Python)
- **Hosting:** Koyeb
- **Database:** None (Static JSON response)
- **CORS Handling:** Enabled using `django-cors-headers`

## API Endpoint
### **Base URL:** `https://stiff-kamillah-htcode-dae24342.koyeb.app/`

### **GET /**
#### **Response Format (200 OK)**
```json
{
  "email": "email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/dammycute/hng_stage_0.git"
}
```

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/dammycute/hng_stage_0.git
cd hng_stage_0
```

### **2. Create & Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run Migrations**
```sh
python manage.py migrate
```

### **5. Start the Server**
```sh
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`

## Deployment
The API is deployed on Render.

## Useful Links
- [Hire Python Developers](https://hng.tech/hire/python-developers)

## License
This project is licensed under the MIT License.


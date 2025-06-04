# Straiv PMS Integration Assignment

## ✅ Task 1: API Integration & Data Mapping

This Django project implements a mock integration with a Property Management System (PMS), demonstrating API consumption, data mapping, error handling, and clean code structure.

### 🔗 Endpoint

```
GET /api/integrations/pms/bookings/
```

### 📄 Sample Response
```json
[
  {
    "guest_name": "John Doe",
    "room_number": 101,
    "check_in": "2025-06-10",
    "check_out": "2025-06-12"
  }
]
```

### 🧠 Structure & Approach
- `services/pms_client.py`: Simulates fetching data from a third-party PMS API.
- `serializers.py`: Maps external data to an internal booking model.
- `views.py`: Exposes the data via a clean Django REST endpoint.
- `test_mapping.py`: Unit tests the data mapping logic.

### ⚙️ Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/pms-integration.git
cd pms-integration
python -m venv straiv-venv
source straiv-venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### ✅ Run Tests

```bash
python manage.py test integrations
```

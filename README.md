# 📢 Ad Management API

## 📌 Overview
This is a Django REST API for managing **Ad Campaigns**, **Branches**, **Audiences**, **Positionings**, and **Ads**.  
It allows users to **create, update, delete, and retrieve** records while enforcing business rules such as **budget limits** and **active campaign validation**.

---

## 📥 How to Clone the Repository

```sh
git clone https://github.com/your-username/ad-management-api.git
```

---

## 🚀 How to Set Up the Project
### 1️⃣ Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations
```sh
python manage.py migrate
```

### 4️⃣ Run the Server
```sh
python manage.py runserver
```

The API will be available at: 🔗 http://127.0.0.1:8000/api/

---

## 📡 Available API Endpoints

Here’s how you can format the **Available API Endpoints** section using the example structure you provided:  

---

### **📡 Available API Endpoints**
| **Resource**      | **Method** | **Endpoint**                 | **Description**                                      |
|-------------------|-----------|------------------------------|------------------------------------------------------|
| **Branches**      |           |                              |                                                      |
| Get all Branches  | `GET`     | `/api/branchs/`             | Retrieve all branches                               |
| Create a Branch   | `POST`    | `/api/branchs/create/`      | Create a new branch                                |
| Get a Branch      | `GET`     | `/api/branchs/{id}`         | Retrieve a specific branch                         |
| Update a Branch   | `PATCH`   | `/api/branchs/{id}`         | Update an existing branch                          |
| Delete a Branch   | `DELETE`  | `/api/branchs/{id}`         | Remove a branch                                    |
| **Audiences**     |           |                              |                                                      |
| Get all Audiences | `GET`     | `/api/audiences/`          | Retrieve all audiences                            |
| Create an Audience | `POST`   | `/api/audiences/create/`   | Create a new audience                            |
| Get an Audience   | `GET`     | `/api/audiences/{id}`      | Retrieve a specific audience                     |
| Update an Audience | `PATCH`  | `/api/audiences/{id}`      | Update an existing audience                      |
| Delete an Audience | `DELETE` | `/api/audiences/{id}`      | Remove an audience                              |
| **Positionings**  |           |                              |                                                      |
| Get all Positionings | `GET`   | `/api/positionings/`       | Retrieve all positionings                         |
| Create a Positioning | `POST`  | `/api/positionings/create/`| Create a new positioning                         |
| Get a Positioning | `GET`     | `/api/positionings/{id}`   | Retrieve a specific positioning                  |
| Update a Positioning | `PATCH` | `/api/positionings/{id}`   | Update an existing positioning                   |
| Delete a Positioning | `DELETE`| `/api/positionings/{id}`   | Remove a positioning                            |
| **Campaigns**     |           |                              |                                                      |
| Get all Campaigns | `GET`     | `/api/campaigns/`          | Retrieve all campaigns                           |
| Create a Campaign | `POST`    | `/api/campaigns/create/`   | Create a new campaign                           |
| Get a Campaign    | `GET`     | `/api/campaigns/{id}`      | Retrieve a specific campaign                    |
| Update a Campaign | `PATCH`   | `/api/campaigns/{id}`      | Update an existing campaign                     |
| Delete a Campaign | `DELETE`  | `/api/campaigns/{id}`      | Remove a campaign                              |
| **Ads**          |           |                              |                                                      |
| Get all Ads       | `GET`     | `/api/ads/`                | Retrieve all ads                                 |
| Create an Ad      | `POST`    | `/api/ads/create/`         | Create a new ad                                 |
| Get an Ad        | `GET`     | `/api/ads/{id}`            | Retrieve a specific ad                          |
| Update an Ad     | `PATCH`   | `/api/ads/{id}`            | Update an existing ad                          |
| Delete an Ad     | `DELETE`  | `/api/ads/{id}`            | Remove an ad                                   |

---

## 🔥 JSON Request Examples
### 1️⃣ Create a Branch
**POST** /api/branchs/create/
```json
{
  "name": "Tech Branch",
  "monthly_budget": 20000.00,
  "daily_budget": 1000.00,
  "pixel": "PX-123456",
  "activated": "active",
  "instagram": "https://instagram.com/techbranch",
  "facebook": "https://facebook.com/techbranch",
  "website": "https://www.techbranch.com"
}
```

✅ Expected Response (201 Created)
```json
{
  "id": 1,
  "name": "Tech Branch",
  "monthly_budget": 20000.00,
  "daily_budget": 1000.00,
  "pixel": "PX-123456",
  "activated": "active",
  "instagram": "https://instagram.com/techbranch",
  "facebook": "https://facebook.com/techbranch",
  "website": "https://www.techbranch.com"
}
```
### 2️⃣ Create a Campaign
**POST** /api/campaigns/create/
```json
{
  "name": "Black Friday Sale",
  "activated": "active",
  "daily_budget": 1500.00,
  "dayparting": true,
  "dayparting_hours": {
    "Monday": ["08:00-12:00"],
    "Friday": ["14:00-20:00"]
  },
  "objetive_of_the_compaign": "Sales",
  "branch_id": 1,
  "positioning_id": 3,
  "audience_id": 2
}
```

✅ Expected Response (201 Created)
```json
{
  "id": 1,
  "name": "Black Friday Sale",
  "activated": "active",
  "daily_budget": 1500.00,
  "dayparting": true,
  "dayparting_hours": {
    "Monday": ["08:00-12:00"],
    "Friday": ["14:00-20:00"]
  },
  "objetive_of_the_compaign": "Sales",
  "branch_id": 1,
  "positioning_id": 3,
  "audience_id": 2
}
```

---

## 🚨 Error Handling & Expected Messages
### 1️⃣ Branch Not Found (404 Not Found)
```json
{
  "error": "Branch not found!"
}
```

### 2️⃣ Campaign Cannot Be Created Due to Inactive References (406 Not Acceptable)
```json
{
  "error": "Cannot create a Campaign for an inactive Branch, Positioning, or Audience"
}
```

### 3️⃣ Campaign Exceeded Budget (200 OK with Warning)
```json
{
  "message": "Warning: The daily budget of 12000.0 has hit or exceeded the limit (10000.0 daily / 50000.0 monthly). The campaign has been deactivated.",
  "campaign": {
    "id": 4,
    "name": "Updated Campaign",
    "activated": "inactive",
    "daily_budget": 12000.00
  }
}
```

---

## ⏳ Automated Reset of Budgets & Reactivation
Campaigns are automatically reset and reactivated at the start of each new day using Django management commands.

### Manually Run Reset
```sh
python manage.py reset_campaigns
```
✅ Expected Output:
```sh
10 campaigns reset on 2024-02-05
```
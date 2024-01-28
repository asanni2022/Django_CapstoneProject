# Django_CapstoneProject

## Project Description: Automating Employee Salary Processing with Django and Azure

**Problem:** Traditional manual salary processing is inefficient, error-prone, and consumes valuable resources. This project tackles these challenges by developing an automated and secure system using Django and Azure cloud services.

**Solution:**

We built a robust Django-based API backend hosted on Azure Web Apps. This API:

* Handles all **CRUD operations** for employee and salary data.
* Provides **secure access** through Azure Active Directory authentication.
* Integrates with a **PostgreSQL database** for reliable data storage.
* Leverages **Azure DevOps and GitHub Actions** for automated CI/CD, ensuring seamless updates and maintenance.

**Technical Architecture:**

- **API Backend:**
    - Built with Django for a **robust and scalable framework**.
    - Hosted on **Azure Web Apps** for a **managed and scalable PaaS solution**.
    - Offers **auto-scaling** to handle peak workloads efficiently.
- **Database:**
    - **PostgreSQL database** chosen for its reliability, features, and **managed Azure service**.
    - Provides **persistent storage and transactional capabilities**.
- **CI/CD Pipeline:**
    - **Azure DevOps** manages the process.
    - **GitHub Actions** triggered on code commits.
    - **Automate testing, building, and deployment** to Azure Web Apps.
- **Source Control:**
    - **GitHub (or Azure Repos)** manages the codebase and tracks changes.

**Benefits:**

**Cost Benefits:**

* **Reduced operational costs:** Eliminate manual data entry and verification.
* **Scalable infrastructure:** Pay-as-you-go pricing model on Azure Web Apps.
* **Resource optimization:** CI/CD pipeline minimizes release management needs.

**Operational Benefits:**

* **Increased accuracy:** Automated calculations eliminate human error.
* **Time-saving:** Process salaries from hours to minutes.
* **Regulatory compliance:** Designed to adhere to financial regulations and audit trails.
* **Improved employee satisfaction:** Timely and accurate disbursements.

**Security and Compliance:**

* **Secure data handling:** Azure AD authentication restricts access.
* **Data protection:** Data at rest and in transit are encrypted.

**Improvements:**

* Combined strengths of both descriptions for a comprehensive overview.
* Streamlined technical details for better readability.
* Emphasized project goals, benefits, and security.
* Used concise and active voice for better impact.

- Demo AppService Django Deployment via github
- Dockerfile and docker-compose with Postgresql db

# Deploy Django App to Azure AppService:

Create a new folder:
> mkdir Django_EmployeeSalaryApp  

move into that folder:
> cd Django_EmployeeSalaryApp

## Create Virtual Environment
```
Python3 -m venv .venv
source /Users/mac/Diverg_CapstoneProject/Django_CapstoneProject/
.venv/bin/activate
```

Create a new django project with admin functionality:
```
- Install All dependencies
pip install django
Pip install djangorestframework
Pip install django-cors-headers   # unblocks request to different domains

django-admin startproject hello_project . # files: (init.py indicates its a python module; asgi.py entry point for asgi compatible webservers; wsgi.py entry point for wsgi compatible webservers; urls.py: contains all the url declaration needed for the project; settings.py conguration at project level; manage.py: CLI utility that helps interact with the python project)
- Run the Project to Test django setup
python manage.py runserver
- running port: http://127.0.0.1:8000/

- Create App to implement API methods
python manage.py startapp SalaryApp   # Configure settings.py with the newly created App
- update models.py with models ( DB Tables are created from this model) needed for our App.

- Build Database
pip install psycopg2   # DB adaptor, To connect to Postgresql from Django App.

Create a Azure Postgresql Database or Local Postgres DB
- Test DB connection using DBerver or PG-Admin
- Create Database
- Add database details in the settings.py at project level

# Create tables for models
python manage.py makemigration SalaryApp
python manage.py migrate SalaryApp   # push changes to database to create tables


- From PG-Admin Insert records into tables

# Create serializers.py at App level  # This helps to conert and breakdown complex types or model into python data types rendered in json or others.
# views.py contains the API methods and where we handles the CRUD (GET, POST, PUT, DELETE) operations

# Requirements file
pip freeze > requirements.txt
deactivate

```
<img width="1358" alt="Screenshot 2024-01-24 at 8 46 21 PM" src="https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/9cc32b85-4cf8-4f79-b613-04dc7190c2bd">



><img width="633" alt="Screenshot 2024-01-24 at 9 29 44 PM" src="https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/4cde1ccb-0501-4dfb-b6fa-cf404e50e435">


>![Screenshot 2024-01-24 at 10 30 00 PM](https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/79232744-771f-4e00-9ac0-c98f99316e69)



![Screenshot 2024-01-24 at 10 32 08 PM](https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/6cf923ac-24cf-4506-87eb-2ac9bf2345c4)

![Screenshot 2024-01-24 at 10 59 42 PM](https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/b36caf76-ab3e-45cd-9bf0-1b1c3ca91f20)

![Screenshot 2024-01-24 at 10 59 56 PM](https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/d4e7f779-7a50-45b0-a57e-77eb06358569)

![Screenshot 2024-01-24 at 11 00 30 PM](https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/e79807ec-fe6b-4997-b1a3-d511ceac5fe8)




![Screenshot 2024-01-25 at 8 57 40 PM](https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/edbca863-ddee-4213-b801-61f27f4a0dd5)



<img width="1195" alt="Screenshot 2024-01-25 at 11 08 43 AM" src="https://github.com/asanni2022/Django_CapstoneProject/assets/104282577/4781f9a7-7a10-4faf-8938-c65ac8c737ea">






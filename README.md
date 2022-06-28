## Installation

Python3 must be already installed

```
git clone https://github.com/8Men5Camels/medic
python -m venv venv
venv\Scripts\activate  # (on Windows)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver  # starts Django Server
```

## Features

#### To access the admin panel:
```
http://localhost:8000/admin/
```
You will be able to add, edit, delete, filter and search for entities using the built-in capabilities of the Django admin panel.

#### List of API routes:

- list of API endpoints:

```
api/hospital/
```
- List of directions:

```
api/hospital/directions/
```
- List of doctors:

```
api/hospital/doctors/
```
- Detailed information about the doctor by ```id```:

```
api/hospital/doctors/<id>
```

#### List of API filtering routes:
- Filtering of doctors by ```id``` of direction:
```
api/hospital/doctors/?directions=<id>
```
- Filtering of doctors by years of experience "from - to" in years inclusive:
```
api/hospital/doctors/?exp_min=<year>&exp_max=<year>
```

#### List of API sorting routes:
- Sort by date of birth:

```api/hospital/doctors/?ordering=date_birth```

in descending order:

```api/hospital/doctors/?ordering=-date_birth```

- Sort by work experience:

```api/hospital/doctors/?ordering=work_experience```

in descending order:

```api/hospital/doctors/?ordering=-work_experience```
# Dance Fitness Class Booking & Instructor Platform

**CS50W Final Project** – A full‑featured scheduling and booking system for dance/fitness classes.

## 📌 Distinctiveness and Complexity

**Distinctiveness**
This project manages class bookings with role‑based access, capacity limits, and attendance tracking. This project's has functionalities such as scheduling and booking dance classes with a calendar logic. You halso ave the choice to choose instructors or students and choose classes and their categories. (different from having features such as posts, likes, biddings, or follow). And This project solves a real‑world problem.

**Complexity**

- **Role‑based permissions** – instructors vs. students, each with different views and actions.
- **Capacity management** – automatic calculation of remaining spots, prevents overbooking.
- **Reverse relations** – `ScheduledClass.remaining_spots()` uses `booking_set` to count confirmed bookings.
- **Unique constraints** – a student cannot book the same class twice.
- **Future‑ready design** – models separate `ClassType` (what) from `ScheduledClass` (when), making it easy to add recurring classes later.

## 🧱 Models

| Model | Purpose |
|-------|---------|
| `User` (custom) | Extended Django user with `is_instructor` flag and `bio`. |
| `Category` | e.g., Cardio, Strength – for filtering classes. |
| `ClassType` | Describes a class: name, description, category, default duration. |
| `ScheduledClass` | A specific occurrence: date, time, instructor, capacity, location. |
| `Booking` | Links a student to a scheduled class; tracks status and attendance. |

## 🚀 Features

- **Authentication** – register, login, logout (students and instructors).
- **Browse classes** – view all upcoming classes on the homepage.
- **Book / cancel** – students can book or cancel (AJAX, no page reload).
- **Instructor dashboard** – instructors can create, edit, delete their own classes.
- **Capacity tracking** – remaining spots update automatically.
- **Student dashboard** – see upcoming and past bookings.
- **Admin panel** – full CRUD for all models via Django admin.
- **Mobile‑responsive** – works on phones, tablets, and desktops.

## 📁 File Structure
final-project/
├── booking/
│ ├── migrations/
│ ├── templates/booking/
│ │ ├── layout.html
│ │ ├── index.html
│ │ ├── class_detail.html
│ │ ├── instructor_dashboard.html
│ │ ├── student_dashboard.html
│ │ └── login.html / register.html
│ ├── static/booking/
│ │ └── styles.css
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── final_project/ (project settings)
│ ├── settings.py
│ └── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt


## 🛠️ How to Run

1. **Clone the repository**
   `git clone https://github.com/yourusername/my_learning_journey_2026.git`

2. **Navigate to the final project folder**
   `cd my_learning_journey_2026/cs50w/final-project`

3. **Create a virtual environment**
   `python -m venv venv`

4. **Activate it**
   - Mac/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`

5. **Install dependencies**
   `pip install -r requirements.txt`

6. **Run migrations**
   `python manage.py migrate`

7. **Create a superuser (admin)**
   `python manage.py createsuperuser`

8. **Start the server**
   `python manage.py runserver`

9. **Visit the app**
   `http://127.0.0.1:8000`

10. **Admin interface**
    `http://127.0.0.1:8000/admin`

## 🔧 Sample Data

You can add sample data via the Django admin or the shell:

```bash
python3 manage.py shell
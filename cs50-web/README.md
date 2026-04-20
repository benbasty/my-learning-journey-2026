# CS50’s Web Programming with Python and JavaScript

This folder contains all my projects for Harvard’s CS50W course (2026 edition).
Each subfolder is a complete, working web application.

## 📚 Projects

| # | Project | Description | Tech |
|---|---------|-------------|------|
| 0 | **Search** | Front‑end clone of Google Search | HTML, CSS |
| 1 | **Wiki** | Wikipedia‑like encyclopedia | Django |
| 2 | **Commerce** | eBay‑style auction site | Django, JavaScript |
| 3 | **Mail** | Single‑page email client | JavaScript, Fetch API |
| 4 | **Network** | Twitter‑like social network | Django, JavaScript, Pagination |
| 5 | **Final Project** | Dance Fitness Class Booking Platform | Django, JavaScript, AJAX |

## 🏆 Final Project Highlight

My final project is a **Dance Fitness Class Booking & Instructor Platform** – a full scheduling system where instructors create classes and students book them, with real‑time availability updates.

See the `final-project/` folder for details.

## 🚀 How to Run Any Project

1. Navigate into the project folder.
2. Create a virtual environment:
   `python -m venv venv`
3. Activate it:
   `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies:
   `pip install -r requirements.txt`
5. Run migrations:
   `python manage.py migrate`
6. Start the server:
   `python manage.py runserver`

Each project’s own README has more specific instructions.

---

*All projects passed CS50W’s tests and are deployment‑ready.*
# Indeed Job Dashboard

A simple web dashboard built with **Dash** and **Dash Bootstrap Components** to search for jobs on Indeed by title and location.  

The app scrapes job listings from Indeed and displays them in a clean, card-based layout for easy browsing.

---

## Features

- Search jobs by **title** and **city**
- Display jobs in **Bootstrap cards**
- Show **company**, **job title**, and **location**
- Responsive layout (works on desktop and mobile)
- Built with Python 3.11 and Dash

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/indeed-job-dashboard.git
cd indeed-job-dashboard
```
2. **Create a virtual environment:**
   python -m venv .venv

4. **Activate the virtual environment:**
   .\.venv\Scripts\activate
   
6. **Install the dependencies: **
   pip install -r requirements.txt
If you don’t have a requirements.txt file yet, create one with:

dash
dash-bootstrap-components
pandas
plotly
python-jobspy

8. **Usage **
   python app.py

10. **Open your browser and go to: **
 http://127.0.0.1:8050/

12. **Project Structure **
  indeed-job-dashboard/
│
├── app.py               # Main Dash application
├── scraper.py           # Contains scrape_jobs_df() function
├── .venv/               # Python virtual environment
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
<img width="3502" height="1307" alt="image" src="https://github.com/user-attachments/assets/1356fced-a34e-474f-9069-2b95d95b1eb1" />

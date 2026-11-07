# Unison 
### A lightweight, Twitter-inspired Django web application where users can create profiles, share and discover Posts.


## ✨ Features
* **User Authentication:** Users can easily register and log in to the platform.
* **Post Management (CRUD):** Users have full control to create, read, update, and delete their own posts.
* **Global Feed:** A central home page that displays all posts shared by the community.
* **Search Functionality:** A global search bar to quickly find specific content across all posts.


## UI Preview
[Unis list](screenshots/unis_list.png)

[Unis create view](screenshots/unis_create.png)



## 🛠️ Tech Stack
* **Backend:** Python, Django , Sqlite
* **Frontend:** HTML, CSS, Bootstrap
* **Image Processing:** Pillow
* **Environment Management:** `uv`


## Installation & Setup 

**Prerequisites:** 
* Python 3.8+ installed on your system.
* `uv` installed globally for environment management.

**1. Clone the repository:**
```bash
git clone https://github.com/AKSHAT0405/Unison.git
cd Unison
```

**2. Set up the virtual environment:**
```bash
uv venv
```
Activate it (Windows):
```bash
.venv\Scripts\activate
```

**3. Install dependencies:**
```bash
uv pip install -r requirements.txt
```

**4. Set up the database:**
```bash
python manage.py migrate
```

**5. Create an admin account (optional but recommended):**
```bash
python manage.py createsuperuser
```

**6. Run the local development server:**
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser to view the application.

## License
This project is open-source and available under the [MIT License](LICENSE).
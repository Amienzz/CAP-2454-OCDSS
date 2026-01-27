--- INITIAL ENVIRONMENT SETUP ---
If you are starting from scratch in a new folder:
1. Open PowerShell and navigate to the folder.
2. Create a folder named backend, then navigate to that
3. Create Virtual Environment:
   python -m venv venv
   
Every time you want to work on this, remember to:
1. Activate the Environment:
   .\venv\Scripts\activate
   (You should see '(venv)' appear in the prompt)

2. Install/Update Libraries:
   pip install -r requirements.txt (If you added any new dependencies, please add them there)

3. To run FastAPI
   python .\main.py

--- 3. TESTING THE API ---
- Open Browser to: http://0.0.0.0:8000/docs
- Use this Swagger UI to test POST and GET requests without 
  worrying about Windows 'curl' quote escaping issues.

--- 4. ENDING WORK ---
1. Stop the Server:
   Press 'Ctrl + C' in the terminal.

2. Exit the Virtual Environment:
   deactivate

--- 5. PROJECT FILES ---
- main.py: The Python code containing your FastAPI logic.
- requirements.txt: List of libraries needed for the project.
- venv/: The folder containing the app's local Python interpreter.

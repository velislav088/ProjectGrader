# AI-Powered Coding Personal Project Reviewer

## Project Grader is a tool designed to help developers analyze and refine their coding project ideas.

By leveraging LLaMA 3, this system evaluates a project idea and provides:

* Pros and cons of the idea
* Uniqueness, usability, and feasibility scores (graded F-S)
* Recommended technologies to use
* Solutions to eliminate cons
* Other QOL features that will be added in the future

This tool helps developers validate their ideas before committing to development, ensuring better project success.

## How it works

* The user submits a project idea along with a description, keywords, and realization plan.
* The AI (powered by LLaMA 3) analyzes the input and provides feedback.
* The system returns scores, pros/cons, and technology suggestions.
* Users can recieve brief recommendations on their projects so they can further improve it.

## How to run the project locally
Follow these steps to set up Project Grader locally on your machine:

1. Clone the repository - `git clone https://github.com/velislav088/ProjectGrader.git` `cd ProjectGrader`
2. Navigate to the Backend Folder - `cd backend`
3. Install Python Dependencies - `pip install -r requirements.txt` <br/>
This installs all the necessary backend libraries, including FastAPI, Uvicorn, and Ollama for interacting with LLaMA 3.
4. Install Ollama CLI (For LLaMA 3) <br/>
To interact with the LLaMA 3 model, you'll need the Ollama CLI.
* macOS - `brew install ollama`
* Windows - You can install Ollama via their website: [Ollama Downloads.](https://ollama.com/download)
* Linux - Follow the instructions on the [official Ollama website.](https://ollama.com/download)
5. Run the Backend server - `uvicorn app.main:app --reload`
6. Set Up the Frontend (React) - `cd ../frontend`
7. Install Frontend Dependencies - `npm install`
8. Start the Frontend Server - `npm run dev`

The frontend should now be running at http://localhost:5173.
Now that both the frontend and backend are running, open your browser and go to http://localhost:5173 to interact with the frontend.
The frontend will communicate with the backend at http://127.0.0.1:8000.

### Troubleshooting
* **CORS Issues**: If you run into CORS errors when the frontend tries to communicate with the backend, make sure FastAPI is configured with the correct CORS middleware. It should already be set up in the backend.
* **Ollama Not Working**: If you can't run the ollama command, ensure you have the Ollama CLI properly installed and available in your system's path. Check with ollama --version to verify.
* **Frontend/Backend Connection Issues**: If the frontend is not connecting to the backend, ensure both servers are running, and check that the backend URL is correctly set in the frontend code (usually in Axios or environment variables).

## Future plan
In the future I'm considering:
* Hosting the project on cloud
* Improve the efficiency of the algorithms
* Improve the UI/UX (right now it is in a very prototype phase)
* Store the data in a database to compare it to other projects and improve the AI instructions
  
The current version is a prototype one and I'm looking forward to make this project better in the future and achieve the future plan.

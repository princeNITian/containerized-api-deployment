Here’s a **README.md** file for your project:

```markdown
# Flask API with CI/CD to Google Cloud

This project is a simple Flask-based REST API that includes automated CI/CD pipelines using GitHub Actions. The application is containerized with Docker and deployed to **Google Container Registry (GCR)** and optionally to **Google Cloud Run**.

---

## Features

- REST API built with Flask
- Dockerized application for portability
- Automated CI/CD pipeline using GitHub Actions
- Pushes Docker images to Google Container Registry (GCR)
- (Optional) Deploys the app to Google Cloud Run

---

## Directory Structure

```
project/
├── app/
│   ├── __init__.py         # Initializes the Flask app
│   ├── main.py             # Contains routes and logic
├── Dockerfile              # Dockerfile to containerize the app
├── requirements.txt        # Python dependencies
├── run.py                  # Entry point to run the app
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions workflow for CI/CD
└── README.md               # This file
```

---

## Prerequisites

1. **Google Cloud Platform**:
   - A GCP project.
   - Enable **Google Container Registry (GCR)** and **Cloud Run**.
   - Create a Service Account with the following roles:
     - `Storage Admin` for GCR.
     - `Cloud Run Admin` for deployment (optional).
   - Download the Service Account JSON key.

2. **GitHub Secrets**:
   - Add the following secrets to your GitHub repository:
     - `GCP_SA_KEY`: Service Account key in JSON format.
     - `GCP_PROJECT_ID`: Your GCP Project ID.

3. **Local Development Tools**:
   - Python 3.11 or later.
   - Docker installed locally.

---

## Installation and Usage

### **Local Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-ci-cd.git
   cd flask-ci-cd
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app locally:
   ```bash
   python run.py
   ```
   Visit `http://127.0.0.1:5000` to access the API.

---

### **Containerization**

1. Build the Docker image:
   ```bash
   docker build -t flask-app .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 flask-app
   ```
   Visit `http://localhost:5000`.

---

### **CI/CD Pipeline**

1. Push your changes to the `main` branch to trigger the CI/CD workflow.
2. The GitHub Actions workflow will:
   - Lint and test the Python code.
   - Build the Docker image.
   - Push the Docker image to Google Container Registry (GCR).
   - (Optional) Deploy the app to Google Cloud Run.

---

## API Endpoints

| Method | Endpoint       | Description                         |
|--------|----------------|-------------------------------------|
| GET    | `/`            | Returns a welcome message.         |
| GET    | `/weather`     | Returns mock weather data.          |

### Example `/weather` Query
```bash
curl "http://127.0.0.1:5000/weather?city=NewYork"
```

Response:
```json
{
  "city": "NewYork",
  "temperature": "22°C",
  "status": "Sunny"
}
```

---

## Workflow Details

The GitHub Actions workflow (`.github/workflows/ci-cd.yml`) performs the following steps:
1. Lints and tests the code.
2. Builds and tags a Docker image.
3. Pushes the image to **Google Container Registry (GCR)**.
4. Deploys the app to **Google Cloud Run** (optional).

---

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Google Container Registry](https://cloud.google.com/container-registry)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

---

### Adjustments
- Replace `your-username` in the clone command with your GitHub username.
- Add a `LICENSE` file if you plan to release the project publicly.

Would you like help customizing this for your specific project?
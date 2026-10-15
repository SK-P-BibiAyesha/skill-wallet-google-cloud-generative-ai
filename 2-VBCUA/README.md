# 🎤 Voice-Based Concept Understanding Analyser (VBCUA)

An AI-powered educational assessment platform that evaluates a student's conceptual understanding through spoken explanations instead of simple keyword matching.

The system converts speech into text using **Faster Whisper**, compares the explanation with expert reference concepts using **Sentence-BERT**, derives similarity-based scores and result-based feedback, stores results in a SQLite database, and creates downloadable PDF reports.

---

# 📌 Project Overview

Voice-Based Concept Understanding Analyser (VBCUA) is designed to improve concept-based learning by evaluating the semantic meaning of a student's explanation rather than checking for exact words.

Students upload an audio explanation of one of the supported topics. The system performs speech transcription using Faster Whisper, semantic similarity using Sentence-BERT, keyword matching, similarity-based scoring, rule-based feedback, dashboard visualization, and PDF report generation.

---

# ✨ Features

- 🎤 Audio Upload
- 📝 Speech-to-Text using Faster Whisper
- 🧠 Semantic Similarity using Sentence-BERT
- 🔑 Keyword Matching
- 📊 Similarity-Based Score Calculation
- 💬 Feedback Based on the Analysis Result
- 📄 Downloadable PDF Reports
- 📈 Dashboard Analytics
- 💾 SQLite Database Storage
- 🎨 Responsive Streamlit Interface

Audio uploads are limited to 200 MB and accepted as WAV, MP3, M4A, OGG, or
WEBM. The app checks that the file signature matches its extension. Repeating
the same audio/topic analysis is blocked within the current session, with an
option to explicitly analyze it again.

---

# 📚 Supported Topics

The current version of VBCUA supports concept evaluation for:

- 🤖 Machine Learning
- ☁️ Cloud Computing
- 🧠 Artificial Intelligence
- 📊 Data Science
- 🗄️ Database Management System
- 💻 Operating System



# ⚙️ System Workflow

```text
Upload Audio
      │
      ▼
Speech Transcription
(Faster Whisper)
      │
      ▼
Load Reference Concept
      │
      ▼
Semantic Similarity
(Sentence-BERT)
      │
      ▼
Keyword Matching
      │
      ▼
Score Calculation
      │
      ▼
Result-Based Feedback
      │
      ▼
Store Results
(SQLite)
      │
      ▼
Generate PDF Report
      │
      ▼
Dashboard Analytics
```

---

# 🛠️ Technologies Used

## Programming

- Python
- Streamlit

## Artificial Intelligence

- Faster Whisper
- Sentence-BERT
- Transformers

## Database

- SQLite

## Libraries

- Librosa
- Torch
- Plotly
- Matplotlib
- ReportLab

---

# 📂 Project Structure

```text
2-VBCUA/
│
├── assets/
│   ├── images/
│   └── styles/
│       └── custom.css
│
├── audio/
│   ├── uploads/
│   ├── processed/
│   └── waveforms/
│
├── database/
│   ├── database.py
│   ├── database.db
│   └── queries.py
│
├── models/
│   ├── whisper_model.py
│   ├── semantic_model.py
│   ├── audio_analysis.py
│   ├── keyword_match.py
│   ├── scoring.py
│   └── feedback.py
│
├── pages/
│   ├── About.py
│   ├── Home.py
│   ├── Analyze_Audio.py
│   ├── Dashboard.py
│   └── Reports.py
│
├── reference_concepts/
│
├── reports/
│
├── tests/
│
├── utils/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/SK-P-BibiAyesha/skill-wallet-google-cloud-generative-ai.git
```

```bash
cd skill-wallet-google-cloud-generative-ai/2-VBCUA
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 🧪 Testing

The project includes unit tests for major modules.

```text
tests/
│
├── test_audio_analysis.py
├── test_whisper_model.py
├── test_semantic_model.py
├── test_keyword_match.py
├── test_audio_validation.py
├── test_history_reset.py
└── test_database.py
```

Run tests individually:

```bash
python tests/test_audio_analysis.py
```

```bash
python tests/test_whisper_model.py
```

```bash
python tests/test_semantic_model.py
```

```bash
python tests/test_keyword_match.py
```

```bash
python tests/test_database.py
```

The reset and upload validation tests use temporary, isolated data. Run them
without touching the application's saved report history:

```bash
python tests/test_history_reset.py
python tests/test_audio_validation.py
```

---

# 📊 Output

The application generates:

- Speech Transcript
- Semantic Similarity Score
- Keyword Matching Score
- Similarity-Based Overall Score
- Rule-Based Feedback
- Dashboard Analytics
- Downloadable PDF Report

---

# 🐳 Docker Deployment

The repository includes a CPU-based Docker image. Docker Engine must be installed
and running. Model weights are downloaded on first use, so the first analysis
requires outbound network access and may take longer than later analyses.

Build and run from the `2-VBCUA` directory:

```bash
docker build -t vbcua:local .
docker volume create vbcua-data
docker volume create vbcua-reports
docker volume create vbcua-model-cache
docker run --rm -p 8501:8501 `
  -v vbcua-data:/data `
  -v vbcua-reports:/app/reports `
  -v vbcua-model-cache:/home/vbcua/.cache/huggingface `
  vbcua:local
```

Open <http://localhost:8501>.

The `vbcua-data` volume persists the SQLite database across container
replacements. The application uses `/data/database.db` in the image. For a
local non-Docker install, it defaults to `database/database.db`; to select a
persistent location, set `VBCUA_DATABASE_PATH` to an absolute database file path
before starting Streamlit.
The `vbcua-reports` volume preserves generated PDF files across container
replacements.

PowerShell example:

```powershell
$env:VBCUA_DATABASE_PATH = "D:\vbcua-data\database.db"
python -m streamlit run app.py
```

Linux/macOS example:

```bash
export VBCUA_DATABASE_PATH=/var/lib/vbcua/database.db
python -m streamlit run app.py
```

**Hosting limitations:** the current application uses one local SQLite
database, has no user authentication, and Reset History clears the shared
history for every user of that deployment. Do not expose it as a public
multi-user service as-is. Streamlit Community Cloud does not provide durable
local-file storage for this database; use a managed database and object storage
with an application migration before deploying there. Do not run multiple
application replicas against a shared SQLite file. Protect the database volume
with backups and restrict access to the Docker host.

Reset History permanently deletes every `analysis_history` row in the active
database after an explicit confirmation. It does not remove generated PDFs,
audio files, or reference concepts.

# 🚀 Future Enhancements

- 🎙️ Live Voice Recording
- 🌍 Multi-language Support
- 🤖 AI Chatbot Tutor
- ☁️ Cloud Deployment
- 👨‍🎓 Student Login System
- 👨‍🏫 Teacher Dashboard
- 📈 Performance Prediction
- 📚 More Academic Subjects

---

# 👨‍💻 Developer

**SHAIK PATTA BIBI AYESHA**

Final Year B.Tech (Computer Science & Engineering)

VOICE-BASED CONCEPT UNDERSTANDING ANALYSER [VBCUA]


---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more details.



# 📷 Application Screenshots

<p align="center">
  <img src="assets/images/home.png" alt="Home Page" width="48%">
  <img src="assets/images/about.png" alt="About Page" width="48%">
</p>

<p align="center">
  <img src="assets/images/analyze.png" alt="Analyze Audio" width="48%">
  <img src="assets/images/dashboard.png" alt="Dashboard" width="48%">
</p>

<p align="center">
  <img src="assets/images/reports.png" alt="Reports" width="70%">
</p>
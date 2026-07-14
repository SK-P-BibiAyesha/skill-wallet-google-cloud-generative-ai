# VBCUA Test Suite

## Overview

This folder contains the unit tests for the **Voice-Based Concept Understanding Analyser (VBCUA)** project.

The purpose of these tests is to verify that the core modules of the application work correctly and produce the expected outputs.

---

## Test Files

### 1. test_audio_analysis.py

Tests the audio analysis module.

Verifies:

- Audio file loads successfully
- Duration is calculated correctly
- Speech rate is calculated
- Audio energy is computed
- Silence percentage is detected
- Output dictionary contains valid values

---

### 2. test_whisper_model.py

Tests the Faster Whisper speech recognition model.

Verifies:

- Audio transcription works
- Transcript is returned as a string
- Transcript is not empty
- Speech-to-text pipeline executes successfully

---

### 3. test_semantic_model.py

Tests the Sentence-BERT semantic similarity model.

Verifies:

- Similarity score is generated
- Score is within the valid range (0–100)
- Similar sentences receive a high similarity score

---

### 4. test_keyword_match.py

Tests the keyword matching module.

Verifies:

- Keywords are extracted correctly
- Matched keywords are identified
- Missing keywords are detected
- Matching score is calculated correctly

---

### 5. test_database.py

Tests the SQLite database module.

Verifies:

- Database connection is established
- Required table is created
- Database schema is accessible

---

## Sample Test File

The file **sample_audio.ogg** is used by multiple test cases for validating audio processing and speech transcription.

---

## Running Tests

Run each test individually from the project root.

Example:

```bash
python tests/test_audio_analysis.py
python tests/test_whisper_model.py
python tests/test_semantic_model.py
python tests/test_keyword_match.py
python tests/test_database.py
```

---

## Test Status

| Test | Status |
|-------|--------|
| Audio Analysis | ✅ Passed |
| Faster Whisper | ✅ Passed |
| Semantic Similarity | ✅ Passed |
| Keyword Matching | ✅ Passed |
| Database | ✅ Passed |

---

## Project

**Voice-Based Concept Understanding Analyser (VBCUA)**

Final Year Major Project

Developed using:

- Python
- Streamlit
- Faster Whisper
- Sentence-BERT
- SQLite
- Librosa
- ReportLab
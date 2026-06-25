<div align="center">

<img src="static/images/main-logo.png" alt="FlashCheck AI logo" width="120" />

# FlashCheck AI

**Marking attendance faster using an intelligent system.**

Face and voice recognition based attendance for classrooms — built with Streamlit and Supabase.

</div>

---

## Overview

FlashCheck AI is a web app that lets teachers take attendance by simply snapping a photo of the classroom (or recording a short audio clip) instead of calling out names one by one. Students enroll once with their face (and optionally their voice), and from then on the system recognizes them automatically.

It supports two kinds of users:

- **Teachers** — create subjects, share join codes/QR codes, take attendance via face or voice recognition, and view attendance history.
- **Students** — log in with FaceID, enroll in subjects using a code or QR scan, and track their own attendance record.

## How It Works

### Face Attendance
1. A teacher takes or uploads one or more classroom photos.
2. [dlib](http://dlib.net/) detects faces in each photo and computes a 128-d face embedding for every face found.
3. An SVM classifier (trained on embeddings of all registered students) predicts the identity behind each face.
4. A prediction is only accepted as a match if it falls within a distance threshold — this filters out false positives from students who aren't in the photo at all.
5. Every student enrolled in the subject is marked **Present** or **Absent** based on whether they were detected in any of the photos, and the teacher reviews/confirms the result before it's saved.

### Voice Attendance
1. The teacher records one continuous classroom audio clip (e.g. each student saying their name in turn).
2. The clip is split into speech segments using silence detection (`librosa`).
3. Each segment is converted into a voice embedding using [Resemblyzer](https://github.com/resemble-ai/Resemblyzer).
4. Each embedding is compared (cosine similarity) against the stored voice profiles of students enrolled in that subject, and matches above a similarity threshold are marked present.

### Student Login (FaceID)
Returning students simply look at the camera — their face is matched against the trained classifier and, if recognized, they're logged straight into their dashboard. New faces trigger a one-time registration flow (name + face capture + optional voice sample).

## Features

- 🧑‍🏫 **Teacher accounts** — username/password registration and login (passwords hashed with bcrypt)
- 📚 **Subject management** — create subjects with a code, name, and section
- 🔗 **Easy enrollment** — students join a subject via a subject code or by scanning a QR code (generated with `segno`)
- 📸 **Face attendance** — capture or upload classroom photos and auto-mark attendance
- 🎙️ **Voice attendance** — record classroom audio and auto-mark attendance from voice alone
- 🪪 **Face-based student login** — no passwords needed for students
- 📊 **Attendance records** — teachers see a class-by-class summary; students see their own per-subject stats
- ✅ **Review before save** — every auto-generated attendance sheet is shown to the teacher for confirmation before it's written to the database

## Tech Stack

| Layer | Technology |
|---|---|
| UI / App framework | [Streamlit](https://streamlit.io/) |
| Face detection & recognition | [dlib](http://dlib.net/), `face_recognition_models` |
| Face classification | scikit-learn (SVM) |
| Voice recognition | [Resemblyzer](https://github.com/resemble-ai/Resemblyzer), [librosa](https://librosa.org/) |
| Database / Backend | [Supabase](https://supabase.com/) (Postgres) |
| Auth (teachers) | bcrypt password hashing |
| QR codes | [segno](https://github.com/heuer/segno) |
| Image handling | Pillow, NumPy |
| Data tables | pandas |

## Project Structure

```
flashcheck-AI/
├── app.py                          # Entry point — routes between home/teacher/student screens
├── requirements.txt
├── static/images/                  # Logos used in the UI
└── src/
    ├── screens/
    │   ├── home_screen.py          # Landing page (choose Student or Teacher)
    │   ├── teacher_screen.py       # Teacher login/register + dashboard (attendance, subjects, records)
    │   └── student_screen.py       # FaceID login/registration + student dashboard
    ├── components/
    │   ├── header.py / footer.py
    │   ├── subject_card.py
    │   ├── dialog_create_subject.py     # Create a new subject
    │   ├── dialog_share_subject.py      # Share subject via link / QR code
    │   ├── dialog_enroll.py             # Student enrolls via subject code
    │   ├── dialog_auto_enroll.py        # Student auto-enrolls via QR/join link
    │   ├── dialog_add_photos.py         # Capture/upload classroom photos
    │   ├── dialog_voice_attendance.py   # Record & process classroom audio
    │   └── dialog_attendance_result.py  # Review & confirm attendance before saving
    ├── pipelines/
    │   ├── face_pipeline.py        # Face embeddings, SVM training, attendance prediction
    │   └── voice_pipeline.py       # Voice embeddings, speaker identification
    ├── database/
    │   ├── config.py               # Supabase client setup
    │   └── db.py                   # All database queries (teachers, students, subjects, attendance)
    └── ui/
        └── base_layout.py          # Shared page styling
```

## Database Schema

FlashCheck AI expects the following tables in your Supabase project:

- **`teachers`** — `teacher_id`, `username`, `password` (bcrypt hash), `name`
- **`students`** — `student_id`, `name`, `face_embedding` (array of floats), `voice_embedding` (array of floats, nullable)
- **`subjects`** — `subject_id`, `subject_code`, `name`, `section`, `teacher_id` (FK → teachers)
- **`subject_students`** — `student_id` (FK), `subject_id` (FK) — join table for enrollments
- **`attendance_logs`** — `student_id` (FK), `subject_id` (FK), `timestamp`, `is_present`

> You'll need to create these tables (with appropriate foreign keys) in your own Supabase project before running the app.

## Getting Started

### Prerequisites

- Python 3.10+
- A [Supabase](https://supabase.com/) project (free tier works) with the tables described above
- `cmake` and a C++ build toolchain installed on your system (required to build `dlib`)

### 1. Clone the repository

```bash
git clone https://github.com/HarshSrivastava10/flashcheck-AI.git
cd flashcheck-AI
```

### 2. Create a virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

> **Note:** `dlib-bin` provides prebuilt wheels for most platforms. If installation fails on your system, you may need to install `dlib` from source, which requires `cmake` and a C++ compiler.

### 3. Configure Supabase secrets

Create a `.streamlit/secrets.toml` file in the project root (this is git-ignored):

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-api-key"
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Usage

1. **Teachers:** Register an account → create a subject → share the subject code/QR with students → use **Take Attendance** to capture photos or audio for a session → review and confirm the results.
2. **Students:** Open the app → register your face (and optionally voice) on first use → enroll in subjects using the code/QR your teacher shares → log in with FaceID on future visits and track your attendance from your dashboard.

## Limitations & Notes

- Face/voice matching relies on similarity thresholds (`0.6` for face, `0.65` for voice cosine similarity) — accuracy depends on lighting, camera quality, and audio clarity.
- This project is intended as a demo/learning project for biometric attendance systems rather than a production-grade security solution.
- Biometric data (face and voice embeddings) is stored in your Supabase database — handle this responsibly and in compliance with applicable privacy laws if you deploy this beyond a personal/educational context.

## Author

Built by [Harsh Srivastava](https://github.com/HarshSrivastava10).

# PDF Merger Tool

A simple web app built with Streamlit to merge multiple PDF files. <br>
Users can upload PDFs, reorder them via drag-and-drop, and download the merged file.

## Features

- Upload multiple PDF files
- Drag-and-drop to reorder before merging
- Merge all PDFs into a single file
- Instant download of merged PDF
- All processing is done in-memory — files are not stored on server

## Tech Stack

- Streamlit (UI framework)
- PyPDF2 (PDF merging)
- streamlit-sortables (Drag-and-drop ordering)

## Project Structure

```md
pdf-merger/
│── app.py              
│── requirements.txt    
│── README.md           

```

## Installation

Clone the project:

```bash
git clone https://github.com/Saumyajeet-Varma/PDF-Merger-Streamlit
cd pdf-merger

```

Create a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate 

```

Install dependencies:

```bash
pip install -r requirements.txt

```

Run the app:

```bash
streamlit run app.py

```

> Open http://localhost:8501

## Contributing

- Fork the repo
- Create your feature branch (git checkout -b feature-name)
- Commit changes (git commit -m 'Add some feature')
- Push to branch (git push origin feature-name)
- Open a Pull Request

## Author

- **Saumyajeet Varma**: [GitHub](https://github.com/Saumyajeet-Varma)
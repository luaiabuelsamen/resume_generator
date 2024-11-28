# README: Resume Tailoring Tool

## Overview

This tool helps automate the process of tailoring a resume to a specific job posting. By using a language model (like GPT-4), it subtly adjusts your resume’s language to better align with the job description, ensuring it retains its original format and integrity.

## Features

- Tailors the content of a LaTeX-formatted resume based on a job posting.
- Modifies skills and experience descriptions to match keywords from the job posting.
- Preserves the original resume's structure and formatting.
- Saves the tailored resume in LaTeX format, ready to be compiled into a PDF.

## Requirements

- Python 3.7+
- `langchain`, `openai`, `python-dotenv`, and `argparse` libraries
- LaTeX installed for compiling the `.tex` file into a PDF
- OpenAI API key (ensure your OpenAI key is set in a `.env` file)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repository/resume-tailoring.git
   cd resume-tailoring
   ```

2. **Install Dependencies:**

   Use `pip` to install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Ensure LaTeX is Installed:**

   You need to have LaTeX installed on your machine to compile `.tex` files to PDF. Install it with:

   - **Mac**: `brew install --cask mactex`
   - **Linux**: `sudo apt-get install texlive`
   - **Windows**: Install from [MiKTeX](https://miktex.org/download).

## Usage

### Command-Line Interface

The script uses the following command-line arguments:

- `--original_resume`: Path to the original LaTeX resume file (default: `input/original_resume.tex`).
- `--job_posting`: Path to the job posting text file (default: `input/job_posting.txt`).
- `--output_resume`: Path to save the tailored LaTeX resume (default: `output/tailored_resume.tex`).

### Example Command

To tailor a resume for a specific job posting and compile it into a PDF, run the following command:

```bash
python main.py --original_resume input/my_resume.tex --job_posting input/job_posting.txt --output_resume output/tailored_resume.tex
```

This will:

1. Tailor your resume (`input/my_resume.tex`) using the job posting (`input/job_posting.txt`).
2. Save the tailored resume in LaTeX format at `output/tailored_resume.tex`.
3. Automatically compile the tailored LaTeX file into a PDF.

### Compilation

Once the tailored resume is saved as a `.tex` file, the script will automatically compile it into a PDF using `pdflatex`.

You can manually compile the `.tex` file by running:

```bash
pdflatex output/tailored_resume.tex
```

## How It Works

1. **Read the Original Resume**: The `.tex` resume file is read.
2. **Tailor the Resume**: The model generates tailored sections by aligning the language with the job posting.
3. **Save the Tailored Resume**: The updated LaTeX content is saved in a new `.tex` file.
4. **Compile to PDF**: The `.tex` file is compiled to a PDF.

## Example Workflow

1. **Prepare your resume** in `.tex` format and save it in the `input/` directory.
2. **Prepare the job posting** text and save it as `job_posting.txt` in the `input/` directory.
3. Run the command to tailor the resume and generate the PDF.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

- If you encounter errors related to LaTeX, ensure that LaTeX is properly installed and configured on your system.
- Make sure your OpenAI API key is valid and correctly set in the `.env` file.
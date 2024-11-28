import os
from agent import generate_resume
import argparse

def compile_tex_to_pdf(tex_file):
    print("Compiling .tex file to PDF...")
    os.system(f"pdflatex {tex_file}")
    print("PDF generated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process resume and job posting paths.')
    
    parser.add_argument(
        '--original_resume', 
        type=str, 
        default='input/original_resume.tex', 
        help='Path to the original resume (default: "original_resume.tex")'
    )
    parser.add_argument(
        '--output_resume', 
        type=str, 
        default='output/tailored_resume.tex', 
        help='Path for the output resume (default: "output_resume.tex")'
    )
    parser.add_argument(
        '--job_posting', 
        type=str, 
        default='input/job_posting.txt', 
        help='Path to the job posting (default: "job_posting.txt")'
    )
    
    args = parser.parse_args()
    generate_resume(args.original_resume, args.job_posting, args.output_resume)
    compile_tex_to_pdf(args.output_resume)
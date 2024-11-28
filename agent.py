import os
from typing import List, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import re

load_dotenv()

class ResumeTailoringAgent:
    def __init__(self, llm_model: str = "gpt-4-turbo"):
        """
        Initialize the Resume Tailoring Agent
        
        :param llm_model: OpenAI language model to use
        """
        self.llm = ChatOpenAI(temperature=0.3)
    
    def _read_tex_file(self, file_path: str) -> str:
        """
        Read the contents of a .tex file
        
        :param file_path: Path to the LaTeX resume file
        :return: Contents of the file as a string
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def _extract_resume_sections(self, tex_content: str) -> Dict[str, str]:
        """
        Extract key sections from the LaTeX resume
        
        :param tex_content: Full LaTeX resume content
        :return: Dictionary of resume sections
        """
        return tex_content
    
    def _create_tailoring_prompt(self) -> ChatPromptTemplate:
        """
        Create a prompt for tailoring the resume
        
        :param resume_sections: Extracted resume sections
        :param job_posting: Job posting text
        :return: Constructed prompt template
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert resume tailoring assistant. Your task is to subtly modify a resume 
            to better align with a specific job posting while maintaining the original resume's integrity.

            Key Guidelines:
            1. Preserve the original resume's structure and overall content
            2. Slightly modify skills and work experience bullet points
            3. Ensure each bullet point remains 1 line (80-120 characters)
            4. Use keywords from the job posting strategically
            5. Do not add new sections or dramatically change the resume's layout

            Please provide a modified LaTeX resume section that:
            - Uses more relevant language from the job posting
            - Subtly highlights skills that match the job requirements
            - Maintains the original formatting and structure"""),
            ("human", "Tailor the resume for this job posting")
        ])
        
        return prompt
    
    def tailor_resume(self, resume_path: str, job_posting: str) -> str:
        """
        Main method to tailor the resume
        
        :param resume_path: Path to the original resume .tex file
        :param job_posting: Text of the job posting
        :return: Tailored resume content
        """
        original_tex = self._read_tex_file(resume_path)
        
        # Create tailoring prompt
        prompt = self._create_tailoring_prompt()
        
        # Create output parser
        output_parser = StrOutputParser()
        
        # Create chain
        chain = prompt | self.llm | output_parser
        
        # Generate tailored resume sections
        tailored_tex = chain.invoke({
            'resume': original_tex,
            'job_description': job_posting
        })
        
        return tailored_tex
    
    def save_tailored_resume(self, tailored_tex: str, output_path: str):
        """
        Save the tailored resume to a new .tex file
        
        :param tailored_tex: Tailored LaTeX resume content
        :param output_path: Path to save the tailored resume
        """
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(tailored_tex)

def generate_resume(original_resume_path, job_posting_path, output_resume_path):
    agent = ResumeTailoringAgent()
    
    # Read job posting
    with open(job_posting_path, 'r', encoding='utf-8') as file:
        job_posting = file.read()
    
    # Tailor resume
    tailored_resume = agent.tailor_resume(original_resume_path, job_posting)
    
    # Save tailored resume
    agent.save_tailored_resume(tailored_resume, output_resume_path)
    
    print("Resume tailoring completed successfully!")
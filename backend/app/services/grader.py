import ollama
import json
import re
from app.models.schemas import ProjectIdea, GradingResponse

def grade_project(project: ProjectIdea) -> GradingResponse:
    """Calls LLaMA 3 to analyze the project idea and return structured feedback."""
    
    prompt = f"""
    Please evaluate the following project idea using the tier system (F-S) and provide constructive feedback:
    - Provide pros, cons, improvement tips, and difficulty level.
    - The difficulty level should reflect the experience needed to build the project.
    - Please grade the project based on feasibility, technological stack, potential scalability, and overall impact.
    
    Return your answer in the following **valid JSON format** with no additional text:
    {{
        "tier": "F",  # Project grade (F-S)
        "pros": ["list", "of", "pros"],  # Positive aspects of the project
        "cons": ["list", "of", "cons"],  # Negative aspects or challenges
        "improvement_tips": ["list", "of", "suggestions"],  # Tips for improvement
        "difficulty": "string"  # Difficulty level (e.g., Beginner, Intermediate, Advanced)
    }}

    **Title:** {project.title}
    **Description:** {project.description}
    **Keywords:** {", ".join(project.keywords)}
    """

    # Call LLaMA 3 for grading
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    ai_response = response["message"]["content"]

    print("Raw AI Response:", ai_response)  # Temporary debugging

    # Extract the JSON response from uneccessary information using regex
    match = re.search(r"\{.*\}", ai_response, re.DOTALL)
    if match:
        json_string = match.group(0)  # Get only the JSON part
        try:
            # Attempt to load the JSON string
            parsed_data = json.loads(json_string)
            
            # Ensure all necessary keys are present
            required_keys = ['tier', 'pros', 'cons', 'improvement_tips', 'difficulty']
            if all(key in parsed_data for key in required_keys):
                return GradingResponse(**parsed_data)  # Return as Pydantic model
            else:
                print("Missing keys in the response.")
        except json.JSONDecodeError:
            print("Failed to decode JSON.")

    return GradingResponse(
        tier="Error",
        pros=[],
        cons=[],
        improvement_tips=["Failed to parse or validate AI response"],
        difficulty="Unknown"
    )

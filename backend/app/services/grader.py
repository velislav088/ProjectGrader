import ollama
import json
import re
from app.models.schemas import ProjectIdea, GradingResponse

def grade_project(project: ProjectIdea) -> GradingResponse:
    """Calls LLaMA 3 to analyze the project idea and return structured feedback."""
    
    prompt = f"""
    Please evaluate the following project idea using the tier system (F-S) and provide structured feedback:
    - Grade the project based on **feasibility, technological stack, scalability, innovation, and real-world impact**.
    - Provide at **least 3 pros and 3 cons**, but include **more if applicable**.
    - Improvement tips must be **detailed**, explaining how they enhance the project.
    - Focus on **how this project can be unique** compared to existing solutions, highlighting its **distinctive features** or innovations.
    - Compare this project to **existing solutions** in the healthcare/AI field, and explain whether it offers a **unique advantage** over these.

    ### Grading Criteria:
    - **S-Tier**: Highly innovative, feasible at scale, fills a market gap, strong use of cutting-edge technology.
    - **A-Tier**: Very strong, feasible but may require refinement, competitive in existing markets.
    - **B-Tier**: Good idea but **lacks uniqueness** or has **scalability concerns**.
    - **C-Tier or Lower**: Major issues in feasibility, execution, or practical use.

    Return your answer in **valid JSON format** with no extra text:
    {{
        "overall_grade": "F",  # Project grade (F-S)
        "usability": "F",  
        "uniqueness": "F",  
        "complexity": "F",  
        "pros": ["At least 3 positive aspects, can be more"],  
        "cons": ["At least 3 negative aspects, can be more"],  
        "improvement_tips": [
            "Each tip must be **at least one sentence long**, explaining how it improves the project."
        ],
        "difficulty": "string"  
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
            required_keys = ['overall_grade', 'usability', 'uniqueness', 'complexity', 'pros', 'cons', 'improvement_tips', 'difficulty']
            if all(key in parsed_data for key in required_keys):
                return GradingResponse(**parsed_data)  # Return as Pydantic model
            else:
                print("Missing keys in the response.")
        except json.JSONDecodeError:
            print("Failed to decode JSON.")

    return GradingResponse(
        overall_grade="Error",
        usability="Error",
        uniqueness="Error",
        complexity="Error",
        pros=[],
        cons=[],
        improvement_tips=["Failed to parse or validate AI response"],
        difficulty="Unknown"
    )

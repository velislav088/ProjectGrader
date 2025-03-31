import { useState } from "react";
import { gradeProject } from "./api/graderApi";

function App() {
    const [idea, setIdea] = useState("");
    const [result, setResult] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const projectData = { idea };
        const response = await gradeProject(projectData);
        setResult(response);
    };

    return (
        <div className="container">
            <h1>Project Grader</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={idea}
                    onChange={(e) => setIdea(e.target.value)}
                    placeholder="Describe your project idea..."
                    required
                />
                <button type="submit">Grade My Project</button>
            </form>

            {result && (
                <div className="result">
                    <h2>Grade: {result.tier}</h2>
                    <p><strong>Pros:</strong> {result.pros.join(", ")}</p>
                    <p><strong>Cons:</strong> {result.cons.join(", ")}</p>
                    <p><strong>Improvement Tips:</strong> {result.improvement_tips.join(", ")}</p>
                    <p><strong>Difficulty:</strong> {result.difficulty}</p>
                </div>
            )}
        </div>
    );
}

export default App;

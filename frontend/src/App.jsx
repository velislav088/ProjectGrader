import { useState } from "react";
import axios from "axios";
import "./styles/app.css";

function App() {
	const [title, setTitle] = useState("");
	const [description, setDescription] = useState("");
	const [keywords, setKeywords] = useState("");
	const [response, setResponse] = useState(null);
	const [error, setError] = useState(null);

	const handleSubmit = async (e) => {
		e.preventDefault();
		setError(null);

		const projectData = {
			title,
			description,
			keywords: keywords.split(",").map((word) => word.trim()),
		};

		try {
			const res = await axios.post("http://127.0.0.1:8000/grade", projectData);
			setResponse(res.data);
		} catch (err) {
			setError("Failed to fetch response. Please try again.");
		}
	};

	return (
		<div className="background">
			<h1>AI Project Grader</h1>
			<h2>Improve your coding project ideas using artificial intelligence</h2>

			<form onSubmit={handleSubmit}>
				<input
					type="text"
					placeholder="Project Title"
					value={title}
					onChange={(e) => setTitle(e.target.value)}
					required
				/>
				<textarea
					placeholder="Project Description"
					value={description}
					onChange={(e) => setDescription(e.target.value)}
					required
				/>
				<input
					type="text"
					placeholder="Keywords (comma-separated)"
					value={keywords}
					onChange={(e) => setKeywords(e.target.value)}
					required
				/>
				<button type="submit">Grade Project</button>
			</form>

			{error && <p className="error">{error}</p>}

			{response && (
				<div className="response">
					<h3>Overall Grade: {response.overall_grade}</h3>
					<p><strong>Usability:</strong> {response.usability}</p>
					<p><strong>Uniqueness:</strong> {response.uniqueness}</p>
					<p><strong>Complexity:</strong> {response.complexity}</p>
					<p><strong>Pros:</strong> {response.pros.join(", ")}</p>
					<p><strong>Cons:</strong> {response.cons.join(", ")}</p>
					<p><strong>Improvement Tips:</strong> {response.improvement_tips.join(", ")}</p>
					<p><strong>Difficulty:</strong> {response.difficulty}</p>
				</div>
			)}
		</div>
	);
}

export default App;

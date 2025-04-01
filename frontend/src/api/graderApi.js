import axios from "axios";

const gradeProject = async (projectData) => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/grade", projectData, {
            headers: {
                "Content-Type": "application/json",
            },
        });

        console.log("Server Response:", response.data);
        return response.data;
    } catch (error) {
        console.error("Error grading project:", error.response ? error.response.data : error.message);
    }
};

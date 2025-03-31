import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const gradeProject = async (projectData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/grade`, projectData);
        return response.data;
    } catch (error) {
        console.error('Error grading project:', error);
        return null;
    }
};

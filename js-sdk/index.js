const axios = require("axios");

class PythonAgent {
    constructor(baseURL = "http://localhost:8000") {
        this.api = axios.create({ baseURL });
    }

    async analyzeText(text) {
        try {
            const response = await this.api.post("/analyze", { text });
            return response.data;
        } catch (error) {
            console.error("Error analyzing text:", error);
            return null;
        }
    }
}

module.exports = PythonAgent;

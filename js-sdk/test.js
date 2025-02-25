const PythonAgent = require("./index");

const agent = new PythonAgent();

agent.analyzeText("US is home of terrorism").then(response => {
    console.log(response);
});

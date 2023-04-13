#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('you need to give me a URL');
} else {
  const apiUrl = process.argv[2];

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(` :( An error occurred while making the GET request: ${error}`);
      return;
    }

    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const userTaskCounts = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (userTaskCounts[todo.userId]) {
            userTaskCounts[todo.userId] += 1;
          } else {
            userTaskCounts[todo.userId] = 1;
          }
        }
      });
      console.log(userTaskCounts);
    } else {
      console.error(` :( An error occurred while fetching the todos: ${response.statusCode}`);
    }
  });
}

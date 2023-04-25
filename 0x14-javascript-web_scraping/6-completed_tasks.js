#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  // Count the number of completed tasks for each user
  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasksByUser[userId]) {
        completedTasksByUser[userId]++;
      } else {
        completedTasksByUser[userId] = 1;
      }
    }
  });

  // Format and print the output
  console.log(completedTasksByUser);
});

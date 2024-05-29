#!/usr/bin/node

// This script computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
const completedTasks = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    }
  }
  console.log(completedTasks);
});

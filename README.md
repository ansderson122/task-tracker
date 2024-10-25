# Task Tracker CLI

Task Tracker is a simple command-line interface (CLI) project for tracking and managing your tasks. This application allows you to add, update, and delete tasks, as well as mark tasks as in progress or completed.

## Features

- Add, update, and delete tasks.
- Mark tasks as "in-progress" or "done".
- List all tasks.
- List completed tasks.
- List incomplete tasks.
- List tasks in progress.

## Task Properties

Each task has the following properties:

- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

## Prerequisites

Make sure you have Python installed on your system. You can download Python [here](https://www.python.org/downloads/).

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory in the terminal.

```bash
git clone <repository-link>
cd task-tracker
```
## Command Explanation

This section provides an overview of each command available in the Task Tracker CLI, along with their usage and functionality.

### 1. Adding a New Task
```bash
task-cli add "Task description"
```
This command allows you to add a new task to the task list. The task will be assigned a unique ID automatically.

### 2. Updating a Task
```bash
task-cli update <id> "New task description"
```
This command updates the description of an existing task identified by its ID. You need to provide both the ID and the new description.

### 3. Deleting a Task
```bash
task-cli delete <id>
```
This command deletes a task from the task list based on its ID.

### 4. Marking a Task as In Progress or Done
```bash
task-cli mark-in-progress <id>
```
This command changes the status of a task to "in-progress", indicating that work on this task has started.

```bash
task-cli mark-done <id>
```
This command marks a task as completed. The status of the task will be updated to "done".

### 5. Listing All Tasks
```bash
task-cli list
```
This command displays all tasks in the task list, regardless of their status.

### 6. Listing Tasks by Status
```bash
task-cli list <status>
```
This command allows you to filter and display tasks based on their status. You can specify one of the following statuses: `todo`, `in-progress`, or `done`.
// Initialize Firebase with your config
firebase.initializeApp({
  apiKey: "AIzaSyC75AsnOSf4PJ9R_do6M_of7iuTsvY_qwI",
  authDomain: "to-do-app-8281f.firebaseapp.com",
  projectId: "to-do-app-8281f",
  storageBucket: "to-do-app-8281f.appspot.com",
  messagingSenderId: "292994092471",
  appId: "1:292994092471:web:c88020392a55a1d8b02c32",
});

const db = firebase.firestore();

// Function to add a task
function addTask() {
  const taskInput = document.getElementById("task-input");
  const task = taskInput.value.trim();
  if (task !== "") {
    db.collection("tasks").add({
      task: task,
      timestamp: firebase.firestore.FieldValue.serverTimestamp(),
    });
    taskInput.value = "";
    console.log("Task added successfully");
  }
}

// Function to render tasks

function renderTasks(doc) {
  const taskList = document.getElementById("task-list");
  const taskItem = document.createElement("li");
  taskItem.className = "task-item";
  taskItem.innerHTML = `
    <span>${doc.data().task}</span>
    <button onclick="deleteTask('${doc.id}')">Delete</button>
    `;
  taskList.appendChild(taskItem);
}

// Real-time listener for tasks
db.collection("tasks")
  .orderBy("timestamp", "desc")
  .onSnapshot((snapshot) => {
    const changes = snapshot.docChanges();
    changes.forEach((change) => {
      if (change.type === "added") {
        renderTasks(change.doc);
      }
    });
  });

// Function to delete a task

function deleteTask(id) {
  db.collection("tasks")
    .doc(id)
    .delete()
    .then(() => {
      // Get the task list element
      var taskList = document.getElementById("task-list");

      // Clear the task list
      while (taskList.firstChild) {
        taskList.removeChild(taskList.firstChild);
      }
    });
    console.log("Task deleted successfully");
}

//https://to-do-app-8281f.web.app
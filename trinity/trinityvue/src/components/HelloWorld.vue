

<template>

<div id="app">
    <h1 class="title">
      
      Vuengo
    
    </h1> <!-- Page title -->
    
    <ul >
      <li v-for="task in tasks" :key="task.username">
        {{task.username}}
      </li>
    </ul>



<table>
    <tr>
        <th>User Name</th>
        <th>First Name</th> 
        <th>Last Name</th>
        <th>Security Group</th>
    </tr>

    <tr v-for="task in tasks" :key="task.username"> 
      <td>{{task.username}}</td>
      <td>{{task.firstname}}</td>
      <td>{{task.lastname}}</td>
      <td>{{task.securitygroup}}</td>
    </tr>
 

</table>
  

  {{tasks}}



</div>




</template>

<script>
import axios from 'axios';

let url = "http://127.0.0.1:8000/trinity/users/?format=json"

export default {
  name: 'HelloWorld',
  data () {
    return {
      tasks: null // Array for holding the tasks
    }
  },
  mounted () { // This will be called when HelloWorld is loaded
    this.getTasks(); // Call our getTasks function below
  },
  methods: {
    getTasks() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/trinity/users/',
            auth: {
                username: 'geob3d',
                password: 'C@mera12'
            }
        }).then(response => this.tasks = response.data);
    }
  }
}
  

    
  

</script>


<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done { /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>
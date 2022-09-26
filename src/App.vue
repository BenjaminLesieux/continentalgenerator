<template>
  <div id="nav">
    <img id="logo" src="../src/assets/continental.png" alt="continental">
    <router-link class="router" to="/">Generate Menu</router-link>
    <router-link class="router" to="/edit">Edit Menu</router-link>
  </div>
  <router-view></router-view>
</template>

<script>

export default {
  name: 'App',
  components: {

  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;

  background-color: black;
}

#logo {
  height: 50px;
}

#nav {

  position: sticky;
  top: 0;

  width: 100%;
  height: 110px;

  background-color: black;

  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

.router {
  text-decoration: none;
  color: beige;
}

.router:hover {
  cursor: pointer;
  color: navajowhite;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<template>
  <div>
    <div id="content">
      <p>{{name}}</p>
      <p style="font-size: 8px; font-style: italic">{{desc}}</p>
      <p>{{price}} euros</p>

      <button id="edit-button">✏</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuItem",
  props: {
    name: String,
    price: Number,
    desc: String
  }
}
</script>

<style scoped>
#content {
  color: wheat;

  height: 50px;
  width: 350px;
  background-color: white;

  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;

  margin-bottom: 10px;

  border-radius: 10px;
}

p {
  color: black;
  background-color: white;
}

button {
  height: 40px;
  width: 40px;

  border-radius: 50%;

  background-color: navajowhite;
  border: none;
}

button:hover {
  cursor: pointer;
}
</style>
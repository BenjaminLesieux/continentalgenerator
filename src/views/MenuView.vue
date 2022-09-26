<template>
  <div id="sections">
    <div :id="drink" v-for="drink in Object.keys(menu)" :key="drink">
      <h1 style="color: white; margin-bottom: 5px ">{{drink}}</h1>
      <div id="drink-container">
        <div id="menu-item" v-for="drinkName in Object.keys(menu[drink])" :key="drinkName">
          <MenuItem
              :name="drinkName"
              :desc="menu[drink][drinkName].desc"
              :price="menu[drink][drinkName].price"
          ></MenuItem>
        </div>
        <button id="add-button" :class="drink" @click="addMenuItem">+</button>
      </div>
    </div>
  </div>
</template>

<script>
import MenuItem from "@/components/MenuItem";

export default {
  name: "MenuView",
  components: {
    MenuItem
  },
  data() {
    return {
      menu: {

      }
    }
  },
  mounted() {
    this.menu = this.getMenu()
    console.log(this.menu)
  },
  methods: {
    getMenu() {
      return new Object(require("../assets/menu.json"))
    },
    addMenuItem(e) {
      const section = e.target.className
      console.log(section)

      const addition = {
        name: "Template",
        desc: "Template",
        price: 3.5
      }

      console.log("hello, world " + addition)
    }
  },
}
</script>

<style scoped>
#sections {
  height: 100vh;

  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: space-around;
}

#drink-container {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: wrap;
}

#drink-container:hover {
  cursor: pointer;
}

#add-button {
  height: 60px;
  width: 60px;

  border-radius: 50%;

  background-color: green;

  margin-bottom: 10px;
}

#add-button:hover {
  cursor: pointer;
}

#menu-item {
  margin-right: 10px;
}
</style>
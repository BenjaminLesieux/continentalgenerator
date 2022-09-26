import {createApp}  from 'vue'
import App from './App.vue'
import {routes} from "@/routes";
import {createRouter, createWebHashHistory} from "vue-router";


// eslint-disable-next-line no-undef
const router = createRouter({
    history: createWebHashHistory(),
    routes
})
createApp(App)
    .use(router)
    .mount('#app')


import {defineStore} from "pinia";
import {ref} from "vue";

const useEditingStore = defineStore('editing',() => {
    const editing = ref(false)

    function toggleEditing() {
        this.editing = !this.editing
    }

    return {editing, toggleEditing}
})
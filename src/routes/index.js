import MenuView from "@/views/MenuView";
import EditMenuView from "@/views/EditMenuView";

export const routes = [
    {
        path: '/', component: MenuView,
    },
    {
        path: '/edit', component: EditMenuView
    }
]
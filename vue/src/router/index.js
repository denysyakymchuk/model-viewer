import { createRouter, createWebHistory } from "vue-router";
import MainModelView from "@/views/MainModelView.vue";
import AdminView from "@/views/AdminView.vue";

const routes = [
    {
        path: "/",
        name: "home",
        meta: { layout: "main" },
        component: MainModelView,
    },
    {
        path: "/admin",
        name: "admin",
        meta: { layout: "admin" },
        component: AdminView,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;

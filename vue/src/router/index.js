import { createRouter, createWebHistory } from "vue-router";
import MainModelView from "@/views/MainModelView.vue";
import AdminView from "@/views/AdminView.vue";
import LoginView from "@/views/LoginView.vue";
import store from "@/store";
import NotFoundView from "@/views/error/NotFoundView.vue";
import SharedPageComponent from "@/views/SharedPageComponent.vue";
import TestPageComponent from "@/views/TestPageComponent.vue";

const routes = [
    {
        path: "/",
        name: "home",
        meta: { layout: "main" },
        component: MainModelView,
    },
    {
        path: "/model/:id",
        name: "model",
        meta: { layout: "main" },
        props:true,
        component: SharedPageComponent,
    },
    {
        path: "/test",
        name: "test",
        meta: { layout: "main" },
        component: TestPageComponent,
    },
    {
        path: "/admin",
        name: "admin",
        meta: { layout: "admin" },
        component: AdminView,
        beforeEnter: (to, from, next) => {
            if (store.getters.TOKEN) {
                next();
            } else {
                next({ name: 'login' });
            }
        },
    },
    {
        path: "/login",
        name: "login",
        meta: { layout: "main" },
        component: LoginView,
        beforeEnter: (to, from, next) => {
            if (!store.getters.TOKEN) {
                next();
            } else {
                next({ name: 'admin' });
            }
        },
    },
    {
        path: "/logout",
        name: "logout",
        beforeEnter: (to, from, next) => {
            next({ name: 'home' });
        },
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: NotFoundView
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});


export default router;

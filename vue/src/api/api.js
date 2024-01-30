import axios from "axios";
import store from "@/store";
const api = axios.create({
    baseURL: `http://localhost:90/api`,
});

api.interceptors.request.use(
    (config) => {
        if (store.getters.TOKEN) {
            config.headers['Authorization'] = 'Bearer ' + store.getters.TOKEN;
        }
        if (config.url.endsWith('/login') || config.url.match('/login/[0-9]')) {
        config.headers["Content-Type"] = 'application/x-www-form-urlencoded'
        } else {
            config.headers["Content-Type"] = 'application/json'
        }
        config.headers["Accept"] = "application/json";
        return config;
    },
    (error) => {
        Promise.reject(error);
    }
);

export default api;

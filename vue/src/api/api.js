import axios from "axios";
import store from "@/store";
const api = axios.create({
    // baseURL: `https://modelviewer.pl/api/v1`,
    baseURL: `http://localhost/api/v1`,
});

api.interceptors.request.use(
    (config) => {
        if (store.getters.TOKEN) {
            config.headers['Authorization'] = 'Token  ' + store.getters.TOKEN;
        }

        config.headers["Accept"] = "application/json";
        return config;
    },
    (error) => {
        Promise.reject(error);
    }
);

export default api;

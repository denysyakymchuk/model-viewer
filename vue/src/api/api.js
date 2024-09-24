import axios from "axios";
import store from "@/store";

// MODE
let baseURL;

if (process.env.NODE_ENV === "production") {
    baseURL = "https://modelviewer.pl/api/v1";
} else {
    baseURL = "http://localhost/api/v1";
}

const api = axios.create({
    baseURL: baseURL,
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

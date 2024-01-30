import axios from "axios";
const api = axios.create({
    baseURL: `http://localhost:90/api`,
});

api.interceptors.request.use(
    (config) => {
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

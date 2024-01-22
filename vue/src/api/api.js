import axios from "axios";
const api = axios.create({
    baseURL: `http://localhost:90/api`,
});

api.interceptors.request.use(
    (config) => {
        config.headers["Content-Type"] = "application/json";
        config.headers["Accept"] = "application/json";
        return config;
    },
    (error) => {
        Promise.reject(error);
    }
);

export default api;

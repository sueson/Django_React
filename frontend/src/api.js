import axios from 'axios';
import { ACCESS_TOKEN } from "./constants";


const api = axios.create({ 
    baseURL: import.meta.env.VITE_API_URL,
});

// This interceptor adds an Authorization header with a Bearer token to each request if a token is found in local storage.
api.interceptors.request.use( // interceptors means that we can intercept the request before it is sent to the server and modify it.
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);


export default api;
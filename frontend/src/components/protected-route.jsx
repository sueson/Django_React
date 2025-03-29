import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import { useEffect, useState } from "react";


function ProtectedRoute({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    useEffect(() => { 
        auth().catch(() => setIsAuthorized(false));  
    }, []); 

    const refreshToken = async () => { // Gets a new token if the current token has expired
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);

        try {
            const response = await api.post("/api/token/refresh/", { refresh: refreshToken }); // Sends a request to the server to get a new token

            if(response.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, response.data.access); // Stores the new token in local storage
                setIsAuthorized(true);
            }
            else {
                setIsAuthorized(false);
            }

        } catch (error) {
            console.log(error);
            setIsAuthorized(false);
        }
    };

    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if(!token) {
            setIsAuthorized(false);
            return;
        };

        const decoded = jwtDecode(token);
        const tokenExpiration = decoded.exp  // Gets the expiration date of the token in seconds 
        const now = Date.now() / 1000;  // Gets Date in seconds not in milliseconds

        if(tokenExpiration < now) {  // If the token has expired
            await refreshToken(); 
        }
        else {
            setIsAuthorized(true); // If the token is still valid, the user is authorized
        }
    };

    if(isAuthorized === null) {
        return <div>Loading...</div>
    };

    return isAuthorized ? children : <Navigate to="/login"/>
}

export default ProtectedRoute;
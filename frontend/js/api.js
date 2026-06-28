// api.js
const BASE_URL = "http://127.0.0.1:8000";

async function secureFetch(endpoint, method = 'GET', body = null) {
    const token = localStorage.getItem('token');
    if (!token) window.location.href = 'login.html';

    const options = {
        method,
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    };
    if (body) options.body = JSON.stringify(body);

    const response = await fetch(`${BASE_URL}${endpoint}`, options);
    return await response.json();
}
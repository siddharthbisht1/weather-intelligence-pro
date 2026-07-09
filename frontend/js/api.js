// BASE_URL se aakhri slash (/) hata do
const BASE_URL = "https://weather-intelligence-pro.onrender.com"; 

async function secureFetch(endpoint, method = 'GET', body = null) {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'login.html';
        return;
    }

    // Endpoint ke aage slash zaroor lagao
    const url = `${BASE_URL}/${endpoint.startsWith('/') ? endpoint.slice(1) : endpoint}`;

    const options = {
        method,
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    };
    if (body) options.body = JSON.stringify(body);

    try {
        const response = await fetch(url, options);
        
        // Agar token expire ho gaya ho (401 Unauthorized)
        if (response.status === 401) {
            localStorage.removeItem('token');
            window.location.href = 'login.html';
            return;
        }
        
        return await response.json();
    } catch (error) {
        console.error("API Fetch Error:", error);
        throw error;
    }
}
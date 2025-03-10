// API ilə əlaqə qurmaq üçün funksiyalar
async function apiRequest(url, method, headers, body) {
    const response = await fetch(url, {
        method: method,
        headers: headers,
        body: body
    });
    return response.json();
}
let socket;

export const connectWebSocket = (onMessage) => {
    socket = new WebSocket("ws://127.0.0.1:8000/ws");

    socket.onopen = () => {
        console.log("Connected to WebSocket");
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        onMessage(data);
    };

    socket.onclose = () => {
        console.log("WebSocket disconnected");
    };

    socket.onerror = (error) => {
        console.error("WebSocket error:", error);
    };
};
document.getElementById("login-form").addEventListener("submit", get_user_credencials);

async function get_user_credencials(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;

    const response = await fetch("http://127.0.0.1:8000/auth/get_credencials", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name
        })
    });

    const data = await response.json();
    console.log(data);
}
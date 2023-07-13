document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    let inputemail = document.getElementById("email").value;
    let inputPassword = document.getElementById("password").value;
    let inputUsername = document.getElementById("username").value;

    if (inputUsername !== "") {
        inscription(inputemail, inputPassword, inputUsername);
    } else {
        connexion(inputemail, inputPassword);
    }
});


async function connexion(email, password) {
    const requestData = {
        email: email,
        password: password
    };

    const requestConfig = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    };

    const loginUrl = "http://localhost:8000/user/login";

    fetch(loginUrl, requestConfig)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Erreur lors de la requête de connexion');
            }
        })
        .then(data => {
            alert('Utilisateur connecté avec succès');
        })
        .catch(error => {
            alert('Erreur lors de la connexion');
        });
}


async function inscription(email, password, username) {
    const requestData = {
        email: email,
        username: username,
        password: password
    };

    const requestConfig = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    };

    const registerUrl = "http://localhost:8000/user/register";

    fetch(registerUrl, requestConfig)
        .then(response => {
            if (response.ok) {
                alert("Inscription réussi");
            } else {
                alert("Inscription échouée");
            }
        })
}
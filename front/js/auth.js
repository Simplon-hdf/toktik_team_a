document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (username && password ) {
        alert(`name = ${username} \n password = ${password}` );
    } else {
        alert("Le Login et le mot de passe sont obligatoires !");
    }
});
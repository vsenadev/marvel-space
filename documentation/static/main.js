const data = {
    login: {
        createUser: {
            description: "Create a user.",
            params: [
                { name: "string" },
                { login: "string" },
                { email: "string" },
                { password: "string" },
            ],
            url: "http://192.168.100.71:3050/api/v1/login",
            method: "POST",
            response: [
                { code: 409, message: "Login already exists in the database" },
                { code: 409, message: "Mail already exists in the database" },
                { code: 500, message: "An error has occurred" },
                { code: 201, message: "User inserted successfully" },
            ],
        },
    },
};

const route = document.getElementById("url");
if (route) {
    route.addEventListener("click", (event) => {
        if(event.target.textContent === "Create User"){
            console.log(data.login.createUser)
        }
    });
} else {
    console.error("Elemento com ID 'url' não encontrado no HTML.");
}
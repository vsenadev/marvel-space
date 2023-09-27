const data = {
    login: {
        createUser: {
            description: "This API route allows the creation of a new user in the system. By sending an HTTP POST request to this endpoint, the data of the new user is processed and stored in the system's database. The newly created user will receive a unique identifier, typically a unique numerical ID, and will be added to the list of registered users in the system.",
            params: [
                { name: "name", type: "string" },
                { name: "login", type: "string" },
                { name: "email", type: "string" },
                { name: "password", type: "string" },
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
const title = document.querySelector(".container__content_main_title");
const description = document.querySelector(".container__content_main_section_description")
const container = document.querySelector(".container__content_main_section_div")

if (route) {
    route.addEventListener("click", (event) => {
        if(event.target.textContent === "Create User"){
            title.textContent = "Create User"
            description.textContent = data.login.createUser.description
            container.innerHTML = ''
            let routeParamsString = ''

            data.login.createUser.params.map((param) => {
                routeParamsString += `<span>${param.name} <span>${param.type}</span></span>`
            })

            const routeData = `
                <section>
                    <div>
                        ${routeParamsString}
                    </div>
                </section>
            `

            container.innerHTML = routeData
        }
    });
} else {
    console.error("Elemento com ID 'url' não encontrado no HTML.");
}
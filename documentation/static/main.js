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
        authenticateUser: {
            description: "This route aims to verify the authenticity of the user based on the login (or username) and password provided by the client. It is an essential part of a secure authentication system, ensuring that only registered and authorized users have access to the application.",
            params: [
                { name: "login", type: "string" },
                { name: "password", type: "string" }
            ],
            url: "http://192.168.100.71:3050/api/v1/login",
            method: "PUT",
            response: [
                { code: 200, message: "Authenticated user" },
                { code: 400, message: "Wrong username or password" },
                { code: 404, message: "User not found." },
                { code: 500, message: "An error has occurred" },
            ],
        },
        requestCode: {
            description: "This route provides users with the ability to request a verification code by email. Upon receiving a POST request containing an email address, the server performs a check. If the email is associated with an existing user, a new verification code is generated and sent to the user. Otherwise, a new user is created with the provided email, and then the verification code is generated and sent via email. This functionality is essential to ensure secure access to the application, ensuring that only authenticated or new users are allowed to receive verification codes.",
            params: [
                { name: "mail", type: "string" },
            ],
            url: "http://192.168.100.71:3050/api/v1/login/request/string:mail",
            method: "GET",
            response: [
                { code: 200, message: "Step by step to reset password sent to your email." },
                { code: 404, message: "Error sending email." },
                { code: 404, message: "User not found." },
                { code: 500, message: "An error has occurred" },
            ],
        },
        userInformations: {
            description: "This route is designed to retrieve user information from the server. It accepts a GET request and returns the requested user data, typically identified by a user ID or username. This endpoint provides a read-only access to user details and is commonly used for profile retrieval and data lookup purposes.",
            params: [
                { name: "mail", type: "string" },
            ],
            url: "http://192.168.100.71:3050/api/v1/login/informations/string:mail",
            method: "GET",
            response: [
                { code: 200, message: "User object" },
                { code: 500, message: "An error has occurred" },
            ],
        },
        validateCode: {
            description: "This route validates a code against the code associated with a given email in the database. It accepts a POST request with email and code parameters, returning a response indicating whether the code is valid or not.",
            params: [
                { name: "mail", type: "string" },
                { name: "code", type: "string" },
            ],
            url: "http://192.168.100.71:3050/api/v1/login/decode/string:mail",
            method: "PUT",
            response: [
                { code: 400, message: "Time limit exceeded, please request a new code." },
                { code: 400, message: "Code entered is incorrect." },
                { code: 200, message: "Correct information, you will be redirected to change your password." },
                { code: 500, message: "An error has occurred" },

            ],
        }
    },
};

const routeElements = document.querySelectorAll(".url");
const title = document.querySelector(".container__content_main_title");
const description = document.querySelector(".container__content_main_section_description")
const container = document.querySelector(".container__content_main_section_div")

if (routeElements) {
    routeElements.forEach(route => {
      route.addEventListener("click", (event) => {

        const routeText = event.target.textContent;

        let routeData = null;
        let routeName = '';

        switch (routeText) {
          case "Create User":
            routeData = data.login.createUser;
            routeName = "Create User";
            break;
          case "Authenticate User":
            routeData = data.login.authenticateUser;
            routeName = "Authenticate User";
            break;
          case "Request Code":
            routeData = data.login.requestCode;
            routeName = "Request Code";
            break;
          case "User Informations":
            routeData = data.login.userInformations;
            routeName = "User Informations";
            break;
          case "Validate Code":
            routeData = data.login.validateCode;
            routeName = "Validate Code";
            break;
z        }

        if (routeData) {
          title.textContent = routeName;
          description.textContent = routeData.description;
          container.innerHTML = '';

          const routeParamsString = routeData.params.map((param) => {
            return `<span class="container__route_div-params-span">${param.name}: <span class="container__route_div-params-type">${param.type}</span></span>`;
          }).join('');

          const responseString = routeData.response.map((response) => {
            return `<span class="response-message"><strong class="response-code">${response.code}</strong> ${response.message}</span>`;
          }).join('');

          const routeHTML = `
            <section class="container__route">
              <div class="container__route_div">
                <div class="container__route_div-route">
                  <span class="container__route_div-route-method">${routeData.method}</span>
                  <span class="container__route_div-route-span">${routeData.url}</span>
                </div>
                <div class="container__route_div-params">
                  <h5>Params</h5>
                  <br/>
                  {
                    ${routeParamsString}
                  } 
                </div>
                <div class="container__route_div-params response">
                  ${responseString}
                </div>
              </div>
            </section>
          `;

          container.innerHTML = routeHTML;
        }
      });
    });


} else {
    console.error("Elemento com ID 'url' não encontrado no HTML.");
}
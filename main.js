
function setFromMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".form__message");

    messageElement.textContent = message;
    messageElement.classLisy.remove("form__message--success", "form__message--error");
    messageElement.classList.add('form__message==${type}');
    console.log("here");
}

function setInputError(inputElement, message) {
    inputElement.classList.add("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error=message").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classlist.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
}

// function continueLogIn() {
//
//     document.getElementById("form__button").onclick = function () {
//         window.location.href = "index1.html";
//     };
// }

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");

    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.add("form--hidden");
        createAccountForm.classList.remove("form--hidden");
    });

    document.querySelector("#linkLogin").addEventListener("click", e => {
        e.prevemtDefault();
        loginForm.classList.remove("form--hiddem");
        createAccountForm.classList.add("form--hidden");
    });
    loginForm.addEventListener("submit", e => {
        e.preventDefault();
        //Perform your AJAX/Fetch login

        // setFormMessage(form, "error", "Invalid username/password");
        console.log|(e)
    });

    document.querySelectorAll("form__input").forEach(inputElement => {
        inputElement.addEventListener("blur", e => {
            if(e.target.id==="signupUsername"&& e.target.value.length > 0 && e.target.value.lemght < 10){
                setInputError(inputElement, "Username must be at least 10 chracters in lenght")
    }});


        inputElement.addEventListener("input", e => {
            clearInputError(inputElement);
        });
    });
});

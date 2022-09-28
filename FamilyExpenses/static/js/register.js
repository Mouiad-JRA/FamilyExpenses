const usernameField = document.querySelector('#id_username');
const useremailField = document.querySelector('#id_email');
const usernamefeedbackField = document.querySelector('#username_invalid_feedback');
const userEmailfeedbackField = document.querySelector('#email_invalid_feedback');
const usernameSuccess = document.querySelector('.usernameSuccess');
const userEmailSuccess = document.querySelector('.userEmailSuccess');
usernameField.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value;
    usernameSuccess.style.display = "block";
    usernameSuccess.textContent = `Checking ${usernameVal}`
    usernameField.classList.remove('is-invalid');
    usernamefeedbackField.style.display = 'none';

    if (usernameVal.length > 0) {
        fetch("/account/validate-username/", {
              body:JSON.stringify( {username: usernameVal}),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
            usernameSuccess.style.display = 'none';
            if (data.username_error) {
                usernameField.classList.add('is-invalid');
                usernamefeedbackField.style.display = 'block';
                usernamefeedbackField.innerHTML = `<p>${data.username_error}</p>`
            }
        });
    }
});



useremailField.addEventListener('keyup', (e) => {
    const useremailVal = e.target.value;
    userEmailSuccess.style.display = "block";
       userEmailSuccess.textContent = `Checking ${useremailVal}`
    useremailField.classList.remove('is-invalid');
    userEmailfeedbackField.style.display = 'none';

    if (useremailVal.length > 0) {
        fetch("/account/validate-email/", {
              body:JSON.stringify( {email: useremailVal}),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
             userEmailSuccess.style.display = "none";
            if (data.email_error) {
                useremailField.classList.add('is-invalid');
                userEmailfeedbackField.style.display = 'block';
                userEmailfeedbackField.innerHTML = `<p>${data.email_error}</p>`
            }
        });
    }
});
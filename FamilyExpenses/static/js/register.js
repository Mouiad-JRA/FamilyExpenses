const usernameField = document.querySelector('#id_username');
const useremailField = document.querySelector('#id_email');
const usernamefeedbackField = document.querySelector('#username_invalid_feedback');
const userEmailfeedbackField = document.querySelector('#email_invalid_feedback');

usernameField.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value;

    usernameField.classList.remove('is-invalid');
    usernamefeedbackField.style.display = 'none';

    if (usernameVal.length > 0) {
        fetch("/account/validate-username/", {
              body:JSON.stringify( {username: usernameVal}),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
            console.log(data)
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

    useremailField.classList.remove('is-invalid');
    userEmailfeedbackField.style.display = 'none';

    if (useremailVal.length > 0) {
        fetch("/account/validate-email/", {
              body:JSON.stringify( {email: useremailVal}),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
            console.log(data)
            if (data.email_error) {
                useremailField.classList.add('is-invalid');
                userEmailfeedbackField.style.display = 'block';
                userEmailfeedbackField.innerHTML = `<p>${data.email_error}</p>`
            }
        });
    }
});
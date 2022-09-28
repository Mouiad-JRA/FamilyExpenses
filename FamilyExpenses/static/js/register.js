const usernameField = document.querySelector('#id_username');
const useremailField = document.querySelector('#id_email');
const usernamefeedbackField = document.querySelector('#username_invalid_feedback');
const userEmailfeedbackField = document.querySelector('#email_invalid_feedback');
const usernameSuccess = document.querySelector('.usernameSuccess');
const userEmailSuccess = document.querySelector('.userEmailSuccess');
const family_name = document.querySelector("#id_family")
const family_namefeedbackField = document.querySelector("#family_name_invalid_feedback")


family_name.addEventListener('keyup', (e) => {
    const familyNameVal = e.target.value;
    family_name.classList.remove('is-invalid');
    family_namefeedbackField.style.display = 'none';

    if (familyNameVal.length > 0) {
        fetch("/account/validate-family-name/", {
              body:JSON.stringify( {family_name: familyNameVal}),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
            usernameSuccess.style.display = 'none';
            if (data.family_name_error) {
                family_name.classList.add('is-invalid');
                family_namefeedbackField.style.display = 'block';
                family_namefeedbackField.innerHTML = `<p>${data.family_name_error}</p>`
            }
        });
    }
});






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
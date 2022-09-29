const usernameField = document.querySelector('#id_username');
const useremailField = document.querySelector('#id_email');
const usernamefeedbackField = document.querySelector('#username_invalid_feedback');
const userEmailfeedbackField = document.querySelector('#email_invalid_feedback');
const usernameSuccess = document.querySelector('.usernameSuccess');
const userEmailSuccess = document.querySelector('.userEmailSuccess');
const family_user_name = document.querySelector("#id_family")
const family_namefeedbackField = document.querySelector("#family_name_invalid_feedback")
const is_head = document.querySelector("#id_head")
const headfeedbackField = document.querySelector("#is_head_invalid_feedback")

const password1 = document.querySelector("#id_password1")
const password2 = document.querySelector("#id_password2")
const headfeedbackField = document.querySelector("#password_invalid_feedback")



password2.addEventListener('keyup',(e)=>{
     const password2Val = e.target.value;
       password2.classList.remove('is-invalid');
       headfeedbackField.style.display = 'none';
       if (password2Val.length>0){
            fetch("/account/validate-family-head/", {
              body:JSON.stringify( {password2: password2Val,  passwordone:password1.textContent }),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
            if (data.password_error) {
                password2.classList.add('is-invalid');
                headfeedbackField.style.display = 'block';
                headfeedbackField.innerHTML = `<p>${data.password_error}</p>`
            }
        });
       }
});

is_head.addEventListener('keyup', (e) => {
    const headVal = e.target.value;
    is_head.classList.remove('is-invalid');
    headfeedbackField.style.display = 'none';

    if (headVal !== null) {
        fetch("/account/validate-family-head/", {
              body:JSON.stringify( {is_head: headVal,  family_name:family_user_name.textContent }),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
            usernameSuccess.style.display = 'none';
            if (data.family_name_error) {
                family_user_name.classList.add('is-invalid');
                family_namefeedbackField.style.display = 'block';
                family_namefeedbackField.innerHTML = `<p>${data.family_name_error}</p>`
            }
        });
    }
});




















family_user_name.addEventListener('keyup', (e) => {
    const familyNameVal = e.target.value;
    family_user_name.classList.remove('is-invalid');
    family_namefeedbackField.style.display = 'none';

    if (familyNameVal.length > 0) {
        fetch("/account/validate-family-name/", {
              body:JSON.stringify( {family_name: familyNameVal}),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {

            if (data.family_name_error) {
                family_user_name.classList.add('is-invalid');
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
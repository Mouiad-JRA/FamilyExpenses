const usernameField = document.querySelector('#id_username');
const feedbackField = document.querySelector('#user_invalid_feedback');

usernameField.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value;

    usernameField.classList.remove('is-invalid');
    feedbackField.style.display = 'none';

    if (usernameVal.length > 0) {
        fetch("/account/validate/", {
              body:JSON.stringify( {username: usernameVal}),
            method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
            console.log(data)
            if (data.username_error) {
                usernameField.classList.add('is-invalid');
                feedbackField.style.display = 'block';
                feedbackField.innerHTML = `<p>${data.username_error}</p>`
            }
        });
    }
});
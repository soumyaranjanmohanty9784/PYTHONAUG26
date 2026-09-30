
        const form = document.getElementById("registrationForm");
        const message = document.getElementById("message");

        form.addEventListener("submit", function(event) {

            event.preventDefault();

            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const phone = document.getElementById("phone").value;
            const password = document.getElementById("password").value;
            const confirmPassword =
                document.getElementById("confirmPassword").value;


            if (
                name === "" ||
                email === "" ||
                phone === "" ||
                password === "" ||
                confirmPassword === ""
            ) {

                message.textContent = "Please fill all fields.";
                message.className =
                    "text-center mt-5 font-semibold text-red-500";

                return;
            }


            if (password !== confirmPassword) {

                message.textContent = "Passwords do not match.";
                message.className =
                    "text-center mt-5 font-semibold text-red-500";

                return;
            }


            const user = {
                name: name,
                email: email,
                phone: phone,
                password: password
            };


            localStorage.setItem("user", JSON.stringify(user));


            message.textContent =
                "Registration Successful! 🎉";

            message.className =
                "text-center mt-5 font-semibold text-green-500";


            form.reset();

        });
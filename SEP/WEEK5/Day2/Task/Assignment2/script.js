
        const loginForm =
            document.getElementById("loginForm");

        const message =
            document.getElementById("message");


        loginForm.addEventListener("submit", function(event) {

            event.preventDefault();


            const email =
                document.getElementById("email").value;

            const password =
                document.getElementById("password").value;


            const storedUser =
                localStorage.getItem("user");


            if (storedUser === null) {

                message.textContent =
                    "No registered user found.";

                message.className =
                    "text-center mt-6 font-semibold text-red-500";

                return;
            }


            const user =
                JSON.parse(storedUser);


            if (
                email === user.email &&
                password === user.password
            ) {

                message.textContent =
                    "Login Successful! 🎉";

                message.className =
                    "text-center mt-6 font-semibold text-green-500";

            } else {

                message.textContent =
                    "Invalid Email or Password.";

                message.className =
                    "text-center mt-6 font-semibold text-red-500";

            }

        });

 // Register Student
        document.getElementById("studentForm").addEventListener("submit", function(event) {

            event.preventDefault();

            let name = document.getElementById("name").value;
            let email = document.getElementById("email").value;
            let phone = document.getElementById("phone").value;
            let dob = document.getElementById("dob").value;
            let gender = document.getElementById("gender").value;
            let address = document.getElementById("address").value;


            localStorage.setItem("name", name);
            localStorage.setItem("email", email);
            localStorage.setItem("phone", phone);
            localStorage.setItem("dob", dob);
            localStorage.setItem("gender", gender);
            localStorage.setItem("address", address);


            alert("Student Registered Successfully!");


            // Clear Form
            document.getElementById("studentForm").reset();

        });


        function viewDetails() {

            let name = localStorage.getItem("name");
            let email = localStorage.getItem("email");
            let phone = localStorage.getItem("phone");
            let dob = localStorage.getItem("dob");
            let gender = localStorage.getItem("gender");
            let address = localStorage.getItem("address");


            if (name === null) {
                alert("No student details found!");
                return;
            }


            document.getElementById("displayName").textContent = name;
            document.getElementById("displayEmail").textContent = email;
            document.getElementById("displayPhone").textContent = phone;
            document.getElementById("displayDob").textContent = dob;
            document.getElementById("displayGender").textContent = gender;
            document.getElementById("displayAddress").textContent = address;

            document.getElementById("details").classList.remove("hidden");
        }
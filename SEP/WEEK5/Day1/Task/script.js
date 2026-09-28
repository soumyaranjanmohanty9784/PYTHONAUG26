        const form = document.getElementById("studentForm");

        form.addEventListener("submit", function(event) {

            event.preventDefault();

            const gender = document.querySelector(
                'input[name="gender"]:checked'
            );

            const student = {
                name: document.getElementById("name").value,
                email: document.getElementById("email").value,
                phone: document.getElementById("phone").value,
                dob: document.getElementById("dob").value,
                gender: gender.value,
                address: document.getElementById("address").value
            };

            localStorage.setItem(
                "studentDetails",
                JSON.stringify(student)
            );

            alert("Student Registered Successfully! 🎉");

        
            form.reset();
        });


        function viewDetails() {

            const data = localStorage.getItem("studentDetails");

            const details = document.getElementById("studentDetails");

            if (!data) {

                details.classList.remove("hidden");

                details.innerHTML = `
                    <h2 class="text-xl font-bold text-gray-800 mb-2">
                        No Student Found
                    </h2>

                    <p class="text-gray-600">
                        Please register a student first.
                    </p>
                `;

                return;
            }


            const student = JSON.parse(data);

            details.classList.remove("hidden");

            details.innerHTML = `

                <h2 class="text-xl font-bold text-indigo-700 mb-4">
                    🎓 Student Details
                </h2>

                <div class="space-y-2 text-gray-700">

                    <p>
                        <strong>Name:</strong>
                        ${student.name}
                    </p>

                    <p>
                        <strong>Email:</strong>
                        ${student.email}
                    </p>

                    <p>
                        <strong>Phone:</strong>
                        ${student.phone}
                    </p>

                    <p>
                        <strong>Date of Birth:</strong>
                        ${student.dob}
                    </p>

                    <p>
                        <strong>Gender:</strong>
                        ${student.gender}
                    </p>

                    <p>
                        <strong>Address:</strong>
                        ${student.address}
                    </p>

                </div>
            `;
        }
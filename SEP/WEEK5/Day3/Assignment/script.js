
    let users = JSON.parse(localStorage.getItem("users")) || [];

    let editIndex = null;


    function displayUsers() {

      const table = document.getElementById("userTable");

      table.innerHTML = "";

      users.forEach((user, index) => {

        table.innerHTML += `
          <tr class="border-b text-center">

            <td class="p-3">${index + 1}</td>

            <td class="p-3">${user.name}</td>

            <td class="p-3">${user.email}</td>

            <td class="p-3">${user.phone}</td>

            <td class="p-3">

              <button
                onclick="editUser(${index})"
                class="bg-yellow-500 text-white px-3 py-1 rounded mr-2">
                Edit
              </button>

              <button
                onclick="deleteUser(${index})"
                class="bg-red-600 text-white px-3 py-1 rounded">
                Delete
              </button>

            </td>

          </tr>
        `;
      });
    }


    function saveData() {

      const name = document.getElementById("name").value;
      const email = document.getElementById("email").value;
      const phone = document.getElementById("phone").value;

      if (name === "" || email === "" || phone === "") {
        alert("Please fill all fields");
        return;
      }


      const user = {
        name: name,
        email: email,
        phone: phone
      };


      if (editIndex !== null) {

        users[editIndex] = user;

        editIndex = null;

        document.getElementById("saveBtn").innerText = "Add User";

      }


      else {

        users.push(user);

      }


      localStorage.setItem("users", JSON.stringify(users));

      clearForm();

      displayUsers();

    }



    function editUser(index) {

      document.getElementById("name").value = users[index].name;

      document.getElementById("email").value = users[index].email;

      document.getElementById("phone").value = users[index].phone;

      editIndex = index;

      document.getElementById("saveBtn").innerText = "Update User";

    }



    function deleteUser(index) {

      if (confirm("Are you sure you want to delete this user?")) {

        users.splice(index, 1);

        localStorage.setItem("users", JSON.stringify(users));

        displayUsers();

      }

    }


    function clearForm() {

      document.getElementById("name").value = "";

      document.getElementById("email").value = "";

      document.getElementById("phone").value = "";

    }

    displayUsers();
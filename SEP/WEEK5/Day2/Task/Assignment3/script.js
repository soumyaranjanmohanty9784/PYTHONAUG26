
        const postsContainer =
            document.getElementById("postsContainer");

        const loading =
            document.getElementById("loading");


        fetch("https://jsonplaceholder.typicode.com/posts")


            .then(function(response) {

                return response.json();

            })


            .then(function(data) {

                loading.style.display = "none";


                data.forEach(function(post) {

                    const postCard =
                        document.createElement("div");


                    postCard.className =
                        "bg-white p-6 rounded-xl shadow-md hover:shadow-xl transition";


                    postCard.innerHTML = `

                        <div class="flex justify-between items-center mb-4">

                            <span class="bg-blue-100 text-blue-600
                                px-3 py-1 rounded-full text-sm font-semibold">

                                User ${post.userId}

                            </span>

                            <span class="text-gray-400 text-sm">

                                #${post.id}

                            </span>

                        </div>


                        <h2 class="text-xl font-bold text-gray-800 mb-3 capitalize">

                            ${post.title}

                        </h2>


                        <p class="text-gray-600 leading-relaxed">

                            ${post.body}

                        </p>

                    `;


                    postsContainer.appendChild(postCard);

                });

            })


            .catch(function(error) {

                loading.textContent =
                    "Failed to fetch data ❌";

                loading.className =
                    "text-center text-lg font-semibold text-red-500";

                console.log(error);

            });
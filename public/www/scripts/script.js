let utilizadores = [];
let admin = new Object;
admin.nome = "admin";
admin.senha = "admin";
utilizadores.push(admin);
userAtual = null;
var userAutenticado = null;

async function makeRequest(url, options) {
    try {
        const response = await fetch(url, options);
        return response;
    } catch (err) {
        console.log(err);
    }
}

async function login() {
    const nome = document.getElementById("username").value;
    const senha = document.getElementById("password").value;
    const user = {
        username: nome,
        password: senha,
    };
    const resposta = await makeRequest("https://localhost:3002/login", {
        method: "POST",
        body: JSON.stringify(user),
        headers: { "Content-type": "application/json; charset=UTF-8" },
    });
    json = await resposta.json();
    console.log(json);
    switch (resposta.status) {
        case 201:
            {
                if (nome === "admin" && senha === "admin") {
                    document.getElementById("main").style.display = "block";
                    document.getElementById("create").style.display = "inline";
                    document.getElementById("delete").style.display = "inline";
                    document.getElementById("search").style.display = "inline";
                    document.getElementById("login_button").style.display = "none";
                    document.getElementById("logout").style.display = "inline";
                    document.getElementById("products").style.display = "inline";
                    document.getElementById("offer").style.display = "flex";
                    document.getElementById("popup").style.display = "none";
                    document.getElementById("mystery").style.display = "flex";
                    localStorage.setItem("token", json.token);
                    userAutenticado = "admin";
                    showProd(user);
                    //await listar();
                    break;
                } else {
                    document.getElementById("login_button").style.display = "none";
                    document.getElementById("popup").style.display = "none";
                    document.getElementById("logout").style.display = "inline";
                    document.getElementById("main").style.display = "block";
                    document.getElementById("delete").style.display = "none";
                    document.getElementById("search").style.display = "none";
                    document.getElementById("create").style.display = "none";
                    document.getElementById("products").style.display = "inline";
                    document.getElementById("offer").style.display = "flex";
                    document.getElementById("mystery").style.display = "flex";
                    userAutenticado = us.nome;
                    showProd(user);
                    return;
                }
            }

        case 401:
            {
                // Password errada
                document.getElementById("pMsg1").innerHTML = json.msg;
                break;
            }
        case 404:
            {
                // Utilizador não encontrado
                console.log(json.msg);
                document.getElementById("pMsg1").innerHTML = json.msg;
                break;
            }
    }
}



function logout() {
    document.getElementById("logout").style.display = "none";
    document.getElementById("login_button").style.display = "inline";
    document.getElementById("delete").style.display = "none";
    document.getElementById("search").style.display = "none";
    document.getElementById("create").style.display = "none";
    document.getElementById("products").style.display = "none";
    document.getElementById("offer").style.display = "none";
    document.getElementById("mystery").style.display = "none";
    localStorage.removeItem("token");

}

async function registarEnviar() {
    const nome = document.getElementById("username_registar").value;
    const senha = document.getElementById("password_registar").value;
    const user = {
        username: nome,
        password: senha,
    };
    const resposta = await makeRequest("https://localhost:3002/registar", {
        method: "POST",
        body: JSON.stringify(user),
        headers: { "Content-type": "application/json; charset=UTF-8" },
    });
    json = await resposta.json();
    switch (resposta.status) {
        case 409:
            {
                // Utilizador já existe
                document.getElementById("pMsg2").innerHTML = json.msg;
                break;
            }
        case 400:
            {
                // Password inaceitável
                document.getElementById("pMsg2").innerHTML = json.msg;
                break;
            }
        case 201:
            {
                // Utilizador registado
                document.getElementById("pMsg2").innerHTML = json.msg;
                break;
            }
    }
}


async function makeRequest(url, options) {
    try {
        const response = await fetch(url, options);
        return response;
    } catch (err) {
        console.log(err);
    }
}

async function del() {
    const nome = document.getElementById("prod").value;
    await fetch('https://localhost:3002/delete/' + nome, {
        method: "DELETE",
        headers: { "Content-type": "application/json;charset=UTF-8" },
        body: JSON.stringify({ nome: nome })
    })
        .then(response => response.json())
        .then(json => console.log(json));
}


async function addProduct() {
    const nome = document.getElementById("nome").value;
    const imagem = document.getElementById("prod_img").value;
    const preco = document.getElementById("prod_preco").value;

    await fetch('https://localhost:3002/create', {
        method: "POST",
        headers: { "Content-type": "application/json;charset=UTF-8" },
        body: JSON.stringify({ nome: nome, preco: preco, imagem: imagem })
    })
        .then(response => response.json())
        .then(json => console.log(json));
    showProd(userAutenticado)
}

async function search_prod() {
    const nome = document.getElementById("nome_prod").value;
    await fetch('https://localhost:3002/getProds/' + nome, {
        method: "GET",
        headers: { "Content-type": "application/json;charset=UTF-8" }
    })
        .then(response => response.json())
        .then(json => {
            let lista = "";
            lista += '<img src="' + json.imagem + '" width="500px">';
            lista += '<br>';
            lista += json.nome;
            lista += '<br>';
            lista += json.preco;
            document.getElementById("listaProds").innerHTML = lista;
        });
}


async function showProd(user) {
    if (user === "admin") {
        let produtos = document.getElementById("listaProds");
        await fetch('https://localhost:3002/getProds', {
            method: "GET",
            headers: { "Content-type": "application/json;charset=UTF-8" }
        })
            .then(response => response.json())
            .then(json => {
                let lista = "";
                for (prod of json) {
                    lista += '<img src="' + prod.imagem + '" width="500px" + prod.nome>';
                    lista += prod.nome;
                    lista += '<br>';
                    lista += prod.preco + '€';
                    lista += '<br>';
                    lista += '<br>'
                    lista += '<br>'
                    //lista += '<input type="checkbox" id="chk" class="prods" value="' + prod.id + '"="del()">';
                    //  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
                }
                produtos.innerHTML = lista;
            });
    } else if (user === null) {
        let produtos = document.getElementById("listaProds");
        await fetch('https://localhost:3002/getProds', {
            method: "GET",
            headers: { "Content-type": "application/json;charset=UTF-8" }
        })
            .then(response => response.json())
            .then(json => {
                let lista = "";
                for (prod of json) {
                    lista += " "
                    lista += " ";
                    lista += '<br>';
                    lista += " ";
                    lista += '<br>';
                    lista += '<br>'
                    lista += '<br>'
                }
                produtos.innerHTML = lista;
            });
    } else {
        let produtos = document.getElementById("listaProds");
        await fetch('https://localhost:3002/getProds', {
            method: "GET",
            headers: { "Content-type": "application/json;charset=UTF-8" }
        })
            .then(response => response.json())
            .then(json => {
                let lista = "";
                for (prod of json) {
                    lista += '<br>'
                    lista += '<br>'
                    lista += '<img src="' + prod.imagem + '" width="500px">';
                    lista += prod.nome;
                    lista += '<br>';
                    lista += prod.preco + '€';
                    lista += '<br>';
                }
                produtos.innerHTML = lista;
            });
    }
}


// Initialize and add the map
function initMap() {
    var options = {
        zoom: 15,
        center: { lat: 38.725090, lng: -9.146890 }
    }
    var map = new google.maps.Map(document.getElementById('map'), options);

    var marker = new google.maps.Marker({
        position: { lat: 38.725090, lng: -9.146890 },
        map: map,
        icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
    });
}
window.initMap = initMap;


function registarform() {
    document.getElementById("popup").style.display = "none";
    document.getElementById("popup_registar").style.display = "flex";
}

function loginform() {
    document.getElementById("popup").style.display = "flex";
    document.getElementById("popup_registar").style.display = "none";
}


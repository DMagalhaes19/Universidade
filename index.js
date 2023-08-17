require('dotenv').config();

const express = require("express");
const cors = require("cors");
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const https = require('https');
const fs = require('fs');


const app = express();
app.use(express.static('public/www'));             //PARA CORRER O COD: https:://localhost:3002 



const sslServer = https.createServer({
    key: fs.readFileSync('cert/key.pem'),
    cert:fs.readFileSync('cert/certificate.pem')
}, app);

const PORT = 3002;

app.use(cors());
app.options('*', cors()) // include before other routes

app.use(express());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

let users = require('./config/users.json');
let dados = require('./config/db.json');
//let db = require("./config/db.json");


function escreve(fich, db) {
    fs.writeFile(fich, JSON.stringify(db, null, 4), 'utf8', err => {
        if (err) {
            console.log(`Error writing file: ${err}`)
        } else {
            console.log('Escreveu no ficheiro ' + fich); // Sucesso
        }
    })
}

function existeUser(nome) {
    for (utilizador of users)
        if (utilizador.username === nome) {
            return true;
        }
    return false;
}
//
// Registo de um novo utilizador
app.post("/registar", (req, res) => {
    const username = req.body.username;
    if (!existeUser(username)) {
        const newUser = {
            username: username,
            password: req.body.password,
            tipo: 0
        }
        if (newUser.password.length < 5) {
            return res.status(400).send({
                msg: 'Password deve ter 5 ou mais caracteres'
            });
        }
        users.push(newUser);
        escreve("./config/users.json", users);
        return res.status(201).send({
            msg: `Criado utilizador ${username}`
        });
    } else {
        return res.status(409).send({
            msg: 'Utilizador já existe'
        });
    }
});

// Login
app.post("/login", (req, res) => {
    const nome = req.body.username;
    const senha = req.body.password;
    for (utilizador of users) {
        if (utilizador.username === nome)
            if (utilizador.password === senha) {
                token = jwt.sign(utilizador, process.env.USER_PASSWORD);
                return res.status(201).json({ 
                    auth: true, 
                    token: token,
                    msg: "Login efetuado com sucesso!"})
            } else {
                return res.status(401).json({ msg: "Password inválida!" })
            }
    }
    return res.status(404).json({ msg: "Utilizador não encontrado!" })
});

function validarToken(token) {
    try {
        return jwt.verify(token, process.env.SECRET);
    } catch (err) {
        return false;
    }
}

// Acesso à informação somente se autorizado
app.get("/listarDados", (req, res) => {
    const decoded = validarToken(req.header('token'));
    if (!decoded) {
        return res.status(401).json({ msg: "Utilizador não autenticado ou não autorizado!" });
    }
    const nome = decoded.username;
    if (dados) {
        res.status(200).json(dados);
    } else {
        res.status(404).json({ msg: "Dados não encontrados!" });
    }
});

// Route to get one post

/*app.get("/:id", (req, res) => {
    const id = req.params.id;
    result = "";
    //search the db.json file for the id 
    for (post of dados) {
        if (post.id == id) {
            result = post;
            break;
        }
    }
    if (result) {
        res.status(200).json(result);
    }
    else {
        res.status(404).json({ msg: "Post not found" });
    }
});*/
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Route to get all posts
app.get("/getProds", cors(), (req, res) => {
    result = dados;
    res.send(result);
});

// Getprods: get a product by name.
app.get("/getProds/:nome", cors(), (req, res) => {
    const nome = req.params.nome;
    result = "";
    //search the db.json file for the id
    for (post of dados) {
        if (post.nome == nome) {
            result = post;
            break;
        }
    }
    if (result) {
        res.status(200).json(result);
    }
    else {
        res.status(404).json({ msg: "Post not found" });
    }
});




// Route for creating a new post
app.post("/create", (req, res) => {
    newID = dados.length + 1;
    const nome = req.body.nome;
    const imagem = req.body.imagem;
    const preco = req.body.preco;

    const newProduct = {
        "id": newID,
        "nome": nome,
        "imagem": imagem,
        "preco": preco
    }
    dados.push(newProduct);
    escreve("./config/db.json", dados);
    result = newProduct;
    res.send(result);
});


app.post('/submit-form', (req, res) => {
    newID = dados.length + 1;
    const nome = req.body.nome;
    const imagem = req.body.imagem;
    const preco = req.body.preco;
    const newProduct = {
        "id": newID,
        "nome": nome,
        "imagem": imagem,
        "preco": preco
    }
    dados.push(newProduct);
    escreve("./config/db.json", dados);
    result = newProduct;
    res.send(result);
});


// Route to delete a post given an name
app.delete("/delete/:nome", (req, res) => {
    const nome = req.params.nome;
    result = "";
    //search the db.json file for the id
    for (post of dados) {
        if (post.nome == nome) {
            result = post;
            break;
        }
    }
    if (result) {
        dados.splice(dados.indexOf(result), 1);
        escreve("./config/db.json", dados);
        res.status(200).json({ msg: "Post deleted" });
    }
    else {
        res.status(404).json({ msg: "Post not found" });
    }
});

sslServer.listen(PORT, () => {
    console.log(`Server is running on ${PORT}`);
});


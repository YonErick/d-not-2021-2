const express = require('express');
const server = express();

const Correios = require('node-cep-correios');
const correios = new Correios();

const porta = 3011

server.listen(porta, () => console.log(`Servidor Rodando na Porta: ${porta}`));

server.get('/', (requisicao, resposta) => {
    console.log('Rota de CEP encontrada!!!')
    const { cep } = requisicao.query;
    console.log('>> ' + cep);

    correios.consultaCEP({cep: cep})
    .then( resultado => {
        resposta.send ( resultado );
        console.log( resultado );
        console.log("Sucesso na Consulta!!!");
    })
    .catch(error => {
        console.log("Ocorreu um Erro: " + error)
    })
})

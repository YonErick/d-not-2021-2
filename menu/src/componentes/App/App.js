import React from 'react'
import './App.css';

import Header from '../Header/Header.jsx'
import Inicio from '../Inicio/Inicio.jsx'
import Cursos from '../Cursos/Cursos.jsx'
import Contatos from '../Contatos/Contatos.jsx'
import Parceiros from '../Parceiros/Parceiros.jsx'
import Missao from '../Missao/Missao.jsx'
import Sobre from '../Sobre/Sobre.jsx'

//import { Link } from 'react-router-dom'
import { Route, Switch} from 'react-router'

function App() {
  return (
    <div>
 
      <Header />
      
      <main>
        <Switch>
          <Route exact path = "/" render = {(props) => <Inicio/>}></Route>
          <Route exact path = "/cursos" render = {(props) => <Cursos/>}></Route>
          <Route exact path = "/contatos" render = {(props) => <Contatos/>}></Route>
          <Route exact path = "/parceiros" render = {(props) => <Parceiros/>}></Route>
          <Route exact path = "/missao" render = {(props) => <Missao/>}></Route>
          <Route exact path = "/sobre" render = {(props) => <Sobre/>}></Route>
        </Switch>

      </main>
      
    </div>
  );
}

export default App;


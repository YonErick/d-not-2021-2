import React from 'react'

import './Cursos.css'
import Inicio from '../Inicio/Inicio.jsx'
import Titulo from '../Titulo/Titulo.jsx'
import CursosHeader from './CursosHeader.jsx'
import { Route, Switch } from 'react-router'

export default function Cursos() {
    return (
        <div>
            <CursosHeader />

            <Titulo texto="Seção de Cursos do Site" />

            <div className="cursos">
                <Switch>
                    <Route exact path="/" render={(props) => <Inicio />}></Route>

                </Switch>
            </div>

        </div>

    )
}


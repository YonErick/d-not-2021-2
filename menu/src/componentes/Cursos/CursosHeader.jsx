import React from 'react'
import { Link } from 'react-router-dom'

import '../Header/Header.css'

export default function Header() {
    return (
        <div className="menu">
            <nav className="navMenu">
                <ul>
                    <li> <Link to="/"> Voltar </Link> </li>
                    <li> <Link to="/cursos"> Informática </Link></li>
                    <li> <Link to="/cursos"> Engenharia </Link></li>
                    <li> <Link to="/cursos"> Quimica </Link></li>
                    <li> <Link to="/cursos"> Administração </Link></li>
                    <li> <Link to="/cursos"> Direito </Link></li>
                </ul>
            </nav>
        </div>
    )
}


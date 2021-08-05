import React from "react" 
import "./menuhorizontal.css"

export default function Menu() {
    return (
        <div>
            <div className="Menu">
                <nav className="navMenu">
                    <ul>
                        <li> <a href="#inicio"> Nosso Canal </a> </li>
                        <li> <a href="#cursos"> Cursos </a> </li>
                        <li> <a href="#Contatos"> Contatos </a> </li>
                        <li> <a href="#parceiros"> Parceiros </a> </li>
                        <li> <a href="#missao"> Missão </a> </li>
                        <li> <a href="#sobre"> Sobre </a> </li>
                    </ul>
                </nav>

                <section id="inicio">
                    <h1> Nosso Canal </h1>
                </section>

                <section id="cursos">
                    <h1> Cursos </h1>
                </section>

                <section id="contatos">
                    <h1> Contatos </h1>
                </section>

                <section id="parceiros">
                    <h1> Parceiros </h1>
                </section>

                <section id="missao">
                    <h1> Missão </h1>
                </section>

                <section id="sobre">
                    <h1> Sobre </h1>
                </section>

            </div>
        </div>
    )
}
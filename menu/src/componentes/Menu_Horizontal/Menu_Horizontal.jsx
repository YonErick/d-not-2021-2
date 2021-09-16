import React from "react"
import "./Menu_Horizontal.css" 

export default function Menu() {
    return (
        <div>
            <div className="menu">
                <nav className="navMenu">
                    <ul>
                        <li> <a href="#inicio"> Nosso Canal </a></li>
                        <li> <a href="#cursos"> Cursos </a></li>
                        <li> <a href="#contatos"> Contatos </a></li>
                        <li> <a href="#parceiros"> Parceiros </a></li>
                        <li> <a href="#missao"> Missão </a></li>
                        <li> <a href="#sobre"> Sobre </a></li>
                    </ul>
                </nav>
            </div>
 
            <section id="inicio">
                <h2> Nosso Canal</h2>

                <aside className="aside">
                    <a href="#inicio" id="inicio2">Canal</a>
                    <a href="#cursos" id="cursos2">Cursos</a>
                    <a href="#contatos" id="contatos2">Contatos</a>
                    <a href="#parceiros" id="parceiros2">Parceiros</a>
                    <a href="#missao" id="missao2">Missao</a>
                    <a href="#sobre" id="sobre2">Sobre</a>
                </aside>
            </section>

            <section id="cursos">
                <h2> Cursos </h2>
            </section>

            <section id="contatos">
                <h2> Contatos</h2>
            </section>

            <section id="parceiros">
                <h2> Parceiros</h2>
            </section>

            <section id="missao">
                <h2> Missão</h2>
            </section>

            <section id="sobre">
                <h2> Sobre </h2>
            </section>

            <a class = "irTopo" href=".menu"> Topo </a>

            < a className = "irInicio" href="#inicio">Nosso Canal</a>
            < a className = "irCursos" href="#cursos">Cursos</a>
            < a className = "irContatos" href="#contatos">Contatos</a>
            < a className = "irParceiros" href="#parceiros">Parceiros</a>
            < a className = "irMissao" href="#missao">Missão</a>
            < a className = "irSobre" href="#sobre">Sobre</a>

            <footer>
                <h2>Rodapé </h2>
                
            </footer>

        </div>
    )
}
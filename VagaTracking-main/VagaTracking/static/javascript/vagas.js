const vagas = [
    {
        titulo: "Desenvolvedor Front-End",
        descricao: "Crie interfaces web com HTML, CSS e JS.",
        requisitos: ["HTML", "CSS", "JavaScript"],
        area: "Desenvolvimento",
        logo: "https://cdn-icons-png.flaticon.com/512/1055/1055687.png",
        
    },

    {
        titulo: "Desenvolvedor Back-End",
        descricao: "APIs com Node.js e banco de dados.",
        requisitos: ["Node.js", "SQL", "Express"],
        area: "Desenvolvimento",
        logo: "https://cdn-icons-png.flaticon.com/512/919/919825.png"
    },
    {
        titulo: "Desenvolvedor Full Stack",
        descricao: "Trabalhe em todas as camadas da aplicação.",
        requisitos: ["React", "Node", "MongoDB"],
        area: "Desenvolvimento",
        logo: "https://cdn-icons-png.flaticon.com/512/919/919851.png"
    },
    {
        titulo: "Desenvolvedor Front-End Júnior",
        descricao: "Apoie no desenvolvimento de interfaces responsivas.",
        requisitos: ["HTML", "CSS", "Bootstrap"],
        area: "Desenvolvimento",
        logo: "https://cdn-icons-png.flaticon.com/512/1055/1055687.png"
    },
    {
        titulo: "Desenvolvedor Back-End Pleno",
        descricao: "Implante e mantenha sistemas em produção.",
        requisitos: ["Java", "Spring Boot", "MySQL"],
        area: "Desenvolvimento",
        logo: "https://cdn-icons-png.flaticon.com/512/919/919825.png"
    },
    {
        titulo: "Desenvolvedor Full Stack Sênior",
        descricao: "Lidere projetos web full stack.",
        requisitos: ["Vue.js", "Node.js", "PostgreSQL"],
        area: "Desenvolvimento",
        logo: "https://cdn-icons-png.flaticon.com/512/919/919851.png"
    },
    {
        titulo: "Designer UI/UX Mobile",
        descricao: "Crie interfaces para apps mobile com foco em experiência.",
        requisitos: ["Figma", "Design Thinking", "Prototipagem"],
        area: "Design",
        logo: "https://cdn-icons-png.flaticon.com/512/281/281764.png"
    },
    {
        titulo: "Designer Gráfico Pleno",
        descricao: "Crie peças digitais e impressas para campanhas.",
        requisitos: ["CorelDraw", "Illustrator", "Criatividade"],
        area: "Design",
        logo: "https://cdn-icons-png.flaticon.com/512/1157/1157109.png"
    },
    {
        titulo: "Motion Designer 3D",
        descricao: "Crie animações 3D para vídeos institucionais.",
        requisitos: ["After Effects", "Cinema 4D", "Storyboard"],
        area: "Design",
        logo: "https://cdn-icons-png.flaticon.com/512/733/733547.png"
    },
    {
        titulo: "Analista de Dados Júnior",
        descricao: "Gere relatórios com base em dados operacionais.",
        requisitos: ["Excel", "SQL", "Dashboards"],
        area: "Dados",
        logo: "https://cdn-icons-png.flaticon.com/512/2721/2721618.png"
    },
    {
        titulo: "Engenheiro de Dados Sênior",
        descricao: "Arquitetura de dados e governança.",
        requisitos: ["BigQuery", "Python", "Airflow"],
        area: "Dados",
        logo: "https://cdn-icons-png.flaticon.com/512/4230/4230616.png"
    },
    {
        titulo: "Cientista de Dados Pleno",
        descricao: "Desenvolva modelos preditivos para negócios.",
        requisitos: ["Python", "Pandas", "Sklearn"],
        area: "Dados",
        logo: "https://cdn-icons-png.flaticon.com/512/1147/1147930.png"
    }
];




const lista = document.getElementById("vagas-lista");
const detalhes = document.getElementById("detalhes-vaga");
const titulo = document.getElementById("titulo-vaga");
const descricao = document.getElementById("descricao-vaga");
const requisitos = document.getElementById("requisitos-vaga");


let vagaSelecionada = null;


function renderizarVagas(filtradas = vagas) {
    lista.innerHTML = "";
    filtradas.forEach((vaga, index) => {
        const div = document.createElement("div");
        div.className = "vaga";


        const logo = document.createElement("img");
        logo.src = vaga.logo;
        logo.alt = "Logo da empresa";
        logo.className = "vaga-logo";


        const titulo = document.createElement("h3");
        titulo.textContent = vaga.titulo;
        titulo.className = "vaga-titulo";


        const descricao = document.createElement("p");
        descricao.textContent = vaga.descricao;
        descricao.className = "vaga-descricao";


        div.appendChild(logo);
        div.appendChild(titulo);
        div.appendChild(descricao);


        div.onclick = () => mostrarDetalhes(index, filtradas);
        lista.appendChild(div);
    });
}


function mostrarDetalhes(index, listaAtual = vagas) {
    const vaga = listaAtual[index];
    vagaSelecionada = vaga;
    titulo.textContent = vaga.titulo;
    descricao.textContent = vaga.descricao;
    requisitos.innerHTML = "";
    vaga.requisitos.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        requisitos.appendChild(li);
    });
    detalhes.classList.remove("oculto");
}


function filtrarVagas() {
    const termo = document.getElementById("busca").value.toLowerCase();
    const area = document.getElementById("filtroArea").value;


    const filtradas = vagas.filter(vaga => {
        const combinaTitulo = vaga.titulo.toLowerCase().includes(termo);
        const combinaArea = !area || vaga.area === area;
        return combinaTitulo && combinaArea;
    });


    renderizarVagas(filtradas);
    detalhes.classList.add("oculto");
}


function abrirModal() {
    document.getElementById("modal").classList.remove("oculto");
}


function fecharModal() {
    document.getElementById("modal").classList.add("oculto");
}


function enviarFormulario(event) {
    event.preventDefault();
    alert(`Candidatura enviada para: ${vagaSelecionada.titulo}`);
    fecharModal();
}


renderizarVagas();

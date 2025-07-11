const candidatos = [
  {
    nome: "João da Silva",
    vaga: "Desenvolvedor Front-End",
    email: "joao@gmail.com",
    status: "Em análise"
  },
  {
    nome: "Maria Oliveira",
    vaga: "UX Designer",
    email: "maria@gmail.com",
    status: "Entrevista marcada"
  },
  {
    nome: "Carlos Souza",
    vaga: "Analista de Dados",
    email: "carlos@gmail.com",
    status: "Aprovado"
  },
  {
    nome: "Ana Martins",
    vaga: "Desenvolvedor Front-End",
    email: "ana@gmail.com",
    status: "Entrevista marcada"
  },
  {
  nome: "Bruno Lima",
  vaga: "Desenvolvedor Back-End",
  email: "bruno.lima@gmail.com",
  status: "Em análise"
},
{
  nome: "Fernanda Rocha",
  vaga: "Product Owner",
  email: "fernanda.rocha@gmail.com",
  status: "Aprovado"
},
{
  nome: "Gabriel Nunes",
  vaga: "Analista de Dados",
  email: "gabriel.nunes@gmail.com",
  status: "Entrevista marcada"
},
{
  nome: "Larissa Costa",
  vaga: "UX Designer",
  email: "larissa.costa@gmail.com",
  status: "Em análise"
},
{
  nome: "Paulo Henrique",
  vaga: "Desenvolvedor Front-End",
  email: "paulo.henrique@gmail.com",
  status: "Aprovado"
},
{
  nome: "Isabela Martins",
  vaga: "Desenvolvedor Back-End",
  email: "isabela.martins@gmail.com",
  status: "Entrevista marcada"
},
{
  nome: "Thiago Alves",
  vaga: "Scrum Master",
  email: "thiago.alves@gmail.com",
  status: "Em análise"
},
{
  nome: "Juliana Ribeiro",
  vaga: "UX Designer",
  email: "juliana.ribeiro@gmail.com",
  status: "Aprovado"
},
{
  nome: "Eduardo Fernandes",
  vaga: "Product Owner",
  email: "eduardo.fernandes@gmail.com",
  status: "Entrevista marcada"
},
{
  nome: "Camila Souza",
  vaga: "Analista de Dados",
  email: "camila.souza@gmail.com",
  status: "Em análise"
}
  
];

const lista = document.getElementById('candidatos-lista');
const filtroVaga = document.getElementById('filtro-vaga');
const filtroStatus = document.getElementById('filtro-status');
const buscaNome = document.getElementById('busca-nome');


function preencherFiltroVagas() {
  const vagasUnicas = [...new Set(candidatos.map(c => c.vaga))];
  vagasUnicas.forEach(vaga => {
    const opt = document.createElement('option');
    opt.value = vaga;
    opt.textContent = vaga;
    filtroVaga.appendChild(opt);
  });
}


function renderizarLista() {
  lista.innerHTML = '';
  const busca = buscaNome.value.toLowerCase();
  const vagaSelecionada = filtroVaga.value;
  const statusSelecionado = filtroStatus.value;

  const filtrados = candidatos.filter(c => {
    const nomeMatch = c.nome.toLowerCase().includes(busca);
    const vagaMatch = vagaSelecionada === '' || c.vaga === vagaSelecionada;
    const statusMatch = statusSelecionado === '' || c.status === statusSelecionado;
    return nomeMatch && vagaMatch && statusMatch;
  });

  if (filtrados.length === 0) {
    lista.innerHTML = "<p>Nenhum candidato encontrado.</p>";
    return;
  }

  filtrados.forEach(candidato => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <h2>${candidato.nome}</h2>
      <div class="vaga">${candidato.vaga}</div>
      <div class="email"><strong>Email:</strong> ${candidato.email}</div>
      <div class="status"><strong>Status:</strong> ${candidato.status}</div>
    `;
    lista.appendChild(card);
  });
}


document.getElementById('limpar-filtros').addEventListener('click', () => {
  buscaNome.value = '';
  filtroVaga.value = '';
  filtroStatus.value = '';
  renderizarLista();
});


filtroVaga.addEventListener('change', renderizarLista);
filtroStatus.addEventListener('change', renderizarLista);
buscaNome.addEventListener('input', renderizarLista);


preencherFiltroVagas();
renderizarLista();

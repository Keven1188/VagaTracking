// Exemplo de dados simulados
let candidatos = [
    {
      nome: "Ana Pereira",
      email: "ana.pereira@exemplo.com",
      cargo: "Desenvolvedor Front-end",
      notaIA: 87,
      comentario: ""
    },
    {
      nome: "Carlos Souza",
      email: "carlos.souza@exemplo.com",
      cargo: "Designer UI/UX",
      notaIA: 92,
      comentario: "Perfil promissor. Verificar portfólio."
    },
    {
      nome: "Juliana Lima",
      email: "juliana.lima@exemplo.com",
      cargo: "Desenvolvedor Back-end",
      notaIA: 78,
      comentario: ""
    }
  ];
  
  // Salvar no localStorage (para simular persistência)
  localStorage.setItem("candidatos", JSON.stringify(candidatos));
  
  function gerarTabela(lista) {
    const tbody = document.querySelector("#tabelaCandidatos tbody");
    tbody.innerHTML = "";
  
    lista.forEach((candidato, index) => {
      const row = document.createElement("tr");
  
      row.innerHTML = `
        <td>${candidato.nome}</td>
        <td>${candidato.email}</td>
        <td>${candidato.cargo}</td>
        <td>${candidato.notaIA}</td>
        <td><button onclick="baixarCurriculo('${candidato.nome}')">Download</button></td>
        <td><textarea onchange="salvarComentario(${index}, this.value)">${candidato.comentario || ''}</textarea></td>
      `;
  
      tbody.appendChild(row);
    });
  }
  
  function filtrarCandidatos() {
    const termo = document.getElementById("filtroCargo").value.toLowerCase();
    const filtrados = candidatos.filter(c => c.cargo.toLowerCase().includes(termo));
    gerarTabela(filtrados);
  }
  
  function baixarCurriculo(nome) {
    alert(`Simulando download do currículo de ${nome}`);
  }
  
  function salvarComentario(index, texto) {
    candidatos[index].comentario = texto;
    localStorage.setItem("candidatos", JSON.stringify(candidatos));
  }
  
  function exportarCSV() {
    const headers = ["Nome", "Email", "Cargo", "Nota IA", "Comentário"];
    const linhas = candidatos.map(c =>
      [c.nome, c.email, c.cargo, c.notaIA, c.comentario || ""].join(",")
    );
    const conteudo = [headers.join(","), ...linhas].join("\n");
  
    const blob = new Blob([conteudo], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "candidatos.csv";
    a.click();
  }
  
  window.onload = () => gerarTabela(candidatos);
  
const input = document.getElementById("curriculo");
const fileNameDisplay = document.getElementById("file-name");
const resultado = document.getElementById("resultado");
const loader = document.getElementById("loader");

input.addEventListener("change", () => {
  if (input.files.length > 0) {
    fileNameDisplay.textContent = input.files[0].name;
  } else {
    fileNameDisplay.textContent = "Nenhum arquivo selecionado";
  }
});

document.getElementById("formulario").addEventListener("submit", async (e) => {
  e.preventDefault();
  resultado.textContent = "";
  loader.style.display = "block";

  const formData = new FormData();
  formData.append("curriculo", input.files[0]);

  try {
    const response = await fetch("/analisar", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    resultado.textContent = data.resultado || "Erro na análise.";
  } catch (err) {
    resultado.textContent = "Erro ao enviar o currículo.";
  } finally {
    loader.style.display = "none";
  }
});

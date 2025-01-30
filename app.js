let listaNomes = [];

function adicionarAmigo() {
  let nomeAmigo = document.querySelector("input").value;
  if (nomeAmigo == "") {
    alert("Por favor, insira um nome.");
  } else {
    listaNomes.push(nomeAmigo);
    console.log(listaNomes);
    listarNomes();
  }

  limparCampo();
}

function listarNomes() {
  let listaAmigo = document.getElementById("listaAmigos").innerHTML;
  listaAmigo += "<li>" + listaNomes[listaNomes.length - 1] + "</li>";
  document.getElementById("listaAmigos").innerHTML = listaAmigo;
}

function sortearAmigo() {
  let tamanhoLista = listaNomes.length;
  let sorteioNumero = Math.floor(Math.random() * tamanhoLista);
  let amigoSorteado = listaNomes[sorteioNumero];
  console.log(sorteioNumero);
  console.log(tamanhoLista);

  if (listaNomes == "") {
    alert("Nenhum nome adicionado");
  } else {
    let resultadoSorteio = document.getElementById("resultado").innerHTML;
    resultadoSorteio =
      "<li>" + "O amigo sorteado é: " + amigoSorteado + "</li>";
    document.getElementById("resultado").innerHTML = resultadoSorteio;
    document.getElementById("listaAmigos").innerHTML = "";
    listaNomes = [];
  }
}

function limparCampo() {
  nomeAmigo = document.querySelector("input");
  nomeAmigo.value = "";
}

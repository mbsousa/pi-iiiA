document.getElementById("produtoForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const nome = document.getElementById("nome").value;
    const descricao = document.getElementById("descricao").value;
    const quantidade = document.getElementById("quantidade").value;

    const response = await fetch("/produtos/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, descricao, quantidade: parseInt(quantidade) })
    });

    if (response.ok) {
        carregarProdutos();
    }
});

async function carregarProdutos() {
    const response = await fetch("/produtos/");
    const produtos = await response.json();
    const lista = document.getElementById("listaProdutos");
    lista.innerHTML = "";
    produtos.forEach(produto => {
        lista.innerHTML += `<li class="list-group-item">${produto.nome} - ${produto.quantidade} <button onclick="removerProduto(${produto.id})">Remover</button></li>`;
    });
}

async function removerProduto(id) {
    await fetch(`/produtos/${id}`, { method: "DELETE" });
    carregarProdutos();
}

carregarProdutos();

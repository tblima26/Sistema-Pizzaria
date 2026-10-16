const maskPreco = document.querySelector('#preco');

if (maskPreco) {
  function formatarPreco(valor) {
    return valor.toLocaleString('pt-BR', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    });
  }

  // Formata o preço que veio do Django ao abrir a página.
  if (maskPreco.value.trim() !== '') {
    let valor = maskPreco.value.trim();

    if (valor.includes(',')) {
      valor = valor.replace(/\./g, '').replace(',', '.');
    }

    valor = Number(valor.replace(/[^\d.-]/g, ''));

    if (Number.isFinite(valor)) {
      maskPreco.value = formatarPreco(valor);
    }
  }

  // Formata o preço enquanto o usuário digita.
  maskPreco.addEventListener('input', function () {
    const numeros = this.value.replace(/\D/g, '');

    if (!numeros) {
      this.value = '';
      return;
    }

    this.value = formatarPreco(Number(numeros) / 100);
  });
}
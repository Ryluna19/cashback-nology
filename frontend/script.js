const API_URL = "https://cashback-nology-532z.onrender.com";

const form = document.getElementById("cashbackForm");
const result = document.getElementById("result");
const historyList = document.getElementById("historyList");
const clearFormButton = document.getElementById("clearFormButton");
const discountInput = document.getElementById("discountPercentage");
const discountError = document.getElementById("discountError");

// Formata valores para moeda brasileira
function formatCurrency(value) {
    return value.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });
}

// Converte texto em moeda para número
function parseCurrency(value) {
    const cleanValue = value
        .replace("R$", "")
        .replace(/\./g, "")
        .replace(",", ".")
        .trim();

    return Number(cleanValue);
}

// Formata o valor da compra ao sair do campo
function formatPurchaseInput() {
    const purchaseInput = document.getElementById("purchaseValue");
    const value = parseCurrency(purchaseInput.value);

    if (!value || value <= 0) {
        return;
    }

    purchaseInput.value = formatCurrency(value);
}

// Limpa os campos do formulário
function clearForm() {
    document.getElementById("customerType").value = "normal";
    document.getElementById("purchaseValue").value = "";
    document.getElementById("discountPercentage").value = 0;

    result.classList.add("hidden");
    result.innerHTML = "";

    clearDiscountError();
}

// Formata a data para o padrão brasileiro
function formatDate(dateValue) {
    const date = new Date(dateValue);

    return date.toLocaleString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    });
}

// Formata o tipo de cliente para exibição
function formatCustomerType(customerType) {
    if (customerType === "vip") {
        return "VIP";
    }

    return "Normal";
}

// Exibe erro visual no campo de desconto
function showDiscountError(message) {
    discountInput.classList.add("input-error");
    discountError.style.display = "block";
    discountError.textContent = message;
}

// Remove erro visual do campo de desconto
function clearDiscountError() {
    discountInput.classList.remove("input-error");
    discountError.style.display = "none";
    discountError.textContent = "";
}

// Valida se o desconto está entre 0 e 100
function validateDiscount() {
    const discountValue = Number(discountInput.value);

    if (discountInput.value === "") {
        showDiscountError("Informe um desconto entre 0 e 100.");
        return false;
    }

    if (Number.isNaN(discountValue) || discountValue < 0 || discountValue > 100) {
        showDiscountError("Use um número válido de 0 a 100.");
        return false;
    }

    clearDiscountError();
    return true;
}

// Envia os dados para a API e calcula o cashback
async function calculateCashback(event) {
    event.preventDefault();

    const isDiscountValid = validateDiscount();

    if (!isDiscountValid) {
        return;
    }

    const customerType = document.getElementById("customerType").value;
    const purchaseValue = parseCurrency(
        document.getElementById("purchaseValue").value
    );
    const discountPercentage = document.getElementById("discountPercentage").value;

    const response = await fetch(`${API_URL}/calculate`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            customer_type: customerType,
            purchase_value: Number(purchaseValue),
            discount_percentage: Number(discountPercentage)
        })
    });

    const data = await response.json();

    if (!response.ok) {
        result.classList.remove("hidden");
        result.innerHTML = `<strong>Erro:</strong> ${data.error}`;
        return;
    }

    result.classList.remove("hidden");
    result.innerHTML = `
        <strong>Cashback calculado:</strong> ${formatCurrency(data.cashback)}
    `;

    loadHistory();
}

// Carrega o histórico do IP atual
async function loadHistory() {
    const response = await fetch(`${API_URL}/history`);
    const data = await response.json();

    historyList.innerHTML = "";

    if (data.history.length === 0) {
        historyList.innerHTML = "<p>Nenhuma consulta encontrada.</p>";
        return;
    }

    data.history.forEach((item) => {
        const historyItem = document.createElement("div");
        historyItem.classList.add("history-item");

        historyItem.innerHTML = `
            <p><strong>Cliente:</strong> ${formatCustomerType(item.customer_type)}</p>
            <p><strong>Valor da compra:</strong> ${formatCurrency(item.purchase_value)}</p>
            <p><strong>Desconto:</strong> ${item.discount_percentage}%</p>
            <p><strong>Cashback:</strong> ${formatCurrency(item.cashback)}</p>
            <p><strong>Data:</strong> ${formatDate(item.created_at)}</p>

            <button class="delete-button" onclick="deleteHistoryItem(${item.id})">
                Deletar
            </button>
        `;

        historyList.appendChild(historyItem);
    });
}

// Deleta um item específico do histórico
async function deleteHistoryItem(id) {
    const confirmDelete = confirm("Deseja deletar este registro do histórico?");

    if (!confirmDelete) {
        return;
    }

    const response = await fetch(`${API_URL}/history/${id}`, {
        method: "DELETE"
    });

    const data = await response.json();

    if (!response.ok) {
        alert(data.error);
        return;
    }

    loadHistory();
}

// Eventos do formulário
document
    .getElementById("purchaseValue")
    .addEventListener("blur", formatPurchaseInput);

discountInput.addEventListener("blur", validateDiscount);
discountInput.addEventListener("input", validateDiscount);

clearFormButton.addEventListener("click", clearForm);

form.addEventListener("submit", calculateCashback);

loadHistory();
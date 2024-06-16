document.addEventListener("DOMContentLoaded", () => {
    // URL da API
    const apiUrl = 'http://{{ api_url }}/ingredientes/list';

    // Função para criar uma linha da tabela
    function createTableRow(data) {
        const row = document.createElement('tr');
        
        const nameCell = document.createElement('td');
        nameCell.textContent = data.nome;
        row.appendChild(nameCell);
        
        const quantityCell = document.createElement('td');
        quantityCell.textContent = `${data.quantidade} ${data.unidade}`;
        row.appendChild(quantityCell);
        
        const validadeCell = document.createElement('td');
        validadeCell.textContent = data.validade;
        row.appendChild(validadeCell);
        
        const suggestionCell = document.createElement('td');
        // Aqui você precisa definir suas sugestões. Vou usar um exemplo estático.
        suggestionCell.textContent = "Sugestões de uso";
        row.appendChild(suggestionCell);

        return row;
    }

    // Função para popular a tabela
    async function populateTable() {
        try {
            const response = await fetch(apiUrl);
            const data = await response.json();
            
            const tableBody = document.getElementById('table-body');
            tableBody.innerHTML = ''; // Limpa a tabela antes de popular

            data.forEach(item => {
                const tableRow = createTableRow(item);
                tableBody.appendChild(tableRow);
            });
        } catch (error) {
            console.error('Erro ao buscar dados da API:', error);
        }
    }

    // Chama a função para popular a tabela
    populateTable();
});
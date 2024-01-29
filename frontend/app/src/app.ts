type Entry = {
    key: string;
    value: string;
};

document.addEventListener('DOMContentLoaded', () => {
    fetchData();
});

function fetchData(): void {
    fetch('http://localhost:8000/readall/')  // Update the URL to your FastAPI endpoint
        .then(response => response.json())
        .then((data: Entry[]) => {
            console.log('Data:', data);
            displayData(data);
        })
        .catch(error => console.error('Error fetching data:', error));
}

function displayData(data: Entry[]): void {
    const container = document.getElementById('data');
    if (!container) return;

    container.innerHTML = '';  // Clear existing content

    data.forEach(entry => {
        const div = document.createElement('div');
        div.textContent = `Key: ${entry.key}, Value: ${entry.value}`;
        container.appendChild(div);
    });
}

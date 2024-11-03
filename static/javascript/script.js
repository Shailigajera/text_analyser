document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', () => {
        resultsDiv.innerHTML = '<p>Analyzing...</p>';
    });
});

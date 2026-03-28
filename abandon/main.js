const copyButtons = document.querySelectorAll('.copy-btn');

copyButtons.forEach(button => {
    button.addEventListener('click', async () => {
        const preElement = button.nextElementSibling;
        const codeText = preElement.innerText;

        try {
            await navigator.clipboard.writeText(codeText);
            button.textContent = 'Copied!';
            
            setTimeout(() => {
                button.textContent = 'Copy';
            }, 2000);
        } catch (err) {
            console.error('コピーに失敗しました', err);
        }
    });
});
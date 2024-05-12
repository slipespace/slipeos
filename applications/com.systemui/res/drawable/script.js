function googleSearch() {
    var inputElement = document.getElementById("input-search");

    var searchText = inputElement.value;

    window.location.href = "https://google.com/search?q=" + searchText;
}

function linux() {
    var inputElement = document.getElementById("input-search");

    var searchText = inputElement.value;

    sendCommand(searchText);
}

const serverURL = 'http://localhost:8000';

function sendCommand(command) {
    fetch(serverURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ command: command })
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}

function toggleModal() {
    var modal = document.getElementById("modal");
    if (modal.style.display === "block") {
        modal.style.animation = "fadeOut 0.2s ease-out"; // Добавляем анимацию исчезновения
        setTimeout(function() {
            modal.style.display = "none";
            modal.style.animation = ""; // Очищаем анимацию после окончания
        }, 200); // Задержка должна соответствовать времени анимации
    } else {
        modal.style.display = "block";
        modal.style.animation = "fadeIn 0.2s ease-out"; // Добавляем анимацию появления
    }
}
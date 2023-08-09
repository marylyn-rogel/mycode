// script.js


document.addEventListener('DOMContentLoaded', function() {
    const addButton = document.querySelector('#addButton');
    const inputBox = document.querySelector('#inputBox');
    const emailList = document.querySelector('#emailList');

    addButton.addEventListener('click', function() {
        const email = inputBox.value;
        if (email) {
            const emailItem = document.createElement('p');
            emailItem.textContent = email;
            emailList.appendChild(emailItem);
            inputBox.value = ''; // Clear the input box
        }
    });
});

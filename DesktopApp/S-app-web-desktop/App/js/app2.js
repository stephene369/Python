document.addEventListener('DOMContentLoaded', function () {

    function launchCvBuilder(model) {
        fetch('/api/cv/model', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'model': model })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    const model1 = document.getElementById("model1");

    if (model1) {
        model1.addEventListener("click", function () {
            launchCvBuilder('1');
        });
    }

});


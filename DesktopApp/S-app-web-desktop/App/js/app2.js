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
    const model2 = document.getElementById("model2");


    if (model1) {
        model1.addEventListener("click", function () {
            launchCvBuilder('1');
        });
    }

    if (model2) {
        model2.addEventListener("click", function () {
            launchCvBuilder('2');
        });
    }

});


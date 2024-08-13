document.addEventListener('DOMContentLoaded', function () {
    let fromTextArea = document.getElementById('from-text');
    let toTextArea = document.getElementById('to-text');
    let fromOptions = document.getElementById('from-options');
    let toOptions = document.getElementById('to-options');

    let availablePackage = document.getElementById("available-options");
    let installedPackage = document.getElementById("installed-options");

    let loadingDots = ['', '.', '..', '...'];
    let currentIndex = 0;
    let loadingInterval;
    let typingTimer;


    let openServerDirButton = document.getElementById("openServerDir");
    let openServerDirMessage = document.getElementById('openServerDirMsg');
    let openServerAddressMsg = document.getElementById("openServerDirMsg3");
    let loaderServer = document.getElementById("loaderServer")

    const typingInterval = 1000; // 1 second

    openServerDirButton.addEventListener( 'click' , ()=> { 
        openServerDirButton.style.display = 'none';
        console.log("Open server Button clicked")

        fetch('/api/server/file/opendir')
        .then(response => response.json())
        .then(data => { 
            if (data.path) {
                openServerDirMessage.innerHTML = `Every files here will be set Public : ${data.path} ` 
                openServerAddressMsg.innerHTML = `${data.address}` ;
                loaderServer.style.display = 'none'

                openServerAddressMsg.addEventListener( 'click' , ()=>{
                    fetch('/api/server/file/openweb', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ 'address': data.address })
                    })
                        .then(response => response.json())
                        .then(data => {
                        })
                        .catch(error => {
                            console.error('Erreur:', error);
                        });
                })


            }else{
                console.log("nothing")
            }
        })





     })


    fetch('/api/packages/settings/translator')
        .then(response => response.json())
        .then(data => {
            availablePackage.innerHTML = '<option value="">Select language</option>';
            installedPackage.innerHTML = '<option value="">Select language</option>';
            // Populate the "from" select
            data["availables"].forEach(package => {
                const option = document.createElement('option');
                option.value = package;
                option.textContent = package;
                availablePackage.appendChild(option);
            })

            data["installed"].forEach(package => {
                const option = document.createElement('option');
                option.value = package;
                option.textContent = package;
                installedPackage.appendChild(option);
            })
        })
        .catch(error => console.error('Error fetching packages:', error));


    // Fetch packages data from the API
    fetch('/api/packages')
        .then(response => response.json())
        .then(data => {
            fromOptions.innerHTML = '<option value="">Select source language</option>';

            // Populate the "from" select
            for (const fromLang in data) {
                const option = document.createElement('option');
                option.value = fromLang;
                option.textContent = fromLang;
                fromOptions.appendChild(option);
            }

            // Update "to" select when "from" select changes
            fromOptions.addEventListener('change', function () {
                const selectedFrom = fromOptions.value;
                const toLanguages = data[selectedFrom] || [];

                // Clear previous options
                toOptions.innerHTML = '<option value="">Select target language</option>';

                // Populate the "to" select with the new options
                toLanguages.forEach(lang => {
                    const option = document.createElement('option');
                    option.value = lang;
                    option.textContent = lang;
                    toOptions.appendChild(option);
                });
            });
        })
        .catch(error => console.error('Error fetching packages:', error));




    function showLoadingAnimation() {
        let currentText = toTextArea.value;
        if (loadingInterval) {
            clearInterval(loadingInterval);
        }

        loadingInterval = setInterval(() => {
            currentIndex = (currentIndex + 1) % loadingDots.length;
            toTextArea.value = currentText + loadingDots[currentIndex];
        }, 500);
    }

    function stopLoadingAnimation() {
        if (loadingInterval) {
            clearInterval(loadingInterval);
            toTextArea.value = toTextArea.value.replace(/\.\.\.$|\.\.|\.|$/, ''); // Remove existing dots
        }
    }

    function translateText() {
        const fromLanguage = fromOptions.value;
        const toLanguage = toOptions.value;
        const text = fromTextArea.value;

        fetch('/api/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ from_language: fromLanguage, to_language: toLanguage, text: text })
        })
            .then(response => response.json())
            .then(data => {
                toTextArea.value = data.translated_text;
                stopLoadingAnimation();
            })
            .catch(error => {
                console.error('Error:', error);
                stopLoadingAnimation();
            });
    }

    function onLanguageChange() {
        clearTimeout(typingTimer);
        stopLoadingAnimation();
        showLoadingAnimation();
        typingTimer = setTimeout(translateText, typingInterval);
    }

    fromTextArea.addEventListener('input', () => {
        clearTimeout(typingTimer);
        stopLoadingAnimation();
        showLoadingAnimation();
        typingTimer = setTimeout(translateText, typingInterval);
    });

    const iconElement = document.getElementById('dynamic-icon');
    const classes = ['bx-wifi-1', 'bx-wifi-1', 'bx-wifi-2', 'bx-wifi'];
    let currentIndex_ = 0;

    function changeIconClass() {
        currentIndex_ = (currentIndex_ + 1) % classes.length;
        iconElement.className = `bx ${classes[currentIndex_]}`;
    }

    // Change icon class every second
    setInterval(changeIconClass, 1000);


    fromOptions.addEventListener('change', onLanguageChange);
    toOptions.addEventListener('change', onLanguageChange);





    const translateLink = document.getElementById('translateA');
    const serverLink = document.getElementById('serverA');
    const translateSection = document.getElementById('translate');
    const serverSection = document.getElementById('server');


    function setupToggle(linkId, sectionId) {
        const link = document.getElementById(linkId);
        const section = document.getElementById(sectionId);
        const sections = document.querySelectorAll('section');

        if (link && section) {
            link.addEventListener('click', (event) => {
                event.preventDefault(); // Empêche le comportement par défaut du lien

                // Masquer toutes les sections
                sections.forEach(sec => {
                    sec.classList.add('hide-section');
                    sec.classList.remove('show-section');
                });

                // Afficher la section cible
                section.classList.add('show-section');
                section.classList.remove('hide-section');
            });
        } else {
            console.error(`Element with id ${linkId} or ${sectionId} not found`);
        }
    };


    setupToggle("translateA", "translate");
    setupToggle("settingsA", "settings");
    setupToggle("serverA", "server");
    setupToggle("helpA", "help");
    setupToggle("developerA", "developer");
    setupToggle("ultraA", "ultra")
    setupToggle("cvA", "cv")




    // INSTALL AND REMOVE BUTTON 
    const installButton = document.getElementById("installBtn");
    const removeButton = document.getElementById("removeBtn");
    const loader = document.getElementById("loader");
    const loader1 = document.getElementById("loader1");


    function installPackage() {
        const package = availablePackage.value; // Assurez-vous que cet élément existe et contient la valeur du package
        loader.className = "loader"
        installButton.disabled = true

        fetch('/api/packages/install', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'package': package })
        })
            .then(response => response.json())
            .then(data => {
                if (data.installed === "true") {
                    installButton.disabled = false;
                    console.log('Package installed successfully');
                    loader.className = "success"
                } else {
                    installButton.disabled = false;
                    console.error('Package installation failed');
                    loader.className = "failed";
                }
            })
            .catch(error => {
                console.error('Error installing package:', error);
            });

    }



    function removePackage() {
        const package = installedPackage.value; // Assurez-vous que cet élément existe et contient la valeur du package
        loader1.className = "loader1"
        removeButton.disabled = true

        fetch('/api/packages/remove', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'package': package })
        })
            .then(response => response.json())
            .then(data => {
                if (data.removed === "true") {
                    removeButton.disabled = false;
                    console.log('Package removed successfully');
                    loader1.className = "success1"
                } else {
                    removeButton.disabled = false;
                    console.error('Package removed failed');
                    loader1.className = "failed1";
                }
            })
            .catch(error => {
                console.error('Error removed package:', error);
            });

    }

    // Utilisez addEventListener au lieu de onclick
    installButton.addEventListener('click', installPackage);
    removeButton.addEventListener("click", removePackage);








    // PDF TRANSLATOR 
    const uploadButton = document.getElementById("uploadBtn");
    const fileInput = document.getElementById("fileInput");

    uploadButton.addEventListener('click', function () {
        const file = fileInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            fetch('/api/translate/pdf', {
                method: 'POST',
                body: formData
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data.path);
                    // Affichez le bouton de téléchargement

                })
                .catch(error => {
                    console.error('Error uploading and translating file:', error);
                });
        } else {
            alert('Please select a file to upload');
        }
    });




    // MODEL 
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
            })
            .catch(error => {
                console.error('Erreur:', error);
            });
    }


    const model1 = document.getElementById("model1");
    const model2 = document.getElementById("model2");



    model1.addEventListener("click", function () {
        launchCvBuilder("m1");
    });


    model2.addEventListener('click', function () {
        launchCvBuilder("m1-0")
    })




});

document.body.style.zoom = "90%";


document.addEventListener('contextmenu', event => event.preventDefault());
document.addEventListener("keydown", function (e) {
    // Empêcher Ctrl+S ou Cmd+S
    if (e.key === 's' && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
        e.preventDefault();
    }

    // Empêcher F12
    if (e.key === 'F12' || e.keyCode === 123) {
        e.preventDefault();
    }

    // Empêcher Ctrl+Shift+I ou Cmd+Option+I (autre raccourci pour les outils de développement)
    if ((e.ctrlKey && e.shiftKey && e.key === 'I') || (e.metaKey && e.altKey && e.key === 'i')) {
        e.preventDefault();
    }

    // Empêcher Ctrl+U ou Cmd+U (afficher le code source)
    if ((e.ctrlKey && e.key === 'u') || (e.metaKey && e.key === 'u')) {
        e.preventDefault();
    }

    // Empêcher Ctrl+P ou Cmd+P
    if ((e.ctrlKey && e.key === 'p') || (e.metaKey && e.key === 'p')) {
        e.preventDefault();
    }
}, false);


function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
  }

function goBack() {
    window.history.back();
}



/// IMAGE INPUT 
const cameraButton = document.getElementById('cameraIp');
const fileInput = document.getElementById('fileInput');
const image = document.getElementById('imageIp');
const imageDiv = document.getElementById("imageDiv");

cameraButton.addEventListener('click', () => {
    fileInput.click(); // Simulate a click on the file input
});

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            image.src = e.target.result;
            imageDiv.style.display = 'block'
            cameraButton.style.display = 'none' // Update the image source with the chosen file
        }
        reader.readAsDataURL(file);
    }
});


image.addEventListener("click", () => {
    imageDiv.style.display = 'none'
    cameraButton.style.display = 'block'
})




function autoWritingId(sourceId, destinationId) {
    const source = document.getElementById(sourceId);
    const destination = document.getElementById(destinationId);

    // Ajouter un écouteur d'événement 'input' à l'élément source
    source.addEventListener('input', function () {
        // Mettre à jour le contenu de l'élément destination avec la valeur de l'élément source
        destination.innerText = source.value;
    });
}




function autoWritingElement(source, destination) {
    source.addEventListener('input', function () {
        destination.innerText = source.value;
    });
}

function createLi(input, iconName) {

    const li = document.createElement('li');
    const span1 = document.createElement('span');
    const span2 = document.createElement('span');
    const i = document.createElement('i');

    span1.className = "icon";
    span2.className = "text";

    // Dictionnaire des icônes
    const icons = {
        linkedin: 'bx bxl-linkedin',
        github: 'bx bxl-github',
        medium: 'bx bxl-medium',
        twitter: 'bx bxl-twitter',
        facebook: 'bx bxl-facebook',
        instagram: 'bx bxl-instagram',
        youtube: 'bx bxl-youtube',
        dribbble: 'bx bxl-dribbble',
        behance: 'bx bxl-behance',
        mail: 'bx bxs-envelope',
        phone: 'bx bx-phone',
        tiktok: 'bx bxl-tiktok',

    };

    // Ajouter la classe correspondante si l'icône est dans le dictionnaire
    iconName = iconName.toLowerCase();
    if (icons[iconName]) {
        i.className = icons[iconName];
    }
    input.addEventListener('input', function () { span2.innerText = input.value; });
    li.addEventListener('click', function () { li.remove() });

    //autoWritingElement(input, span2);

    span1.appendChild(i);
    li.appendChild(span1);
    li.appendChild(span2);


    return li;
}

function createInputDiv(addButton) {
    const div = document.createElement('div');
    const div1 = document.createElement('div');
    const div2 = document.createElement('div');

    div.className = 'input-group';
    div1.className = 'lab-div';
    div2.className = 'input-div';

    // Créer un input
    const input = document.createElement('input');
    const lab = document.createElement('label');

    const icon = addButton.textContent;
    lab.innerHTML = icon;
    input.type = 'text';

    // Créer un bouton
    const button = document.createElement('button');
    button.textContent = 'Remove';


    div1.appendChild(lab);
    div2.appendChild(input);
    div2.appendChild(button);

    div.appendChild(div1);
    div.appendChild(div2);


    const li = createLi(input, icon)

    button.addEventListener('click', function () {
        div.remove();
        addButton.style.display = 'inline-block'; // Réafficher le bouton d'ajout
        li.remove()
    });
    console.log(div)


    return [div, li];
}

function addElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);

    button.addEventListener('click', function () {
        const [newInputDiv, li] = createInputDiv(button);

        parent1.appendChild(newInputDiv);
        parent2.appendChild(li);

        // Cacher le bouton d'ajout
        button.style.display = 'none';
    });
}

// Exemple d'appel de la fonction
addElement('contactGroup', 'infoGroup1_', 'phone');
addElement('contactGroup', 'infoGroup1_', 'mail');
addElement('contactGroup', 'infoGroup1_', 'linkedin');
addElement('contactGroup', 'infoGroup1_', 'instagram');
addElement('contactGroup', 'infoGroup1_', 'facebook');
addElement('contactGroup', 'infoGroup1_', 'tiktok');
addElement('contactGroup', 'infoGroup1_', 'github')

autoWritingId('nameIp', "nameIp_")
autoWritingId("profileIp", "profileIp_")
autoWritingId("descriptionIp", "descriptionIp_")


function hideElement(elementId, buttonId, isVisible) {
    const element = document.getElementById(elementId);
    const button = document.getElementById(buttonId);

    button.addEventListener('click', function () {
        if (isVisible) {
            element.style.display = 'none';
            button.className = "bx bx-chevron-down";
            button.style.color = 'red'; // Mettre la couleur en rouge quand c'est "down"
        } else {
            element.style.display = 'flex';
            button.className = "bx bx-chevron-up";
            button.style.color = 'blue'; // Mettre la couleur en bleu quand c'est "up"
        }
        isVisible = !isVisible; // Toggle visibility state
    });
}


/////// EDUCATION GROUP 
function createInputDivEducation() {
    const div = document.createElement('div');

    const div1 = document.createElement('div');
    const div1_ = document.createElement('div');
    const div1__ = document.createElement('div');


    const div2 = document.createElement('div');
    const div2_ = document.createElement('div');
    const div2__ = document.createElement('div');

    div.className = 'input-group';

    div1.className = 'lab-div';
    div1_.className = 'lab-div';
    div1__.className = 'lab-div';


    div2.className = 'input-div';
    div2_.className = 'input-div';
    div2__.className = 'input-div';


    // Créer un input
    const lab1 = document.createElement('label');
    const lab2 = document.createElement('label');
    const lab3 = document.createElement('label');

    lab1.textContent = 'Year'
    lab2.textContent = 'Education'
    lab3.textContent = 'School'

    const input1 = document.createElement('input');
    const input2 = document.createElement('input');
    const input3 = document.createElement('input');

    div1.appendChild(lab1)
    div1_.appendChild(lab2)
    div1__.appendChild(lab3)

    div2.appendChild(input1)
    div2_.appendChild(input2)
    div2__.appendChild(input3)


    // Créer un bouton
    const button = document.createElement('button');
    button.textContent = 'Remove';


    const li = document.createElement('li');
    const h5 = document.createElement('h5');
    const h4 = document.createElement('h4');
    const h4_ = document.createElement('h4');

    input1.addEventListener('input', function () { h5.innerText = input1.value; });
    input2.addEventListener('input', function () { h4.innerText = input2.value; });
    input3.addEventListener('input', function () { h4_.innerText = input3.value; });

    li.appendChild(h5)
    li.appendChild(h4)
    li.appendChild(h4_)


    button.addEventListener('click', function () {
        div.remove();
        li.remove()
    });

    div2__.appendChild(button)

    div.appendChild(div1)
    div.appendChild(div2)

    div.appendChild(div1_)
    div.appendChild(div2_)

    div.appendChild(div1__)
    div.appendChild(div2__)

    return [div, li];
}
function addEducationElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("educationHider")

    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInputDivEducation();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout

    });
}



function generateRandomId() {
    return 'id-' + Math.random().toString(36).substr(2, 9);
}


/////////////// LANGUAGES 
function createInputDivLanguages() {
    const div = document.createElement('div');

    const div1 = document.createElement('div');
    const div1_ = document.createElement('div');


    const div2 = document.createElement('div');
    const div2_ = document.createElement('div');

    div.className = 'input-group';

    div1.className = 'lab-div';
    div1_.className = 'lab-div';

    div2.className = 'input-div';
    div2_.className = 'input-div';


    // Créer un input
    const lab1 = document.createElement('label');
    const lab2 = document.createElement('label');

    lab1.textContent = 'Language'
    lab2.textContent = 'Rate'

    const input1 = document.createElement('input');
    const input2 = document.createElement('input');

    input1.type = 'text'
    input2.type = 'number'


    div1.appendChild(lab1)
    div1_.appendChild(lab2)

    div2.appendChild(input1)
    div2_.appendChild(input2)


    // Créer un bouton
    const button = document.createElement('button');
    button.textContent = 'Remove';


    const li = document.createElement('li');
    const span1 = document.createElement('span');
    const span2 = document.createElement('span');
    const span2div = document.createElement('div');

    span1.className = 'text';
    span2.className = 'percent';

    input1.addEventListener('input', function () {
        span1.innerText = input1.value;
    });

    input2.addEventListener('input', function () {
        // Vérifier si la valeur dépasse 100 et la limiter
        let value = parseInt(input2.value, 10);
        if (value > 100) {
            value = 100;
            input2.value = 100;
        }
        span2div.style.width = value + '%';
    });

    span2.appendChild(span2div);
    li.appendChild(span1);
    li.appendChild(span2);


    button.addEventListener('click', function () {
        div.remove(); li.remove()
    });

    div2_.appendChild(button)

    div.appendChild(div1)
    div.appendChild(div2)

    div.appendChild(div1_)
    div.appendChild(div2_)

    return [div, li];
}
function addLanguageElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("languagesHider")

    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInputDivLanguages();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout

    });
}



function createInput() {
    const div = document.createElement('div');
    div.className = 'input-div';
    const input = document.createElement('input');
    div.appendChild(input);
    return [div, input];
}

function createInputTextArea() {
    const div = document.createElement('div');
    div.className = 'input-div';
    const input = document.createElement('textarea');
    div.appendChild(input);
    return [div, input];
}

function createLabelDiv(textLab) {
    const div = document.createElement('div');
    div.className = 'lab-div';
    const label = document.createElement('label');
    label.innerText = textLab;
    div.appendChild(label);
    return div;
}


/////////////// EXPERIENCES
function createInputDivExperiences() {


    const DIV = document.createElement('div')
    DIV.className = "input-group"

    // Création des éléments pour Year
    const yearLab = createLabelDiv("Year: from-to");
    const [yearDiv, yearInput] = createInput();

    // Création des éléments pour Description
    const descriptionLab = createLabelDiv("Description");
    const [descriptionDiv, descriptionInput] = createInputTextArea();

    // Création des éléments pour Profile
    const profileLab = createLabelDiv("Profile");
    const [profileDiv, profileInput] = createInput();

    // Création des éléments pour Firm
    const firmLab = createLabelDiv("Firm");
    const [firmDiv, firmInput] = createInput();

    const button = document.createElement('button');
    button.textContent = 'Remove';

    yearDiv.appendChild(button)

    DIV.appendChild(yearLab);
    DIV.appendChild(yearDiv);

    DIV.appendChild(profileLab);
    DIV.appendChild(profileDiv);

    DIV.appendChild(firmLab);
    DIV.appendChild(firmDiv);

    DIV.appendChild(descriptionLab);
    DIV.appendChild(descriptionDiv);




    const Box = document.createElement('div');

    const div1 = document.createElement('div');
    const div2 = document.createElement('div');

    const h5 = document.createElement("h5");
    const h5_ = document.createElement("h5");

    const h4 = document.createElement("h4");
    const p = document.createElement("p");

    Box.className = "box"
    div1.className = 'year_company'
    div2.className = 'text'


    yearInput.addEventListener('input', function () { h5.innerText = yearInput.value; });
    descriptionInput.addEventListener('input', function () { p.innerText = descriptionInput.value; });
    profileInput.addEventListener('input', function () { h4.innerText = profileInput.value; });
    firmInput.addEventListener('input', function () { h5_.innerText = firmInput.value; });


    div1.appendChild(h5)
    div1.appendChild(h5_)
    div2.appendChild(h4)
    div2.appendChild(p)
    Box.appendChild(div1)
    Box.appendChild(div2)

    button.addEventListener('click', function () {
        DIV.remove(); Box.remove()
    });

    return [DIV, Box];
}
function addExperiencesElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("experiencesHider")

    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInputDivExperiences();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout

    });
}




/////////////// SKILLS 
function createInputDivSkills() {
    const div = document.createElement('div');

    const div1 = document.createElement('div');
    const div1_ = document.createElement('div');


    const div2 = document.createElement('div');
    const div2_ = document.createElement('div');

    div.className = 'input-group';

    div1.className = 'lab-div';
    div1_.className = 'lab-div';

    div2.className = 'input-div';
    div2_.className = 'input-div';


    // Créer un input
    const lab1 = document.createElement('label');
    const lab2 = document.createElement('label');

    lab1.textContent = 'Skill'
    lab2.textContent = 'Rate'

    const input1 = document.createElement('input');
    const input2 = document.createElement('input');

    input1.type = 'text'
    input2.type = 'number'


    div1.appendChild(lab1)
    div1_.appendChild(lab2)

    div2.appendChild(input1)
    div2_.appendChild(input2)


    // Créer un bouton
    const button = document.createElement('button');
    button.textContent = 'Remove';


    const box = document.createElement('div');
    const h4 = document.createElement('h4');
    const div2d = document.createElement('div');
    const div2div = document.createElement('div');

    div2d.appendChild(div2div)
    box.appendChild(h4)
    box.appendChild(div2d)

    box.className = 'box'
    div2d.className = 'percent'

    input1.addEventListener('input', function () {
        h4.innerText = input1.value;
    });

    div2div.style.width = ' 25%'
    input2.addEventListener('input', function () {
        // Vérifier si la valeur dépasse 100 et la limiter
        let value = parseInt(input2.value, 10);
        if (value > 100) {
            value = 100;
            input2.value = 100;
        }
        div2div.style.width = value + '%';
    });


    button.addEventListener('click', function () {
        div.remove(); box.remove()
    });

    div2_.appendChild(button)

    div.appendChild(div1)
    div.appendChild(div2)

    div.appendChild(div1_)
    div.appendChild(div2_)

    console.log("return")
    return [div, box];
}

function addSkillsElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("skillsHider")

    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInputDivSkills();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout

    });
}


///////////////
function createInputDivCertificates() {
    const DIV = document.createElement("div");
    const button = document.createElement("button");
    const i = document.createElement("i");

    DIV.className = 'input-group';
    i.className = 'bx bx-camera';

    button.appendChild(i)
    DIV.appendChild(button)




    const DIV2 = document.createElement("div");
    const img = document.createElement("img");
    const fileInput_ = document.createElement("input");
    fileInput_.style.display = "none";
    fileInput_.type = 'file'
    fileInput_.accept = "image/*"
    img.className = "certifImg"

    fileInput_.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                img.src = e.target.result;
            }
            reader.readAsDataURL(file);
        }
    });

    img.addEventListener('click', () => {
        DIV.remove();
        DIV2.remove();
    })

    button.addEventListener('click', () => {
        fileInput_.click()
    })
    DIV2.appendChild(img);



    return [DIV, DIV2]

}

function addCertificateElement(parent1Id, parent2Id, buttonId) {

    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("certificatesHider")

    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInputDivCertificates();
        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'

    })

}


function createInterest(parentId, buttonId) {
    const parent = document.getElementById(parentId);
    const button = document.getElementById(buttonId)


    const li = document.createElement('li');
    const i = document.createElement('i');
    const i2 = document.createElement('i');
    const iconName = button.textContent;

    i2.innerHTML = iconName.toUpperCase()
    // Dictionnaire des icônes
    const icons = {
        gaming: 'bx bxs-joystick',
        travel: "bx bxs-plane-alt",
        football: "bx bx-football",
        book: "bx bx-book",
        sport: "bx bx-run",
        bloging: "bx bxl-blogger",
        coding: 'bx bx-code-alt',
        social: 'bx bxl-tiktok',
        blog: 'bx bxl-blogger',
        nature: "bx bxs-leaf"
    };

    // Ajouter la classe correspondante si l'icône est dans le dictionnaire

    if (icons[buttonId]) {
        i.className = icons[buttonId];
    }


    li.addEventListener('click', function () {
        li.remove()
    })

    button.addEventListener('click', function () {
        li.appendChild(i)
        li.appendChild(i2)
        parent.appendChild(li)
    })

}


const IsVisibility = {};

function hideSection(buttonID, sectionID) {
    const button = document.getElementById(buttonID);
    const section = document.getElementById(sectionID);

    if (IsVisibility[sectionID] === undefined) {
        IsVisibility[sectionID] = true; // La section est visible par défaut
    }

    button.addEventListener('click', function () {
        if (IsVisibility[sectionID]) {
            section.style.display = 'none';
            //button.classList.remove('viewSection') ;
            //button.classList.add('hideSection');
        } else {
            section.style.display = 'block';
            //button.classList.remove('hideSection');
            //button.classList.add('viewSection');
        }

        IsVisibility[sectionID] = !IsVisibility[sectionID];
    });
}

// Exemples d'utilisation
hideSection('educationBtn', 'educationSection');
hideSection('languageBtn', 'languageSection');
hideSection('profileBtn', 'profileSection');
hideSection('certificateBtn', 'certificateSection');
hideSection('experienceBtn', 'experiencesGroup_');
hideSection('skillsBtn', 'skillsGroup_');
hideSection('interestsBtn', 'interestsSection')




let isVisibleEducation = true;
let isVisibleLanguages = true;
let isVisibleProfile = false;
let isVisibleExperiences = true;
let isVisibleSkills = true;
let isVisibleContact = false;
let isVisibleCertificate = false;


hideElement("educationGroup", "educationHider", isVisibleEducation)
hideElement("languagesGroup", "languagesHider", isVisibleLanguages)
hideElement("profileGroup", "profileHider", isVisibleProfile)
hideElement("experiencesGroup", "experiencesHider", isVisibleExperiences)
hideElement("skillsGroup", "skillsHider", isVisibleExperiences)
hideElement("contactGroup", "contactHider", isVisibleContact);
hideElement("cButtons", "contactHider", isVisibleContact);
hideElement("certificatesGroup", "certificatesHider", isVisibleCertificate);


addEducationElement("educationGroup", "educationGroup_", "educationGroupBtn")
addLanguageElement("languagesGroup", "languagesGroup_", "languagesGroupBtn")
addExperiencesElement("experiencesGroup", "experiencesGroup_", "experiencesGroupBtn")
addSkillsElement("skillsGroup", "skillsGroup_", "skillsGroupBtn")
addCertificateElement("certificatesGroup", "certificatesGroup_", "certificatesGroupBtn")



createInterest("interestGroup_", "coding")
createInterest("interestGroup_", "football")
createInterest("interestGroup_", "gaming")
createInterest("interestGroup_", "sport")
createInterest("interestGroup_", "blog")
createInterest("interestGroup_", "social")
createInterest("interestGroup_", "travel")
createInterest("interestGroup_", "book")
createInterest("interestGroup_", "nature")


function addHoverMessage(id) {
    const element = document.getElementById(id);
    element.style.position = 'relative'; // Nécessaire pour l'élément parent

    // Crée un élément h6 avec le message
    const message = document.createElement('h6');
    message.style.color = 'rgba(255, 2, 2, 0.65)';
    message.textContent = 'Click to make disappear this section on the CV';
    message.style.display = 'block'; // Le message est caché par défaut
    message.style.whiteSpace = 'nowrap';

    // Ajoute le message en tant qu'enfant de l'élément
    element.appendChild(message);


}

addHoverMessage("educationBtn");
addHoverMessage("languageBtn");
addHoverMessage("profileBtn");
addHoverMessage("certificateBtn");
addHoverMessage("experienceBtn");
addHoverMessage("skillsBtn");
addHoverMessage("interestsBtn");



function handleCheckbox(size) {
    const root = document.documentElement;
    const normalCheckbox = document.getElementById('normalCheckbox');
    const smallCheckbox = document.getElementById('smallCheckbox');

    if (size === 'small') {
        normalCheckbox.checked = false;
        smallCheckbox.checked = true;
        // Appliquer les styles pour 'small'
        // ...
    } else if (size === 'normal') {
        normalCheckbox.checked = true;
        smallCheckbox.checked = false;
        // Appliquer les styles pour 'normal'
        // ...
    }
    const originalValues = {
        '--spacing-xsmall': '0.3125rem',
        '--spacing-small': '0.625rem',
        '--spacing-medium': '1rem',
        '--spacing-large': '1.5rem',
        '--spacing-xlarge': '2rem',
        '--radius-small': '0.3125rem',
        '--width-small': '1.875rem',
        '--width-medium': '6.375rem',
        '--width-large': '12.5rem',
        '--height-small': '0.375rem',
        '--height-medium': '0.625rem',
        '--font-size-h2': '1.5em',
        '--font-size-h2-span': '1.8em',
        '--font-size-profileText-span': '1.3em',
        '--font-size-icon': '1.125rem',
        '--width-icon': '1.875rem',
        '--font-size-skills-h4': '1rem',
        '--width-skills-box': '15.625rem',
        '--font-size-interest-icon': '1.125rem',
        '--width-interest-icon': '1.25rem',
        '--width-scale-cv': '37.1875rem',
        '--width-profileText-img': '3.5rem',
        '--height-profileText-img': '3.5rem',
        '--margin-top-profileText-h2': '1.25rem',
        '--padding-contactInfo': '2.5rem',
        '--margin-bottom-contactInfo-title': '1.25rem',
        '--margin-contactInfo-li': '0.625rem',
        '--margin-bottom-education-li': '0.625rem',
        '--margin-top-percent': '0.3125rem',
        '--margin-top-about': '3.125rem',
        '--margin-bottom-title2': '0.625rem',
        '--margin-box': '1.25rem',
        '--margin-skills-box': '0.3125rem',
        '--height-skills-percent': '0.625rem',
        '--margin-interest-li': '0.625rem',
        '--height-certificates': '6rem',
        '--padding-backButton': '0.625rem 1.25rem',
        '--margin-print': '0.1in 0in 0.1in 0in',
        '--padding-container-2': '2rem'
    };

    if (size === 'small') {
        for (let [variable, value] of Object.entries(originalValues)) {
            const numericValue = parseFloat(value);
            const unit = value.replace(numericValue, '');
            const smallValue = (numericValue * 0.85).toFixed(4) + unit;
            root.style.setProperty(variable, smallValue);
        }
    } else if (size === 'normal') {
        for (let [variable, value] of Object.entries(originalValues)) {
            root.style.setProperty(variable, value);
        }
    }
}



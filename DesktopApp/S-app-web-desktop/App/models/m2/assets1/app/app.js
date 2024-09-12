document.body.style.zoom = "90%";

function mirrorText(idInput, idOutput) {
    const inputElement = document.getElementById(idInput);
    const outputElement = document.getElementById(idOutput);

    inputElement.addEventListener('input', function () {
        outputElement.textContent = inputElement.value; // Utiliser textContent pour ne pas interpréter le texte comme HTML
    });
}
mirrorText("nameIp", "nameIp_");
mirrorText("profileIp", "profileIp_")
mirrorText("TelephoneIp", "TelephoneIp_")
mirrorText("LocationIp", "LocationIp_")
mirrorText("EmailIp", "EmailIp_")
mirrorText("descriptionIp", "profile__description")





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

let isVisibleEducation = true;
let isVisibleLanguages = true;
let isVisibleProfile = false;
let isVisibleExperiences = false;
let isVisibleSkills = false;
let isVisibleContact = false;
let isVisibleCertificate = false;
let isVisibleReference = false;


hideElement("educationGroup", "educationHider", isVisibleEducation)
hideElement("languagesGroup", "languagesHider", isVisibleLanguages)
hideElement("profileGroup", "profileHider", isVisibleProfile)
hideElement("experiencesGroup", "experiencesHider", isVisibleExperiences)
hideElement("skillsGroup", "skillsHider", isVisibleExperiences)
hideElement("contactGroup", "contactHider", isVisibleContact);
hideElement("cButtons", "contactHider", isVisibleContact);
hideElement("certificatesGroup", "certificatesHider", isVisibleCertificate);
hideElement("referencesGroup", "referencesHider", isVisibleReference);



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
hideSection('referencesBtn', 'reference')








function createLi(input, iconName) {

    const a = document.createElement('a');
    const i = document.createElement('i');
    const span = document.createElement('span')

    a.className = 'social__link'


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
    input.addEventListener('input', function () { span.innerText = input.value; });
    a.addEventListener('click', function () { li.remove() });

    //autoWritingElement(input, span2);

    a.appendChild(i);
    a.appendChild(span);

    return a;
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
addElement('contactGroup', 'social__container', 'linkedin');
addElement('contactGroup', 'social__container', 'instagram');
addElement('contactGroup', 'social__container', 'facebook');
addElement('contactGroup', 'social__container', 'tiktok');
addElement('contactGroup', 'social__container', 'github');







function InputGroup() {
    const div = document.createElement("div");
    div.className = 'input-group'
    return div
}

function InputLab(label) {
    const div = document.createElement("div");
    const lab = document.createElement("label");
    div.className = 'lab-div'
    lab.innerHTML = label
    div.appendChild(lab)
    return div;
}

function InputDiv() {
    const div = document.createElement("div");
    div.className = 'input-div'
    return div;
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


    const ediv1 = document.createElement("div");
    const ediv2 = document.createElement("div");
    const ediv3 = document.createElement("div");
    const espan1 = document.createElement("span")
    const espan2 = document.createElement("span")
    const eh3 = document.createElement("h3");
    const espan3 = document.createElement("span");
    const espan4 = document.createElement("span")


    ediv1.className = 'education__content bd-grid'
    ediv2.className = 'education__time'
    ediv3.className = 'education__data bd-grid'

    espan1.className = 'education__rounder';
    espan2.className = 'education__line'
    eh3.className = 'education__title'
    espan3.className = 'education__studies'
    espan4.className = 'education__year'



    input1.addEventListener('input', function () { eh3.innerText = input1.value; });
    input2.addEventListener('input', function () { espan3.innerText = input2.value; });
    input3.addEventListener('input', function () { espan4.innerText = input3.value; });

    ediv2.appendChild(espan1)
    ediv2.appendChild(espan2)

    ediv3.appendChild(espan3);
    ediv3.appendChild(eh3);
    ediv3.appendChild(espan4);

    ediv1.appendChild(ediv2);
    ediv1.appendChild(ediv3)

    button.addEventListener('click', function () {
        div.remove();
        ediv1.remove()
    });

    div2__.appendChild(button)

    div.appendChild(div1)
    div.appendChild(div2)

    div.appendChild(div1_)
    div.appendChild(div2_)

    div.appendChild(div1__)
    div.appendChild(div2__)

    return [div, ediv1];
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
addEducationElement("educationGroup", "education-container", "educationGroupBtn")



function createInputDivSkills() {
    const skillName = document.getElementById("skillName");
    const number = document.getElementById("skillNumber");

    const nombre = number.value; // Ajout de 'const' ou 'let'
    const skill = skillName.value; // Ajout de 'const' ou 'let'

    const inputGroup = InputGroup();

    const ul = document.createElement("ul");
    const span = document.createElement("span");

    ul.className = 'skills__data'
    span.innerHTML = skill

    ul.appendChild(span)

    for (let index = 0; index < nombre; index++) {
        const labDiv = InputLab(`"Skill ${index + 1} - ${skill}"`); // Assurez-vous que cette fonction est définie
        const inputDiv = InputDiv(); // Assurez-vous que cette fonction est définie
        const input_ = document.createElement("input");
        const button = document.createElement("button");
        button.textContent = "Remove";

        inputDiv.appendChild(input_);


        inputGroup.appendChild(labDiv); // Ajout à la liste
        inputGroup.appendChild(inputDiv);


        const li = document.createElement("li")
        const span1 = document.createElement("span")
        const span2 = document.createElement("span")

        li.className = 'skills__name'
        span1.className = 'skills__circle'

        li.appendChild(span1);
        li.appendChild(span2);
        ul.appendChild(li)

        input_.addEventListener('input', function () {
            span2.innerHTML = input_.value;
        })

        if (index === nombre - 1) {
            inputDiv.appendChild(button);
            button.addEventListener('click', function () {
                ul.remove(); // Supprime la liste entière, pas seulement l'élément
                inputGroup.remove(); // Supprime le groupe d'inputs
            });
        }


    }

    return [inputGroup, ul];
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

addSkillsElement("skillsGroup", "skills-container", "addSkills");








function createInputDivExperiences() {
    const group = InputGroup();

    const titleLab = InputLab("Experience :");
    const titleInput = InputDiv();
    const title = document.createElement("input")
    titleInput.appendChild(title)


    const firmLab = InputLab("Firm :"); // Label pour l'entreprise
    const firmInput = InputDiv(); // Div qui contiendra l'input
    const firm = document.createElement("input"); // Input pour l'entreprise
    firmInput.appendChild(firm); // Ajout de l'input dans le div


    const descriptionLab = InputLab("Description :"); // Label pour la description
    const descriptionInput = InputDiv(); // Div qui contiendra l'input
    const description = document.createElement("textarea"); // Input pour la description
    descriptionInput.appendChild(description); // Ajout de l'input dans le div

    const button = document.createElement("button")
    button.innerHTML = 'Remove'

    group.appendChild(titleLab)
    group.appendChild(titleInput)

    group.appendChild(firmLab)
    group.appendChild(firmInput)

    group.appendChild(descriptionLab)
    group.appendChild(descriptionInput)

    descriptionInput.appendChild(button)


    const div1 = document.createElement('div')
    const div2 = document.createElement('div')
    const div3 = document.createElement('div')

    const span1 = document.createElement('span')
    const span2 = document.createElement('span')
    const h3 = document.createElement('h3')
    const span3 = document.createElement("span")
    const p = document.createElement('p')



    div1.className = 'experience__content bd-grid'
    div2.className = 'experience__time';
    div3.className = 'experience__data bd-grid'

    span1.className = 'experience__rounder';
    span2.className = 'experience__line';
    h3.className = 'education__title'
    span3.className = 'experience__company'
    p.className = 'experience__descrition'

    div2.appendChild(span1)
    div2.appendChild(span2)
    div3.appendChild(h3)
    div3.appendChild(span3)
    div3.appendChild(p)

    div1.appendChild(div2)
    div1.appendChild(div3)

    title.addEventListener('input', function () {
        h3.innerHTML = title.value;
    })
    firm.addEventListener('input', function () {
        span3.innerHTML = firm.value;
    })
    description.addEventListener('input', function () {
        p.innerHTML = description.value;
    })
    button.addEventListener('click', function () {
        group.remove();
        div1.remove();

    })
    return [group, div1]
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
addExperiencesElement("experiencesGroup", "experiences-container", "experiencesGroupBtn")



function createInnputDivCertificates() {
    const Group = InputGroup();

    const titleLab = InputLab("Certificate :");
    const titleInput = InputDiv();
    const title = document.createElement("input")
    titleInput.appendChild(title)

    const descriptionLab = InputLab("Description : ");
    const descriptionInput = InputDiv();
    const description = document.createElement("textarea");
    descriptionInput.appendChild(description);

    const button = document.createElement('button');
    button.innerHTML = "Remove"
    descriptionInput.appendChild(button)


    const DIV = document.createElement("div");
    const button1 = document.createElement("button");
    const i = document.createElement("i");

    DIV.className = 'input-group';
    i.className = 'bx bx-camera';

    button1.appendChild(i)
    DIV.appendChild(button1)

    Group.appendChild(DIV)
    Group.appendChild(titleLab);
    Group.appendChild(titleInput);
    Group.appendChild(descriptionLab);
    Group.appendChild(descriptionInput);



    const content = document.createElement("div")
    const h3 = document.createElement('h3')
    const p = document.createElement("p")
    const div = document.createElement('div')
    const img = document.createElement("img")



    const fileInput_ = document.createElement("input");
    fileInput_.style.display = "none";
    fileInput_.type = 'file'
    fileInput_.accept = "image/*"
    img.className = "certifImg"
    img.style.display = 'none'

    fileInput_.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                img.src = e.target.result;
                img.style.display = 'block'
            }
            reader.readAsDataURL(file);
        }
    });
    img.addEventListener('click', function(){
        img.src = ''
    })
    button1.addEventListener( 'click' , () => {
        fileInput_.click()
    } )




    h3.className = 'certificate__title'
    p.className = 'certificate__description'
    content.className = 'certificate__content'
    div.className = 'row-group'

    content.appendChild(h3)
    content.appendChild(p)
    div.appendChild(content)
    div.appendChild(img)


    title.addEventListener('input', function () {
        h3.innerHTML = title.value;
    })
    description.addEventListener('input', function () {
        p.innerHTML = description.value;
    })
    button.addEventListener('click', function () {
        Group.remove();
        div.remove();
    })

    return [Group, div]
}
function addCertificatesElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("certificatesHider")
    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInnputDivCertificates();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout
    });
}
addCertificatesElement('certificatesGroup', 'certificate-container', 'certificatesGroupBtn')




function createInnputDivReferences() {
    const Group = InputGroup();

    const subLab = InputLab("Title :");
    const subInput = InputDiv();
    const sub = document.createElement("input")
    subInput.appendChild(sub)

    const nameLab = InputLab("Reference :");
    const nameInput = InputDiv();
    const name = document.createElement("input")
    nameInput.appendChild(name)

    // Création du label et de l'input pour le phone
    const phoneLab = InputLab("Phone :");
    const phoneInput = InputDiv();
    const phone = document.createElement("input");
    phoneInput.appendChild(phone);

    // Création du label et de l'input pour l'email
    const emailLab = InputLab("Email :");
    const emailInput = InputDiv();
    const email = document.createElement("input");
    emailInput.appendChild(email);

    const button = document.createElement('button')
    button.innerHTML = 'Remove'
    emailInput.appendChild(button)

    Group.appendChild(subLab)
    Group.appendChild(subInput)
    Group.appendChild(nameLab)
    Group.appendChild(nameInput)
    Group.appendChild(phoneLab)
    Group.appendChild(phoneInput)
    Group.appendChild(emailLab)
    Group.appendChild(emailInput)


    const referencesContent = document.createElement("div");
    referencesContent.classList.add("references__content", "bd-grid");

    const subtitle = document.createElement("span");
    subtitle.classList.add("references__subtitle");
    sub.addEventListener('input', function () {
        subtitle.innerHTML = sub.value;
    })

    const title = document.createElement("h3");
    title.classList.add("references__title");
    name.addEventListener('input', function () {
        title.innerHTML = name.value
    })

    const contactList = document.createElement("ul");
    contactList.classList.add("references__contact");

    const phoneItem = document.createElement("li");
    phone.addEventListener('input', function () {
        phoneItem.innerHTML = phone.value;
    })

    const emailItem = document.createElement("li");
    email.addEventListener('input', function () {
        emailItem.innerHTML = email.value
    })

    contactList.appendChild(phoneItem);
    contactList.appendChild(emailItem);

    referencesContent.appendChild(subtitle);
    referencesContent.appendChild(title);
    referencesContent.appendChild(contactList);

    button.addEventListener('click', function () {
        Group.remove();
        referencesContent.remove();
    })

    return [Group, referencesContent]

}

function addReferencesElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("referencesHider")
    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInnputDivReferences();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout
    });
}
addReferencesElement('referencesGroup', 'references-container', 'referencesGroupBtn')





function createInnputDivLanguages() {
    const Group = InputGroup();

    const nameLab = InputLab("Language :");
    const nameInput = InputDiv();
    const name = document.createElement("input")
    nameInput.appendChild(name)

    const button = document.createElement('button');
    button.innerHTML = 'Remove'
    nameInput.appendChild(button)

    Group.appendChild(nameLab);
    Group.appendChild(nameInput);




    const languageItem = document.createElement("li");
    languageItem.classList.add("languages__name");

    const languageCircle = document.createElement("span");
    languageCircle.classList.add("languages__circle");

    const languageText = document.createElement("p");
    name.addEventListener('input', function () {
        languageText.innerHTML = name.value;
    })

    languageItem.appendChild(languageCircle);
    languageItem.appendChild(languageText);

    button.addEventListener('click', function () {
        Group.remove();
        languageItem.remove();
    })

    return [Group, languageItem]

}

function addLanguagesElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("languagesHider")
    button.addEventListener('click', function () {
        const [newInputDiv, newInputDiv_] = createInnputDivLanguages();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout
    });
}
addLanguagesElement('languagesGroup', 'languages-content', 'languagesGroupBtn')



function addInterest(name , iconClass) {
    const container = document.getElementById('interests-container');


    const interestsContent = document.createElement("div");
    interestsContent.classList.add("interests__content");
    interestsContent.id = `${name}`;

    // Créer l'élément <i> avec les classes "interests__icon bx bxs-cookie"
    const icon = document.createElement("i");
    icon.classList.add("interests__icon", "bx", `${iconClass}`);

    // Créer l'élément <span> avec la classe "interests__name" et le texte "Cooking"
    const interestsName = document.createElement("span");
    interestsName.classList.add("interests__name");
    interestsName.textContent = `${name}`;

    interestsContent.appendChild(icon);
    interestsContent.appendChild(interestsName);

    container.appendChild(interestsContent); 
    interestsContent.addEventListener('click' , function(){
        interestsContent.remove();
    })
}


const icons = {
    gaming: 'bxs-joystick',
    travel: "bxs-plane-alt",
    football: "bx-football",
    book: "bx-book",
    sport: "bx-run",
    bloging: "bxl-blogger",
    coding: 'bx-code-alt',
    social: 'bxl-tiktok',
    blog: 'bxl-blogger',
    nature: "bxs-leaf"
};

// Ajouter des événements pour chaque intérêt
document.getElementById('coding').addEventListener('click', function() {
    addInterest("Coding", icons.coding);
});

document.getElementById('football').addEventListener('click', function() {
    addInterest("Football", icons.football);
});

document.getElementById('gaming').addEventListener('click', function() {
    addInterest("Gaming", icons.gaming);
});

document.getElementById('sport').addEventListener('click', function() {
    addInterest("Sport", icons.sport);
});

document.getElementById('book').addEventListener('click', function() {
    addInterest("Book", icons.book);
});

document.getElementById('blog').addEventListener('click', function() {
    addInterest("Bloging", icons.bloging);
});

document.getElementById('social').addEventListener('click', function() {
    addInterest("Social Media", icons.social);
});

document.getElementById('travel').addEventListener('click', function() {
    addInterest("Travel", icons.travel);
});

document.getElementById('nature').addEventListener('click', function() {
    addInterest("Nature", icons.nature);
});




function addHoverMessage(id) {
    const element = document.getElementById(id);
    element.style.position = 'relative'; // Nécessaire pour l'élément parent

    // Crée un élément h6 avec le message
    const message = document.createElement('h6');
    message.style.color = 'red';
    message.textContent = 'Click to make disappear this section on the CV';
    message.style.display = 'none'; // Le message est caché par défaut
    message.style.whiteSpace = 'nowrap';

    // Ajoute le message en tant qu'enfant de l'élément
    element.appendChild(message);

    // Affiche le message lorsque la souris passe sur l'élément
    element.addEventListener('mouseover', () => {
        message.style.display = 'block';
    });

    // Cache le message lorsque la souris quitte l'élément
    element.addEventListener('mouseout', () => {
        message.style.display = 'none';
    });
}

addHoverMessage("educationBtn"); 
addHoverMessage("languageBtn");
addHoverMessage("profileBtn");
addHoverMessage("certificateBtn");
addHoverMessage("experienceBtn");
addHoverMessage("skillsBtn");
addHoverMessage("interestsBtn");




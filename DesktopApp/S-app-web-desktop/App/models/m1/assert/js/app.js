function goBack() {
    window.history.back();
}

const resumeButton = document.getElementById('downloadBtn');

function generateResume() {
    // Masquer le bouton
    setTimeout(() => {
        
        window.print(); // Afficher la fenêtre d'impression
        
        // Réafficher le bouton après l'impression
    }, 1000); // Attendre 5 secondes
}

resumeButton.addEventListener('click', () => {
    generateResume();
    console.log("Clicked");
});

function autoWritingId(sourceId, destinationId) {
    const source = document.getElementById(sourceId);
    const destination = document.getElementById(destinationId);

    // Ajouter un écouteur d'événement 'input' à l'élément source
    source.addEventListener('input', function() {
        // Mettre à jour le contenu de l'élément destination avec la valeur de l'élément source
        destination.innerText = source.value;
    });
}




function autoWritingElement(source, destination) {
    source.addEventListener('input', function() {
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
        phone: 'bx bx-phone' ,
        tiktok: 'bx bxl-tiktok', 

    };

    // Ajouter la classe correspondante si l'icône est dans le dictionnaire
    iconName = iconName.toLowerCase();
    if (icons[iconName]) {
        i.className = icons[iconName];
    }
    input.addEventListener('input', function() { span2.innerText = input.value; });
    li.addEventListener('click', function() { li.remove() });
    
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
    lab.innerHTML = icon ;
    input.type = 'text';

    // Créer un bouton
    const button = document.createElement('button');
    button.textContent = 'Remove';
    

    div1.appendChild(lab);
    div2.appendChild(input);
    div2.appendChild(button);

    div.appendChild(div1);
    div.appendChild(div2);

    
    const li = createLi( input , icon )
    
    button.addEventListener('click', function() {
        div.remove();
        addButton.style.display = 'inline-block'; // Réafficher le bouton d'ajout
        li.remove()
    });
    console.log(div)


    return [ div , li ] ;
}

function addElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);

    button.addEventListener('click', function() {
        const  [ newInputDiv , li ] = createInputDiv(button);

        parent1.appendChild(newInputDiv);
        parent2.appendChild(li);

        // Cacher le bouton d'ajout
        button.style.display = 'none';
    });
}

// Exemple d'appel de la fonction
addElement('infoGroup1', 'infoGroup1_', 'phone');
addElement('infoGroup1', 'infoGroup1_', 'mail');
addElement('infoGroup1', 'infoGroup1_', 'linkedin');
addElement('infoGroup1', 'infoGroup1_', 'instagram');
addElement('infoGroup1', 'infoGroup1_', 'facebook');
addElement('infoGroup1', 'infoGroup1_', 'tiktok');
addElement('infoGroup1', 'infoGroup1_', 'github')

autoWritingId('nameIp' , "nameIp_")
autoWritingId("profileIp", "profileIp_")
autoWritingId("descriptionIp" , "descriptionIp_")


function hideElement(elementId, buttonId , isVisible) {
    const element = document.getElementById(elementId);
    const button = document.getElementById(buttonId);

    button.addEventListener('click', function() {
        if (isVisible) {
            element.style.display = 'none';
            button.className = "bx bx-chevron-down"
        } else {
            element.style.display = 'block';
            button.className = "bx bx-chevron-up"

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

    input1.addEventListener('input', function() { h5.innerText = input1.value; });
    input2.addEventListener('input', function() { h4.innerText = input2.value; });
    input3.addEventListener('input', function() { h4_.innerText = input3.value; });
    
    li.appendChild(h5)
    li.appendChild(h4)
    li.appendChild(h4_)


    button.addEventListener('click', function() {
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

    return [ div , li ] ;
}
function addEducationElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("educationHider")

    button.addEventListener('click', function() {
        const  [ newInputDiv , newInputDiv_ ] = createInputDivEducation();

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
    
    input1.addEventListener('input', function() { 
        span1.innerText = input1.value; 
    });
    
    input2.addEventListener('input', function() { 
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


    button.addEventListener('click', function() {
        div.remove(); li.remove() 
    });

    div2_.appendChild(button)

    div.appendChild(div1)
    div.appendChild(div2)

    div.appendChild(div1_)
    div.appendChild(div2_)

    return [ div , li ] ;
}
function addLanguageElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("languagesHider")

    button.addEventListener('click', function() {
        const  [ newInputDiv , newInputDiv_ ] = createInputDivLanguages();

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
    return [div , input ] ;
}

function createInputTextArea() {
    const div = document.createElement('div');
    div.className = 'input-div';
    const input = document.createElement('textarea');
    div.appendChild(input);
    return [div , input ] ;
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
    const [ yearDiv ,  yearInput ] = createInput();

    // Création des éléments pour Description
    const descriptionLab = createLabelDiv("Description");
    const [descriptionDiv ,  descriptionInput] = createInputTextArea();

    // Création des éléments pour Profile
    const profileLab = createLabelDiv("Profile");
    const [ profileDiv , profileInput ]= createInput();

    // Création des éléments pour Firm
    const firmLab = createLabelDiv("Firm");
    const [firmDiv ,  firmInput ]= createInput();

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

    const h4 = document.createElement("h4") ;
    const p = document.createElement("p") ;

    Box.className = "box"
    div1.className = 'year_company'
    div2.className = 'text'
    

    yearInput.addEventListener('input', function() {h5.innerText = yearInput.value; });
    descriptionInput.addEventListener('input', function() {p.innerText = descriptionInput.value; });
    profileInput.addEventListener('input', function() {h4.innerText = profileInput.value; });
    firmInput.addEventListener('input', function() {h5_.innerText = firmInput.value; });


    div1.appendChild(h5)
    div1.appendChild(h5_)
    div2.appendChild(h4)
    div2.appendChild(p)
    Box.appendChild(div1)
    Box.appendChild(div2)

    button.addEventListener('click', function() {
        DIV.remove(); Box.remove() 
    });

    return [ DIV , Box ] ;
}
function addExperiencesElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("experiencesHider")

    button.addEventListener('click', function() {
        const  [ newInputDiv , newInputDiv_ ] = createInputDivExperiences();

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
    
    input1.addEventListener('input', function() { 
        h4.innerText = input1.value; 
    });
    
    div2div.style.width = ' 25%'
    input2.addEventListener('input', function() { 
        // Vérifier si la valeur dépasse 100 et la limiter
        let value = parseInt(input2.value, 10);
        if (value > 100) {
            value = 100;
            input2.value = 100;
        }
        div2div.style.width = value + '%'; 
    });
    

    button.addEventListener('click', function() {
        div.remove(); box.remove() 
    });

    div2_.appendChild(button)

    div.appendChild(div1)
    div.appendChild(div2)

    div.appendChild(div1_)
    div.appendChild(div2_)

    console.log("return")
    return [ div , box ] ;
}

function addSkillsElement(parent1Id, parent2Id, buttonId) {
    const parent1 = document.getElementById(parent1Id);
    const parent2 = document.getElementById(parent2Id);
    const button = document.getElementById(buttonId);
    const hider = document.getElementById("skillsHider")

    button.addEventListener('click', function() {
        const  [ newInputDiv , newInputDiv_ ] = createInputDivSkills();

        parent1.appendChild(newInputDiv);
        parent2.appendChild(newInputDiv_);
        parent1.classList.add('group')
        hider.style.display = 'block'
        // Cacher le bouton d'ajout

    });
}



function createInterest( parentId , buttonId) {
    const parent = document.getElementById(parentId) ;
    const button = document.getElementById(buttonId)


    const li = document.createElement('li');
    const i = document.createElement('i');
    const i2 = document.createElement('i');
    const iconName = button.textContent ; 

    i2.innerHTML = iconName.toUpperCase()
    // Dictionnaire des icônes
    const icons = {
        gaming:'bx bxs-joystick' , 
        travel:"bx bxs-plane-alt", 
        football:"bx bx-football" , 
        book:"bx bx-book", 
        sport:"bx bx-run", 
        bloging:"bx bxl-blogger", 
        coding:'bx bx-code-alt', 
        socialmedial:'bx bxl-tiktok'

    };

    // Ajouter la classe correspondante si l'icône est dans le dictionnaire

    if (icons[buttonId]) {
        i.className = icons[buttonId];
    }    


    li.addEventListener('click', function() {
        li.remove()
    })

    button.addEventListener('click', function() {
        li.appendChild(i)
        li.appendChild(i2)
        parent.appendChild(li)
    } )

}





let isVisibleEducation = true;
let isVisibleLanguages = true;
let isVisibleProfile = false;
let isVisibleExperiences = true;
let isVisibleSkills = true;


hideElement("educationGroup" , "educationHider" , isVisibleEducation)
hideElement("languagesGroup" , "languagesHider" , isVisibleLanguages)
hideElement("profileGroup" , "profileHider",isVisibleProfile)
hideElement("experiencesGroup" , "experiencesHider",isVisibleExperiences)
hideElement("skillsGroup" , "skillsHider",isVisibleExperiences)


addEducationElement("educationGroup" , "educationGroup_" , "educationGroupBtn")
addLanguageElement("languagesGroup" , "languagesGroup_" , "languagesGroupBtn")
addExperiencesElement("experiencesGroup" , "experiencesGroup_" , "experiencesGroupBtn")
addSkillsElement("skillsGroup" , "skillsGroup_" , "skillsGroupBtn")


createInterest("interestGroup_" , "coding")
createInterest("interestGroup_" , "football")
createInterest("interestGroup_" , "gaming")
createInterest("interestGroup_" , "sport")
createInterest("interestGroup_" , "blog")
createInterest("interestGroup_" , "social")
createInterest("interestGroup_" , "travel")



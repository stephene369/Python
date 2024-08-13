document.querySelectorAll('button').forEach(button => {
    if (button.textContent.trim().toLowerCase() === 'add') {
        button.classList.add('add');
    } else if (button.textContent.trim().toLowerCase() === 'remove') {
        button.classList.add('remove');
    }
});

// NAME AND TITLE and Other


const introductionObjects = {
    "name": ".home__title",
    "title": ".home__profession",
    "location": ".location-address",
    "email": ".email-address",
    "phone": ".phone-address",
    "profile-paragraph": ".profile__description"
}

function updateIntroInformation(inputId, insertId) {
    var objectInput = document.getElementById(inputId).value;
    var objectInCv = document.querySelector(insertId);

    if (objectInput) {
        objectInCv.textContent = objectInput;
    }

}

for (const object_ of Object.keys(introductionObjects)) {
    document.getElementById(object_).addEventListener('input', function () {
        updateIntroInformation(object_, introductionObjects[object_]);
    });
}










/*==============================
        SOCIAL INSERTION
=================================*/

const socialIcons = {
    "instagram": "bx bxl-instagram",
    "facebook": "bx bxl-facebook",
    "linkedin": "bx bxl-linkedin-square",
    "twitter": "bx bxl-twitter",
    "youtube": "bx bxl-youtube",
    "blog": "bx bxl-blogger",
    "link": "bx bx-link"
}


const socialContent = document.querySelector(".social-insertion .insertion-content");
const socialSelect = document.getElementById("social-media");
const socialContainer = document.getElementById("social__container")

socialSelect.addEventListener('change', function () {
    const selectedOption = socialSelect.options[socialSelect.selectedIndex];
    const optionText = selectedOption.textContent;
    const optionValue = selectedOption.value;

    // Avoid adding duplicate entries
    if (optionValue === "") return;
    if (document.getElementById(optionValue)) return;

    // Create a new div element 
    const newDiv = document.createElement("div");
    newDiv.classList.add("input-group");
    newDiv.id = optionValue;

    // Create the label element
    const label = document.createElement("label");
    label.setAttribute("for", optionValue);
    label.textContent = `${optionText} :`;

    // Create the input element
    const input = document.createElement("input");
    input.type = "text";
    input.id = optionValue;
    input.placeholder = "https://profile...";


    // Element to insert into CV 
    const newA = document.createElement("a");
    newA.classList.add("social__link");

    const newI = document.createElement('i');
    for (c of socialIcons[optionValue].split(" ")) {
        newI.classList.add(c);
    }

    const newSpan = document.createElement('span');
    newSpan.textContent = optionText

    input.addEventListener('input', function () {
        newA.href = input.value;
    })



    // Create the remove button
    const removeButton = document.createElement("button");
    removeButton.textContent = "Remove";
    removeButton.addEventListener('click', function () {
        socialContent.removeChild(newDiv);
        socialContainer.removeChild(newA);
    });

    // Append label, input, and button to the new div
    newDiv.appendChild(label);
    newDiv.appendChild(input);
    newDiv.appendChild(removeButton);

    // Append the new div to socialContent
    socialContent.appendChild(newDiv);


    // Append element to SocialContainer
    newA.appendChild(newI);
    newA.appendChild(newSpan);
    socialContainer.appendChild(newA);
});








/*==============================
        Education Insertion
=================================*/
const inputEducationContainer = document.getElementById("input-education-container");
const educationContainer = document.getElementById("education-container")
const addEducationButton = document.getElementById("button-education-insertion");



function updateContainer() {
    // Div input group
    const inputGroup = document.createElement("div");
    inputGroup.classList.add("input-group");


    // Input 
    const label = document.createElement("label");
    const titleInput = document.createElement("input");
    const studiesInput = document.createElement("input");
    const dateInput = document.createElement("input");
    label.innerHTML = "Education : "


    /// CV Object 
    // DIV
    const educationContent = document.createElement('div');
    const educationTime = document.createElement('div');
    const educationData = document.createElement('div');

    educationContent.classList.add("education__content");
    educationContent.classList.add("bd-grid");
    educationTime.classList.add("education__time");
    educationData.classList.add("education__data");
    educationData.classList.add("bd-grid")

    // h3 span 
    const title = document.createElement('h3');
    const rounderSpan = document.createElement("span");
    const lineSpan = document.createElement("span");
    const studieSpan = document.createElement('span');
    const yearSpan = document.createElement('span');

    title.classList.add("education__title");
    rounderSpan.classList.add("education__rounder");
    lineSpan.classList.add("education__line");
    studieSpan.classList.add("education__studies");
    yearSpan.classList.add("education__year");


    // EventListiner 
    titleInput.placeholder = "Title";
    titleInput.addEventListener('input', function () {
        title.textContent = titleInput.value;
    })
    studiesInput.placeholder = "school/field";
    studiesInput.addEventListener("input", function () {
        studieSpan.textContent = studiesInput.value;
    })
    dateInput.placeholder = "year-year";
    dateInput.addEventListener('input', function () {
        yearSpan.textContent = dateInput.value;
    })


    // remove button
    const remove = document.createElement("button");
    remove.innerHTML = 'Remove';
    remove.addEventListener('click', function () {
        inputEducationContainer.removeChild(inputGroup);
        educationContainer.removeChild(educationContent);
    })



    //Append Child
    inputGroup.appendChild(label);
    inputGroup.appendChild(titleInput);
    inputGroup.appendChild(studiesInput);
    inputGroup.appendChild(dateInput);
    inputGroup.appendChild(remove);

    educationTime.appendChild(rounderSpan);
    educationTime.appendChild(lineSpan);
    educationData.appendChild(title);
    educationData.appendChild(studieSpan);
    educationData.appendChild(yearSpan);

    educationContent.appendChild(educationTime);
    educationContent.appendChild(educationData);

    inputEducationContainer.appendChild(inputGroup);
    educationContainer.appendChild(educationContent);

}

addEducationButton.addEventListener('click', function () {
    updateContainer();
    //updateLine();
})





/*==============================
        SKILLS
=================================*/
const inputSkillsContainer = document.getElementById("input-skills-container");
const skillsContainer = document.getElementById("skills-container");
const buttonSkillsInsertion = document.getElementById("button-skills-insertion");

buttonSkillsInsertion.addEventListener("click", function () {
    const inputSkillsTitle = document.getElementById("input-skill-title");
    const inputSkillNumber = document.getElementById("input-skills-number");

    // Creating object 
    const inputGroup = document.createElement("div");
    inputGroup.classList.add("input-group");

    const skillLabel = document.createElement("label")

    if (inputSkillNumber.value && inputSkillsTitle.value) {
        skillLabel.textContent = inputSkillsTitle.value + " :";
        inputGroup.appendChild(skillLabel);

        // Skill Container object 
        const newUl = document.createElement("ul");
        const newh3 = document.createElement("span");

        newUl.classList.add("skills__data");
        newUl.appendChild(newh3);
        newh3.textContent = inputSkillsTitle.value;
        const removeButton = document.createElement("button");

        for (let i = 0; i < inputSkillNumber.value; i++) {

            // Input Object 
            const skill = document.createElement("input");


            skill.placeholder = "Skill-" + `${i}`
            removeButton.textContent = "Remove"

            //skill Container Object 
            const newLi = document.createElement("li")
            const circleSpan = document.createElement("span");
            const skillSpan = document.createElement("span");

            newLi.classList.add("skills__name");
            circleSpan.classList.add("skills__circle");

            //Event 
            skill.addEventListener("input", function () {
                skillSpan.textContent = skill.value;
            })


            // Appending Object 
            inputGroup.appendChild(skill);


            newLi.appendChild(circleSpan);
            newLi.appendChild(skillSpan);

            newUl.appendChild(newLi);

        }
        removeButton.addEventListener("click", function () {
            inputSkillsContainer.removeChild(inputGroup);
            skillsContainer.removeChild(newUl);

        })

        inputGroup.appendChild(removeButton);
        inputSkillsContainer.appendChild(inputGroup);
        skillsContainer.appendChild(newUl);
    }


})








/*==============================
        EXPERIENCES
=================================*/

const inputExperiencesContainer = document.getElementById("input-experiences-container");
const experiencesContainer = document.getElementById("experiences-container")
const addExperienceButton = document.getElementById("button-experiences-insertion");


addExperienceButton.addEventListener('click', function () {

    const inputGroup = document.createElement("div");
    inputGroup.classList.add("input-group");


    // Input 
    const label = document.createElement("label");
    const titleInput = document.createElement("input");
    const companyInput = document.createElement("input");
    const descritionInput = document.createElement("textarea");
    label.innerHTML = "Education : "


    /// CV Object 
    // DIV
    const experiencesContent = document.createElement('div');
    const experiencesTime = document.createElement('div');
    const experiencesDescription = document.createElement('div');

    experiencesContent.classList.add("experience__content");
    experiencesContent.classList.add("bd-grid");
    experiencesTime.classList.add("experience__time");
    experiencesDescription.classList.add("experience__data");
    experiencesDescription.classList.add("bd-grid")

    // h3 span 
    const title = document.createElement('h3');
    const rounderSpan = document.createElement("span");
    const lineSpan = document.createElement("span");
    const company = document.createElement('span');
    const description = document.createElement('p');

    title.classList.add("education__title");
    rounderSpan.classList.add("experience__rounder");
    lineSpan.classList.add("experience__line");
    company.classList.add("experience__company");
    description.classList.add("experience__descrition");


    // EventListiner 
    titleInput.placeholder = "Title";
    titleInput.addEventListener('input', function () {
        title.textContent = titleInput.value;
    })
    companyInput.placeholder = "at ...";
    companyInput.addEventListener("input", function () {
        company.textContent = companyInput.value;
    })
    descritionInput.placeholder = "description ... ";
    descritionInput.addEventListener('input', function () {
        description.textContent = descritionInput.value;
    })


    // remove button
    const remove = document.createElement("button");
    remove.innerHTML = 'Remove';
    remove.addEventListener('click', function () {
        inputExperiencesContainer.removeChild(inputGroup);
        experiencesContainer.removeChild(experiencesContent);
    })



    //Append Child
    inputGroup.appendChild(label);
    inputGroup.appendChild(titleInput);
    inputGroup.appendChild(companyInput);
    inputGroup.appendChild(descritionInput);
    inputGroup.appendChild(remove);

    experiencesTime.appendChild(rounderSpan);
    experiencesTime.appendChild(lineSpan);
    experiencesDescription.appendChild(title);
    experiencesDescription.appendChild(company);
    experiencesDescription.appendChild(description);

    experiencesContent.appendChild(experiencesTime);
    experiencesContent.appendChild(experiencesDescription);

    inputExperiencesContainer.appendChild(inputGroup);
    experiencesContainer.appendChild(experiencesContent);

})



/*==============================
        CERTIFICATION
=================================*/
const certificateContainer = document.getElementById("certificate-container");
const inputCertificateContainer = document.getElementById("input-certificate-container")
const buttonAddCertification = document.getElementById("button-add-certificate");

buttonAddCertification.addEventListener('click', function () {

    // input object 
    const label = document.createElement("label")
    const inputGroup = document.createElement("div");

    label.textContent = "Certicate : "
    inputGroup.classList.add("input-group");


    const inputCertificationTitle = document.createElement("input");
    const inputCertificationDescription = document.createElement('input');
    const remove = document.createElement('button');
    inputCertificationTitle.placeholder = "@title ...";
    inputCertificationDescription.placeholder = "@description..."
    remove.textContent = "Remove"

    // CV object 
    const certificateContent = document.createElement("div");
    const title = document.createElement("h3");
    const description = document.createElement("p");

    title.placeholder = "title ... ";
    description.placeholder = "description ...";

    certificateContent.classList.add("certificate__content");
    title.classList.add("certificate__title");
    description.classList.add("certificate__description");


    // Event listiner 
    inputCertificationTitle.addEventListener("input", function () {
        title.textContent = inputCertificationTitle.value
    });
    inputCertificationDescription.addEventListener('input', function () {
        description.textContent = inputCertificationDescription.value
    });
    remove.addEventListener("click", function () {
        inputCertificateContainer.removeChild(inputGroup);
        certificateContainer.removeChild(certificateContent)
    });


    // Add childrend
    inputGroup.appendChild(label);
    inputGroup.appendChild(inputCertificationTitle);
    inputGroup.appendChild(inputCertificationDescription);
    inputGroup.appendChild(remove);

    inputCertificateContainer.appendChild(inputGroup);

    certificateContent.appendChild(title);
    certificateContent.appendChild(description);

    certificateContainer.appendChild(certificateContent);
})







/*==============================
        REFERENCES
=================================*/
const referencesContainer = document.getElementById("references-container");
const inputReferencesContainer = document.getElementById("input-references-container")
const buttonAddReferences = document.getElementById("button-add-references");

buttonAddReferences.addEventListener('click', function () {

    // Input object
    const label = document.createElement("label")
    const inputGroup = document.createElement("div");

    label.textContent = "Reference : "
    inputGroup.classList.add("input-group");

    const remove = document.createElement('button');
    remove.textContent = "Remove"; 

    const inputTitle = document.createElement("input");
    const inputSubtitle = document.createElement("input");
    const inputContact = document.createElement("input");
    const inputContact1 = document.createElement("input");

    inputTitle.placeholder = "@name" ;
    inputSubtitle.placeholder = "@subtitle";
    inputContact.placeholder = "Phone : 00000000";
    inputContact1.placeholder = "Email: eamil.com";


    // CV Object 
    const referenceContent = document.createElement("div");
    const referenceSubtitle = document.createElement("span");
    const referenceTitle = document.createElement("h3");
    const referenceUl = document.createElement("ul");
    const referenceLi = document.createElement("li");
    const referenceLi1 = document.createElement("li");


    //const iconElement = document.createElement('i');


    referenceContent.classList.add("references__content");
    referenceContent.classList.add("bd-grid");
    referenceSubtitle.classList.add("references__subtitle");
    referenceTitle.classList.add("references__title");
    referenceUl.classList.add("references__contact");
    //iconElement.classList.add('bx', 'bx-envelope');

    // Event 
    inputTitle.addEventListener('input' , function(){
        referenceTitle.textContent = inputTitle.value ; 
    }) ; 
    inputSubtitle.addEventListener('input' , function(){
        referenceSubtitle.textContent = inputSubtitle.value;
    }) ; 
    inputContact.addEventListener('input', function(){
        referenceLi.textContent = inputContact.value; 
    } );
    inputContact1.addEventListener('input', function(){
        referenceLi1.textContent = inputContact1.value; 
    } );
    remove.addEventListener('click', function(){
        inputReferencesContainer.removeChild(inputGroup);
        referencesContainer.appendChild(referenceContent);
    })

    // Add Child
    inputGroup.appendChild(inputTitle);
    inputGroup.appendChild(inputSubtitle);
    inputGroup.appendChild(inputContact);
    inputGroup.appendChild(inputContact1);
    inputGroup.appendChild(remove);

    inputReferencesContainer.appendChild(inputGroup)

    //referenceUl.appendChild(iconElement);
    referenceUl.appendChild(referenceLi);
    referenceUl.appendChild(referenceLi1)
    
    referenceContent.appendChild(referenceSubtitle);
    referenceContent.appendChild(referenceTitle);
    referenceContent.appendChild(referenceUl);

    referencesContainer.appendChild(referenceContent);
})




/*==============================
        LANGUAGES
=================================*/
const languagesContainer = document.getElementById("languages-conainer");
const inputLanguagesContainer = document.getElementById("input-languages-container");
const buttonAddLanguages = document.getElementById("button-add-languages");

const languagesContent = document.getElementById("languages-content");

buttonAddLanguages.addEventListener('click', function() {

    // Insertion objects
    const label = document.createElement("label");
    const inputGroup = document.createElement("div");
    const inputLanguage = document.createElement("input");
    inputLanguage.placeholder = "@language";

    label.textContent = "Language : ";
    inputGroup.classList.add("input-group");

    const remove = document.createElement('button');
    remove.textContent = "Remove"; 

    // Cv Object 
    const languageName = document.createElement('li');
    const circleLanguage = document.createElement("span");
    const language = document.createElement('p');

    languageName.classList.add("languages__name");
    circleLanguage.classList.add("languages__circle");

    inputLanguage.addEventListener('input', function() {
        // Update the text content
        language.textContent = inputLanguage.value; 
    });

    remove.addEventListener("click", function() {
        inputLanguagesContainer.removeChild(inputGroup);
        languagesContent.removeChild(languageName);
    });

    // appending 
    inputGroup.appendChild(label);
    inputGroup.appendChild(inputLanguage);
    inputGroup.appendChild(remove);

    languageName.appendChild(circleLanguage);
    languageName.appendChild(language);
    languagesContent.appendChild(languageName);
    inputLanguagesContainer.appendChild(inputGroup);

});







/*==============================
        INTERESTS
=================================*/
const interests = {
    "book": "bx bx-book-content",
    "travel": "bx bxs-plane-alt",
    "music": "bx bxs-music",
    "sports": "bx bx-football",
    "gaming": "bx bx-joystick",
    "art": "bx bx-palette",
    "technology": "bx bx-laptop",
    "cooking": "bx bxs-cookie",
    "photography": "bx bxs-camera",
    "movies": "bx bxs-movie-play",
    "nature": "bx bxs-leaf",
    "writing": "bx bxs-edit-alt",
    "science": "bx bxs-flask",
    "history": "bx bx-bookmark-minus",
    "languages": "bx bx-world"
};

const interestSelect = document.getElementById("interests-select");
const interestContainer = document.getElementById("interests-container");

interestSelect.addEventListener("change", function() {
    // Get selected option
    const selectedOption = interestSelect.options[interestSelect.selectedIndex];
    const optionText = selectedOption.textContent; 
    const optionValue = selectedOption.value;

    if (optionValue === "") return;
    if (document.getElementById(optionValue)) return;

    // Create interest content
    const interestContent = document.createElement('div');
    const interestIcon = document.createElement("i");
    const interestName = document.createElement("span");

    interestContent.classList.add("interests__content");
    interestContent.id = optionValue; // Add id to prevent duplicates
    interestIcon.classList.add("interests__icon");

    for (let c of interests[optionValue].split(" ")) {
        interestIcon.classList.add(c);
    }

    interestName.classList.add("interests__name");
    interestName.textContent = optionText;

    // Append icon and name to content
    interestContent.appendChild(interestIcon);
    interestContent.appendChild(interestName);

    // Add click event to remove the element
    interestContent.addEventListener("click", function() {
        interestContainer.removeChild(interestContent);
    });

    // Append content to container
    interestContainer.appendChild(interestContent);
});


function download(){
    window.print()
}
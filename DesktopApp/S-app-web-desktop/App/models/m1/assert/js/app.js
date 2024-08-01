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


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
        reader.onload = function(e) {
            image.src = e.target.result;
            imageDiv.style.display = 'block'
            cameraButton.style.display = 'none' // Update the image source with the chosen file
        }
        reader.readAsDataURL(file);
    }
});


image.addEventListener("click" , () => {
    imageDiv.style.display = 'none'
    cameraButton.style.display = 'block'
})
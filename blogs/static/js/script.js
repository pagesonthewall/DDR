
const image_input = document.querySelector('#image_input');
const upload_image_button = document.querySelector('.upload_image_button');
var uploaded_image = "";

image_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector('.uploaded-image').style.backgroundImage = `url(${uploaded_image})`;
    });

    reader.readAsDataURL(this.files[0]);
});
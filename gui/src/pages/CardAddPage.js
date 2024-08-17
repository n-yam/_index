export default class CardAddPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `
            <div>CARD ADD PAGE</div>
            
            <div id="frontImagesDiv"></div>
            <input id="frontImageInput" type="file" accept="image/jpeg"><br>
            <textarea id="frontTextarea"></textarea>
            <hr>
            
            <div id="backImagesDiv"></div>
            <input id="backImageInput" type="file" accept="image/jpeg"><br>
            <textarea id="backTextarea"></textarea><br>
            <button id="saveButton">save</button>
        `;
    }

    connectedCallback() {
        const saveButton = this.querySelector("#saveButton");
        const frontImageInput = this.querySelector("#frontImageInput");
        const backImageInput = this.querySelector("#backImageInput");

        saveButton.addEventListener("click", this.handleSave);
        frontImageInput.addEventListener("change", this.handleChange);
        backImageInput.addEventListener("change", this.handleChange);
    }

    handleSave = async event => {
        const frontTextarea = this.querySelector("#frontTextarea");
        const backTextarea = this.querySelector("#backTextarea");

        const frontText = frontTextarea.value;
        const backText = backTextarea.value;

        const formData = new FormData();

        formData.append("frontText", frontText);
        formData.append("backText", backText);

        const frontImages = this.querySelector("#frontImagesDiv").querySelectorAll("img");
        const backImages = this.querySelector("#backImagesDiv").querySelectorAll("img");

        for (let img of frontImages) {
            const base64Image = img.src;
            const response = await fetch(base64Image);
            const blob = await response.blob();
            formData.append("frontImage", blob);
        };

        for (let img of backImages) {
            const base64Image = img.src;
            const response = await fetch(base64Image);
            const blob = await response.blob();
            formData.append("backImage", blob);
        };

        const url = "http://localhost:8000/api/cards";
        const options = {
            method: "POST",
            body: formData,
        }

        fetch(url, options).then(async res => {
            if (res.status == 200) {
                frontTextarea.value = "";
                backTextarea.value = "";
                this.querySelectorAll("input[type='file']").forEach(input => {
                    input.value = "";
                    this.querySelectorAll("img").forEach(img => img.remove());
                });
            }
        });
    }

    handleChange = event => {
        const input = event.target;
        const file = input.files[0];
        const reader = new FileReader();

        const img = document.createElement("img");
        img.onclick = event => {
            if (confirm("Do you want to delete this image?"))
                event.target.remove();
        }

        reader.onload = e => {
            img.src = e.target.result;
            img.style.width = "100%";
        }

        reader.readAsDataURL(file);

        if (input.id == "frontImageInput")
            document.querySelector("#frontImagesDiv").appendChild(img);

        if (input.id == "backImageInput")
            document.querySelector("#backImagesDiv").appendChild(img);

        input.value = "";
    }
}

customElements.define('card-add-page', CardAddPage);
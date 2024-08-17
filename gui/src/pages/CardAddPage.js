export default class CardAddPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `
            <div>CARD ADD PAGE</div>
            
            <div id="frontImagesDiv"></div>
            <button id="addFrontImageButton">add</button><br>
            <textarea id="frontTextarea"></textarea>
            <hr>
            
            <div id="backImagesDiv"></div>
            <button id="addBackImageButton">add</button><br>
            <textarea id="backTextarea"></textarea><br>
            <button id="saveButton">save</button>
        `;
    }

    connectedCallback() {
        const saveButton = this.querySelector("#saveButton");
        const addFrontImageButton = this.querySelector("#addFrontImageButton");
        const addBackImageButton = this.querySelector("#addBackImageButton");

        saveButton.addEventListener("click", this.handleSave);
        addFrontImageButton.addEventListener("click", this.handleAddFrontImage);
        addBackImageButton.addEventListener("click", this.handleAddBackImage);
    }

    handleSave = event => {
        const frontTextarea = this.querySelector("#frontTextarea");
        const backTextarea = this.querySelector("#backTextarea");

        const frontText = frontTextarea.value;
        const backText = backTextarea.value;

        const formData = new FormData();

        formData.append("frontText", frontText);
        formData.append("backText", backText);

        this.querySelectorAll("input[name='frontImage']").forEach(input => {
            formData.append("frontImage", input.files[0]);
        });
        this.querySelectorAll("input[name='backImage']").forEach(input => {
            formData.append("backImage", input.files[0]);
        });

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
                });
            }
        });
    }

    handleAddFrontImage = event => {
        const frontImagesDiv = this.querySelector("#frontImagesDiv");
        const html = "<input type='file' accept='image/jpeg' name='frontImage'><br></br>";
        frontImagesDiv.insertAdjacentHTML("beforeend", html);
    }

    handleAddBackImage = event => {
        const backImagesDiv = this.querySelector("#backImagesDiv");
        const html = "<input type='file' accept='image/jpeg' name='backImage'><br>";
        backImagesDiv.insertAdjacentHTML("beforeend", html);
    }
}

customElements.define('card-add-page', CardAddPage);
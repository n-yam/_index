export default class CardAddPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `
            <div id="frontImagesDiv"></div>
            <input id="frontImageInput" type="file" accept="image/jpeg"><br>
            <textarea id="frontTextarea"></textarea>
            <hr>
            
            <div id="backImagesDiv"></div>
            <input id="backImageInput" type="file" accept="image/jpeg"><br>
            <textarea id="backTextarea"></textarea><br>
            <button id="saveButton">save</button>
            <button id="deleteButton">delete</button>
        `;
    }

    connectedCallback() {
        // Set default values
        const urlParams = new URLSearchParams(window.location.search);
        this.id = urlParams.get("id");
        this.editMode = this.id !== "null";
        console.log(`editMode: ${this.editMode}`);

        const saveButton = this.querySelector("#saveButton");
        const frontImageInput = this.querySelector("#frontImageInput");
        const backImageInput = this.querySelector("#backImageInput");

        saveButton.addEventListener("click", this.handleSave);
        deleteButton.addEventListener("click", this.handleDelete);
        frontImageInput.addEventListener("change", this.handleChange);
        backImageInput.addEventListener("change", this.handleChange);

        if (this.editMode) {
            const url = `http://localhost:8000/api/cards/${this.id}`;

            fetch(url).then(async res => {
                const card = await res.json();

                const frontTextarea = this.querySelector("#frontTextarea");
                const backTextarea = this.querySelector("#backTextarea");

                frontTextarea.value = card.frontText;
                backTextarea.value = card.backText;

                card.frontImages.forEach(frontImage => {
                    const src = `http://localhost:8000/images/${frontImage.uuid}`;
                    const img = document.createElement("img");

                    img.src = src;
                    img.style.width = "100%";
                    img.onclick = event => {
                        if (confirm("Do you want to delete this image?"))
                            event.target.remove();
                    }

                    const frontImagesDiv = this.querySelector("#frontImagesDiv");
                    frontImagesDiv.appendChild(img);
                });

                card.backImages.forEach(backImage => {
                    const src = `http://localhost:8000/images/${backImage.uuid}`;
                    const img = document.createElement("img");

                    img.src = src;
                    img.style.width = "100%";
                    img.onclick = event => {
                        if (confirm("Do you want to delete this image?"))
                            event.target.remove();
                    }

                    const backImagesDiv = this.querySelector("#backImagesDiv");
                    backImagesDiv.appendChild(img);
                });
            });
        }
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

        let url;
        let options;

        if (this.editMode) {
            url = `http://localhost:8000/api/cards/${this.id}`;
            options = {
                method: "PUT",
                body: formData,
            }
        } else {
            url = `http://localhost:8000/api/cards`;
            options = {
                method: "POST",
                body: formData,
            }
        }

        fetch(url, options).then(async res => {
            if (res.status == 200) {
                if (this.editMode) {
                    const href = `/cards/detail?id=${this.id}`;
                    const event = new CustomEvent("updateView", { detail: href });
                    window.dispatchEvent(event);
                } else {
                    frontTextarea.value = "";
                    backTextarea.value = "";
                    this.querySelectorAll("input[type='file']").forEach(input => {
                        input.value = "";
                        this.querySelectorAll("img").forEach(img => img.remove());
                    });
                }
            }
        });
    }

    handleDelete = async event => {
        if (confirm("Do you want to delete this card?")) {
            const url = `http://localhost:8000/api/cards/${this.id}`;
            const options = {
                method: "DELETE"
            };
            fetch(url, options).then(async res => {
                if (res.status == 200) {
                    const href = "/cards/list";
                    const event = new CustomEvent("updateView", { detail: href });
                    window.dispatchEvent(event);
                }
            });
        }
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
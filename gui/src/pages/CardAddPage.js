export default class CardAddPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `
            <div>CARD ADD PAGE</div>
            <input type="file" accept="image/jpeg"><br>
            <textarea id="frontTextarea"></textarea>
            <hr>
            <input type="file" accept="image/jpeg"><br>
            <textarea id="backTextarea"></textarea><br>
            <button id="saveButton">save</button>
        `;
    }

    connectedCallback() {
        const saveButton = this.querySelector("#saveButton");

        saveButton.addEventListener("click", this.handleSave);
    }

    handleSave = event => {
        const frontTextarea = this.querySelector("#frontTextarea");
        const backTextarea = this.querySelector("#backTextarea");

        const frontText = frontTextarea.value;
        const backText = backTextarea.value;

        const formData = new FormData();
        formData.append("frontText", frontText);
        formData.append("backText", backText);

        const url = "http://localhost:8000/api/cards";
        const options = {
            method: "POST",
            body: formData,
        }

        fetch(url, options).then(async res => {
            if (res.status == 200) {
                frontTextarea.value = "";
                backTextarea.value = "";
            }
        });
    }
}

customElements.define('card-add-page', CardAddPage);
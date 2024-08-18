import SpaAnchor from "../components/SpaAnchor";

export default class QuestionPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `
            <div id="countDiv"></div>
            <div id="questionDiv">
                <div id="frontside"></div>
                <hr>

                <button id="viewAnswerButton">VIEW ANSWER</button>
                <div id="backside" style="display: none"></div>
                <hr>

                <button id="okButton">OK</button>
                <button id="ngButton">NG</button>
                <hr>

                <div id="detailDiv"></div>
            </div>
        `;
    }

    async connectedCallback() {
        this.count();
        const card = await this.fetch_first_question();
        this.render(card);

        if (!card) return;

        const viewAnswerButton = this.querySelector("#viewAnswerButton");
        viewAnswerButton.onclick = event => {
            const backside = this.querySelector("#backside");
            backside.style.display = "block";
        };

        const okButton = this.querySelector("#okButton");
        okButton.onclick = event => {
            const url = `${API_SERVER}/api/questions/first?answer=1`;
            const options = {
                method: "POST"
            };
            fetch(url, options).then(async res => {
                if (res.status == 200) {
                    this.count();
                    const card = await this.fetch_first_question();
                    this.render(card);
                }
            })
        };

        const ngButton = this.querySelector("#ngButton");
        ngButton.onclick = event => {
            const url = `${API_SERVER}/api/questions/first?answer=0`;
            const options = {
                method: "POST"
            };
            fetch(url, options).then(async res => {
                if (res.status == 200) {
                    this.count();
                    const card = await this.fetch_first_question();
                    this.render(card);
                }
            })
        };
    }

    count() {
        const url = `${API_SERVER}/api/questions/count`;
        fetch(url).then(async res => {
            const count = await res.json();
            const countDiv = this.querySelector("#countDiv");
            countDiv.innerHTML = `
                <p>count: ${count.done}/${count.todo} (fresh: ${count.fresh})</p>
            `;
        });
    }

    render(card) {
        if (!card) {
            const questionDiv = this.querySelector("#questionDiv");
            questionDiv.innerHTML = "WELL DONE!";
            return;
        }

        const frontside = this.querySelector("#frontside");
        frontside.innerHTML = `
            ${card.frontImages.map(image => `<img src="/static/images/${image.uuid}.jpg"/>`).join("")}
            <p>${card.frontText}</p>
        `;

        const backside = this.querySelector("#backside");
        backside.style.display = "none";
        backside.innerHTML = `
            ${card.backImages.map(image => `<img src="/static/images/${image.uuid}.jpg"/>`).join("")}
            <p>${card.backText}</p>
        `;

        const detailDiv = this.querySelector("#detailDiv");
        detailDiv.innerHTML = `
            <p>id: ${card.id}</p>
            <p>level: ${card.level}</p>
            <p>next: ${card.next}</p>
            <p>created: ${card.created}</p>
            <p>updated: ${card.updated}</p>
            <p>fresh: ${card.fresh}</p>
            <p>todo: ${card.todo}</p>
            <p>done: ${card.done}</p>
            <spa-anchor href="/cards/update?id=${card.id}">edit</spa-anchor>
        `;
    }

    async fetch_first_question() {
        const url = `${API_SERVER}/api/questions/first`;
        const response = await fetch(url);

        if (response.status == 200) {
            const card = await response.json();
            return card;
        } else {
            return null;
        }
    }
}

customElements.define('question-page', QuestionPage);
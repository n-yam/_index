import SpaAnchor from "../components/SpaAnchor";

export default class CardDetailPage extends HTMLElement {

    constructor() {
        super()
    }

    connectedCallback() {
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get("id");

        const url = `http://localhost:8000/api/cards/${id}`;

        fetch(url).then(async res => {
            const card = await res.json();
            const html = `
                ${card.frontImages.map(image => `<img src="/images/${image.uuid}" width="100%"/>`).join("")}
                <p>frontText: ${card.frontText}</p>
                <hr>

                ${card.backImages.map(image => `<img src="/images/${image.uuid}" width="100%"/>`).join("")}
                <p>backText: ${card.backText}</p>
                <hr>
                
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
            this.insertAdjacentHTML("beforeend", html);
        });
    }
}

customElements.define('card-detail-page', CardDetailPage);
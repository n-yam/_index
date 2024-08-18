import SpaAnchor from "../components/SpaAnchor";

export default class CardListPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `
            <table id="cardTable">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>frontText</th>
                        <th>backText</th>
                        <th>level</th>
                        <th>next</th>
                    </tr>
                </thead>
            </table>
        `;
    }

    connectedCallback() {
        const url = `${API_SERVER}/api/cards`;
        fetch(url).then(async res => {

            const json = await res.json();

            for (let card of json) {
                const cardTable = this.querySelector("#cardTable");

                const row = cardTable.insertRow(-1);

                const id = row.insertCell(0);
                const frontText = row.insertCell(1);
                const backText = row.insertCell(2);
                const level = row.insertCell(3);
                const next = row.insertCell(4);

                id.innerHTML = `<spa-anchor href="/cards/detail?id=${card.id}">${card.id}</spa-anchor>`;
                frontText.innerHTML = card.frontText.substring(0, 10);
                backText.innerHTML = card.backText.substring(0, 10);
                level.innerHTML = card.level;
                next.innerHTML = card.next;
            }
        });
    }
}

customElements.define('card-list-page', CardListPage);
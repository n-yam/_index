export default class SpaAnchor extends HTMLElement {

    constructor() {
        super()
        if (!this.hasAttribute('href')) {
            throw new Error("Attribute 'href' is required.");
        }
    }

    connectedCallback() {
        const shadow = this.attachShadow({ mode: "open" });

        shadow.innerHTML = `
            <style>
                span {
                    cursor: pointer;
                    color: green;
                }
            </style>
            <span><slot></slot></span>
        `

        this.addEventListener("click", this.handleClick);
    }

    handleClick(event) {
        event.preventDefault();

        const href = this.getAttribute("href")
        const updateViewEvent = new CustomEvent("updateView", { detail: href });
        window.dispatchEvent(updateViewEvent);
        console.log(`update view: href`);
    }
}

customElements.define('spa-anchor', SpaAnchor);
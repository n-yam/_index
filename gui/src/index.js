function component() {
    const element = document.createElement('div');
    element.innerHTML = "HELLO WORLD";

    return element;
}

document.body.appendChild(component());
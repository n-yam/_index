function component() {
    const element = document.createElement('div');
    element.innerHTML = "HELLO WORLD";

    return element;
}

document.body.appendChild(component());

document.querySelectorAll("a").forEach(a => {
    a.onclick = event => {
        event.preventDefault();
        window.history.pushState(null, "", a.href);
    };
});

const updateView = () => {
    const pages = {
        "/": `
        <h1>TOP</h1>
      `,
        "/hello": `
        <h1>HELLO</h1>
      `,
        "/profile": `
        <h1>PROFILE</h1>
      `
    };
    const page = pages[window.location.pathname];
    const render = page || `<h1>404:Not Found<h1>`;
    document.getElementById("app").innerHTML = render;
};

document.querySelectorAll("a").forEach(a => {
    a.onclick = event => {
        event.preventDefault();
        window.history.pushState(null, "", a.href);
        updateView();
    };
});

// 初期表示時の処理
updateView();

// ブラウザバック時の処理
window.addEventListener("popstate", () => {
    updateView();
});
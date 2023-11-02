let btn = document.createElement("button");
btn.innerHTML = "Click me!";
btn.id = "item";
btn.disabled = true;
btn.addEventListener("click", () => {
    const a = "Console-ations-and-congrats-";
    const b = "56428a8e-178d-4348-b6c5-5737bd44d360"
    alert("aetherius{" + a + b + "}");
});
document.body.appendChild(btn);
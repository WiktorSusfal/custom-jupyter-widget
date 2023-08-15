export function render({ model, el }) {
    let main_div = document.createElement('div');
    main_div.classList.add('custom-widget');
    
    let text_1 = document.createElement('input');
    text_1.classList.add('custom-input');
    text_1.disabled = true;
    text_1.value = String(model.get("text_1"));
    
    let text_2 = document.createElement('input');
    text_2.classList.add('custom-input');
    text_2.disabled = true
    text_2.value = String(model.get("text_2"));

    model.on("change:text_1", () => {
            text_1.value = String(model.get("text_1"));
        });

    model.on("change:text_2", () => {
            text_2.value = String(model.get("text_2"));
        });

    main_div.appendChild(text_1);
    main_div.appendChild(text_2);
    el.appendChild(main_div);
}
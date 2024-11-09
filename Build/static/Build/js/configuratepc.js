document.addEventListener("DOMContentLoaded", function() {
    const formFields = document.querySelectorAll(".form-group select");

    formFields.forEach(field => {
        field.addEventListener("change", function() {
            // Получаем id выбранного компонента
            const selectedComponentId = field.value;

            // Скрываем все блоки информации
            document.querySelectorAll(".component-info").forEach(info => info.style.display = "none");

            // Отображаем блок с информацией, если поле выбрано
            if (selectedComponentId) {
                const infoBlock = document.getElementById(`${field.name}-info`);
                if (infoBlock) {
                    infoBlock.style.display = "block";
                }
            }
        });
    });
});
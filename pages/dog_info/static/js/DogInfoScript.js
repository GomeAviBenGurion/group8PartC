document.addEventListener("DOMContentLoaded", () => {
    window.showLargeImage = function (imageElement) {
        console.log("showLargeImage called with:", imageElement); // Debug log
        const overlay = document.createElement('div');
        overlay.style.position = 'fixed';
        overlay.style.top = '0';
        overlay.style.left = '0';
        overlay.style.width = '100vw';
        overlay.style.height = '100vh';
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
        overlay.style.display = 'flex';
        overlay.style.alignItems = 'center';
        overlay.style.justifyContent = 'center';
        overlay.style.zIndex = '1000';

        const img = document.createElement('img');
        img.src = imageElement.src;
        console.log("Image source:", img.src); // Debug log
        img.style.maxWidth = '90vw';
        img.style.maxHeight = '90vh';
        img.style.borderRadius = '15px';

        const closeButton = document.createElement('button');
        closeButton.textContent = '×';
        closeButton.style.position = 'absolute';
        closeButton.style.top = '50px';
        closeButton.style.right = '50px';
        closeButton.style.backgroundColor = '#fff';
        closeButton.style.color = '#333';
        closeButton.style.border = 'none';
        closeButton.style.padding = '10px 17px';
        closeButton.style.fontSize = '24px';
        closeButton.style.borderRadius = '50%';
        closeButton.style.cursor = 'pointer';
        closeButton.onclick = () => {
            console.log("Close button clicked"); // Debug log
            document.body.removeChild(overlay);
        };

        overlay.appendChild(img);
        overlay.appendChild(closeButton);
        document.body.appendChild(overlay);
    };
});


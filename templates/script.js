document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('image-upload');
    const originalImage = document.getElementById('original-image');
    const originalImageCompare = document.getElementById('original-image-compare');
    const enhancedImageCompare = document.getElementById('enhanced-image-compare');
    const optionsSection = document.getElementById('options-section');
    const imagePreviewSection = document.getElementById('image-preview');
    const enhancedSection = document.getElementById('enhanced-section');
    const downloadButton = document.getElementById('download-button');
    const buttons = document.querySelectorAll('.enhance-button');
    const slider = document.getElementById('slider');
    const enhancedWrapper = document.getElementById('enhanced-wrapper');
    const compareContainer = document.getElementById('compare-container');

    window.previewImage = function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const imgSrc = e.target.result;
                originalImage.src = imgSrc;
                originalImageCompare.src = imgSrc;
                imagePreviewSection.classList.remove('hidden');
                optionsSection.classList.remove('hidden');

                originalImage.onload = function() {
                    compareContainer.style.height = `${originalImage.height}px`;
                };
            };
            reader.readAsDataURL(file);
        }
    };

    buttons.forEach(button => {
        button.addEventListener('click', async () => {
            const enhancementType = button.getAttribute('data-type');
            await enhanceImage(enhancementType);
        });
    });

    async function enhanceImage(type) {
        const file = fileInput.files[0];
        if (!file) {
            alert('Please upload an image first.');
            return;
        }

        const formData = new FormData();
        formData.append('image', file);

        const apiUrl = `http://127.0.0.1:5000/enhance_image_${type}`;

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const data = await response.json();
                enhancedImageCompare.src = `data:image/png;base64,${data.enhanced_image}`;
                enhancedSection.classList.remove('hidden');
                downloadButton.classList.remove('hidden');
                enableSlider();
            } else {
                const errorData = await response.json();
                alert(`Error: ${errorData.error}`);
            }
        } catch (error) {
            alert(`An error occurred: ${error.message}`);
        }
    }

    downloadButton.addEventListener('click', () => {
        const enhancedImageUrl = enhancedImageCompare.src;
        const link = document.createElement('a');
        link.href = enhancedImageUrl;
        link.download = 'enhanced_image.png';
        link.click();
    });

    function enableSlider() {
        let isDragging = false;
        slider.addEventListener('mousedown', () => { isDragging = true; });
        document.addEventListener('mouseup', () => { isDragging = false; });
        document.addEventListener('mousemove', (event) => {
            if (isDragging) {
                const rect = compareContainer.getBoundingClientRect();
                let offsetX = event.clientX - rect.left;
                offsetX = Math.max(0, Math.min(offsetX, rect.width));
                slider.style.left = `${offsetX}px`;
                enhancedWrapper.style.width = `${offsetX}px`;
            }
        });
    }
});

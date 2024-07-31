import { isImageFile } from "/static/js/admin-scripts/image_validator.mjs";

function selectInputImageHandler() {
  const items = document.querySelectorAll(".item");

  items.forEach((item) => {
    const displayImageContainer = item.querySelectorAll(".image-container");

    displayImageContainer.forEach((container) => {
      const displayImage = container.querySelector(".display-image");
      const input = container.querySelector("input[type=file]");
  
      displayImage.addEventListener("click", () => {
        input.click();
  
        input.addEventListener("change", () => {
          const file = input.files[0];
          const fileName = file.name;
  
          if (file && isImageFile(fileName)) {
            const blobUrl = URL.createObjectURL(file);
            displayImage.src = blobUrl;
          }
        });
      });
    });
  });
}

selectInputImageHandler();
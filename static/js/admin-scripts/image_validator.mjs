const imageExtensions = [
    '.jpeg', '.jpg',
    '.png',
    '.tiff', '.tif',
    '.bmp',
    '.webp',
    '.psd',
    '.ico',
    '.heic', '.heif'
];


// Function to check if a file's extension is in the imageExtensions array
export function isImageFile(filename) {
    // Get the file extension (assuming filename is a string like 'filename.jpg')
    const extension = '.' + filename.split('.').pop().toLowerCase();
    
    // Check if the extension is in the imageExtensions array
    return imageExtensions.includes(extension);
}

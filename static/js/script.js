
/**
 * This function retrieves the current date and updates the HTML elements with the class "date-today" 
 * to display the date in the format "YYYY Month, DD".
 *
 * @returns {void} This function does not return any value.
 */
function getDate() {
    const currentDate = new Date();
    const monthNames = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"];
    
    items = document.querySelectorAll(".date-today");
    
    items.forEach(item => {
        const formattedDate = currentDate.getFullYear() + " " + monthNames[currentDate.getMonth()] + ", " + currentDate.getDate();
        item.innerHTML = formattedDate;
    });
}

getDate();
const words = [
  "Computer Engineer ",
  "Frontend Web Developer ",
  "Aspiring Data Scientist ",
  "Data Analyst ",
  "Software Engineer"
];

let i = 0;
let j = 0;
let currentWord = "";
let isDeleting = false;
const typedElement = document.getElementById("typed");

function type() {
    if (i >= words.length) i = 0; // loop words
    const fullWord = words[i];

    if (isDeleting) {
        currentWord = fullWord.substring(0, j--);
    } else {
        currentWord = fullWord.substring(0, j++);
    }

    typedElement.textContent = currentWord;

    if (!isDeleting && j === fullWord.length) {
        isDeleting = true;
        setTimeout(type, 1000); // wait before deleting
    } else if (isDeleting && j === 0) {
        isDeleting = false;
        i++;
        setTimeout(type, 500);
    } else {
        setTimeout(type, isDeleting ? 50 : 150); // typing speed
    }
}

type();

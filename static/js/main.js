// Search Bar START
function search() {
    const input = document.getElementById("search-input");
    const query = input.value;

    // Perform any necessary actions with the query, such as sending it to a Django backend

    input.value = ""; // Clear the input field after searching
}

const placeholderTexts = ["Projects...", "Blogs...", "Anything...", "Content...", "Documentation..."];

function animatePlaceholder() {
    const input = document.getElementById("search-input");
    let currentIndex = 0;

    setInterval(() => {
        input.placeholder = `Search ${placeholderTexts[currentIndex]}`;
        currentIndex = (currentIndex + 1) % placeholderTexts.length;
    }, 2000);
}

animatePlaceholder();

// Search Bar END


// Welcome Screen Animation START
// A list of code snippets in different languages
let snippets = [
    "<div class=\"container\">",
    "public class HelloWorld {",
    "int x = y;",
    "def add(a, b):",
    "#include <iostream>",
    ".box { width: 100vw; }",
    "console.log('Hello, world!');",
    "using System;",
    "return a + b;",
    "</div>",
    "public static void Main() {",
    "float f = sin(3.14);",
    "print(add(2,3))",
    "using namespace std;",
    "display: flex;",
    "document.getElementById('logo');",
    "};",
    "};",
    "align-items: center;",
    "let name = prompt('your name?');",
    "Console.WriteLine(Hello, world!);",
    "for (int i =0; i < n;",
    "if (x > y) {",
    "import math",
    "#define PI3.14",
    "justify-content:center;",
    "alert('Hello, ' + name);",
    "public class HelloWorld { }",
    "int x = 5 * y;",
    "def multiply(a, b):",
    ".box { width: 100vw; }",
    "console.log('Hello, world!');",
    ".box { width: calc(100vw;",
    "console.log('Welcome to my",
    "using System; ",
    "class Program",
    "return a + b;",
    "public static void Main()",
    "float f = Math.sin(3.14);",
    "print(add(2, 3));",
    "using namespace std;int main()",
    "display: flex; width: calc(100vw;",
    "document.getElementById('logo');",
    "int x = 5;",
    "int x = 10;",
    "align-items: center;",
    "width: calc(100vw;",
    "let name = prompt('What",
];


// A list of colors for different languages
let colors = ["#e34c26", // HTML
    "#b07219", // Java
    "#f34b7d", // C
    "#3572A5", // Python
    "#f1e05a", // C++
    "#563d7c", // CSS
    "#f1e05a", // JavaScript
    "#178600", // C#
    "#3d9970", // C++

    // Additional colors
    "#ff6b6b", // HTML
    "#9b5de5", // Java
    "#f6ad55", // C
    "#48bb78", // Python
    "#f9c74f", // C++
    "#f56565", // CSS
    "#4299e1", // JavaScript
    "#38a169", // C#
    "#4fd1c5", // C++
];

// A function to create a random snippet element
function createSnippet() {
    // Create a div element with the snippet class
    let snippet = document.createElement("div");
    snippet.className = "snippet";

    // Pick a random snippet from the list and set its text content
    let index = Math.floor(Math.random() * snippets.length);
    snippet.textContent = snippets[index];

    // Pick a random color from the list and set its style
    let color = colors[Math.floor(Math.random() * colors.length)];
    snippet.style.color = color;

    // Return the snippet element
    return snippet;
}

// A function to animate a snippet element within the welcome screen section
function animateSnippet(snippet) {
    // Get the welcome screen section element and its dimensions
    let welcomeScreen = document.querySelector('.welcome-screen');
    let welcomeScreenWidth = welcomeScreen.offsetWidth;
    let welcomeScreenHeight = welcomeScreen.offsetHeight;

    // Get the angle and radius of the snippet's position within the welcome screen section
    let angle = Math.random() * Math.PI * 2; // Random angle between 0 and 2π
    let radius = Math.min(welcomeScreenWidth, welcomeScreenHeight) / 2 - snippet.offsetWidth; // Random radius within the welcome screen section

    // Calculate the x and y coordinates of the snippet's position within the welcome screen section
    let x = welcomeScreenWidth / 2 + radius * Math.cos(angle);
    let y = welcomeScreenHeight / 2 + radius * Math.sin(angle);

    // Set the snippet's position within the welcome screen section
    snippet.style.position = 'absolute';
    snippet.style.left = x + 'px';
    snippet.style.top = y + 'px';

    // Append the snippet to the welcome screen section element
    welcomeScreen.appendChild(snippet);

    // Set a random duration for the animation between one and three seconds
    let duration = Math.random() * 2000 + 1000;

    // Set a random direction for the animation (inward or outward)
    let direction = Math.random() < 0.5 ? -1 : 1;

    // Set the animation keyframes
    let keyframes = [
        {transform: 'scale(1)', opacity: 1, offset: 0},
        {transform: 'scale(2)', opacity: 0, offset: 1},
    ];

    // Set the animation options
    let options = {
        duration: duration,
        iterations: 1,
        easing: 'ease-out',
    };

    // Create the animation object
    let animation = snippet.animate(keyframes, options);

    // When the animation ends, remove the snippet element
    animation.onfinish = function () {
        welcomeScreen.removeChild(snippet);
    };
}

// A function to create and animate a new snippet every 100 milliseconds
function generateSnippets() {
    setInterval(function () {
        let snippet = createSnippet();
        animateSnippet(snippet);
    }, 100);
}

// Call the generateSnippets function when the page loads
window.onload = generateSnippets;

// Welcome Screen Animation END


// Navigation Bar START
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

// Navigation Bar END

// Comments & Reviews START

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    var reviews = document.querySelectorAll(".review-card"); // Select all review cards
    var currentReview = 0; // Index of the currently displayed review

    // Function to show a specific review
    function showReview(index) {
        // Hide all reviews
        for (var i = 0; i < reviews.length; i++) {
            reviews[i].style.display = "none";
        }

        // Show the review at the specified index
        reviews[index].style.display = "grid";
    }

    // Function to show the next review
    function showNextReview() {
        currentReview++;
        if (currentReview >= reviews.length) {
            currentReview = 0; // Start from the beginning if the last review is reached
        }
        showReview(currentReview);
    }

    // Function to show the previous review
    function showPreviousReview() {
        currentReview--;
        if (currentReview < 0) {
            currentReview = reviews.length - 1; // Go to the last review if the first review is reached
        }
        showReview(currentReview);
    }

    // Show the initial review
    showReview(currentReview);

    // Set an interval to automatically show the next review every 5 seconds
    setInterval(showNextReview, 5000);

    // Add event listeners to the navigation buttons
    var previousButton = document.querySelector(".chevron.left");
    var nextButton = document.querySelector(".chevron.right");

    previousButton.addEventListener("click", showPreviousReview);
    nextButton.addEventListener("click", showNextReview);
});
// Comments & Reviews END

// Milestones Table START
const table = document.getElementById('milestones-table');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const rowsPerPage = 6;
let currentPage = 1;

function showPage(pageNumber) {
    const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    const startIndex = (pageNumber - 1) * rowsPerPage;
    const endIndex = startIndex + rowsPerPage;

    for (let i = 0; i < rows.length; i++) {
        if (i >= startIndex && i < endIndex) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
    }
}

function updatePaginationButtons() {
    const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    const totalPages = Math.ceil(rows.length / rowsPerPage);

    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = currentPage === totalPages || totalPages === 0;
}

prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        showPage(currentPage);
        updatePaginationButtons();
    }
});

nextBtn.addEventListener('click', () => {
    const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    const totalPages = Math.ceil(rows.length / rowsPerPage);

    if (currentPage < totalPages) {
        currentPage++;
        showPage(currentPage);
        updatePaginationButtons();
    }
});

showPage(currentPage);
updatePaginationButtons();

// Milestones Table END


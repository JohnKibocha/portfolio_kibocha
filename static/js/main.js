// Search Bar START
function search() {
    const input = document.getElementById("search-input");
    const query = input.value;

    // Perform any necessary actions with the query, such as sending it to a Django backend

    input.value = ""; // Clear the input field after searching
}

const placeholderTexts = ["Projects", "Blogs", "Anything", "Content", "Documentation"];

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
    "int x = y + z;",
    "def add(a, b):",
    "#include <iostream>",
    ".box {",
    "console.log('Hello, world!');",
    "using System;",
    "return a + b;",
    "}",
    "</div>",
    "public static void Main() {",
    "float f = sin(3.14);",
    "print(add(2,3))",
    "using namespace std;",
    "display: flex;",
    "document.getElementById('logo').style.color = 'red';",
    "};",
    "};",
    "align-items: center;",
    "let name = prompt('What is your name?');",
    "Console.WriteLine(Hello, world!);",
    "for (int i =0; i < n; i++) {",
    "if (x > y) {",
    "import math",
    "#define PI3.14",
    "justify-content:center;",
    "alert('Hello, ' + name);",
    "public class HelloWorld { }",
    "int x = 5 * y;",
    "def multiply(a, b):  return a * b",
    ".box { width: 100vw; }",
    "console.log('Hello, world!');",

    ".box { width: calc(100vw - 400px); }",
    "console.log('Welcome to my website!');",
    "using System; class Program { static void Main() {  Console.WriteLine(Hello, world!);    }}",
    "return a + b;",
    "public static void Main() { }",
    "float f = Math.sin(3.14);",
    "print(add(2, 3));",
    "using namespace std;int main() {    return 0;}",
    "display: flex; width: calc(100vw - 400px);",
    "document.getElementById('logo').style.color = 'red';",
    "int x = 5;",
    "int x = 10;",
    "align-items: center; width: calc(100vw - 400px);",
    "let name = prompt('What is your name?');alert('Hello, ' + name);",
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
    { transform: 'scale(1)', opacity: 1, offset: 0 },
    { transform: 'scale(2)', opacity: 0, offset: 1 },
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

// Rest of the code...

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
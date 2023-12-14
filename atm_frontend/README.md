# Frontend Module for Agile Task Manager (ATM)

## Overview

This document provides an overview of the frontend module for the Agile Task Manager (ATM). Our frontend architecture is designed to be modular, scalable, and easy to maintain, using a combination of traditional web technologies and modern JavaScript practices.

## Architecture

The frontend is structured as a Single Page Application (SPA) without relying on modern frameworks like React or Vue. Instead, we use vanilla JavaScript and AJAX for dynamic content loading, coupled with external JavaScript modules for page-specific functionality.

### Key Components

- **HTML Pages**: Stored in the `/pages` directory, these are individual HTML files representing different views of the application (e.g., `home.html`, `login.html`).

- **JavaScript Modules**: Each HTML page has a corresponding JavaScript module in `/js/` that contains page-specific scripts.

- **CSS**: Global styles are defined in a central stylesheet (`global.css`), ensuring a consistent look and feel across the application.

- **Main JavaScript (`main.js`)**: This is the core script of our application, handling dynamic content loading and client-side routing.

### Dynamic Content Loading

The `main.js` script uses `XMLHttpRequest` to asynchronously fetch HTML content and inject it into the main layout (`index.html`). This approach allows us to load new content without a full page refresh, enhancing the user experience and reducing server load.

### Client-Side Routing

We use the HTML5 History API for client-side routing. This allows us to update the browser's address bar and navigate between pages without reloading the entire page.

### Modular JavaScript

Each page in our application has a corresponding JavaScript module. When a page is loaded, its module is dynamically imported and executed. This modular structure helps in isolating page-specific functionalities and promotes easier maintenance and scalability.

## Technologies

This section outlines the key technologies used in the development of the ATM frontend module:

- **HTML**: The foundation of our web pages. Each view of the application is an individual HTML file, ensuring simplicity and clarity.

- **CSS**: Used for styling the web pages. A global stylesheet (`global.css`) provides consistent styling across the application.

- **JavaScript (Vanilla)**: The core programming language used for dynamic behavior on the client side. Vanilla JavaScript is used for its simplicity and direct control over the DOM and browser APIs.

- **AJAX (Asynchronous JavaScript and XML)**: Utilized for loading new content asynchronously without the need for a page reload. This enhances user experience by providing a smoother interaction with the application.

- **HTML5 History API**: Enables client-side routing, allowing the browser's URL to be updated dynamically without refreshing the page, thereby supporting our SPA approach.

- **jQuery**: A fast, small, and feature-rich JavaScript library. It's used to simplify event handling, HTML document traversing, animating, and Ajax interactions.

- **Modular JavaScript**: ES6 modules are used for separating page-specific functionalities into individual files, promoting better organization and maintainability.

- **XMLHttpRequest**: This object is used to interact with servers. It's employed in our application to retrieve data from a URL without having to do a full page refresh.

These technologies were chosen for their reliability, ease of use, and wide support, ensuring that our application is robust, maintainable, and easily scalable.

## Why This Architecture?

1. **Simplicity**: Without the overhead of large frameworks, the application remains lightweight and easy to understand.

2. **Modularity**: Each page's functionality is encapsulated in its own module, making the codebase more organized and easier to manage.

3. **Scalability**: New pages and functionalities can be added with minimal impact on the existing codebase.

4. **Performance**: Reduced server load and faster interactions due to AJAX and client-side rendering.

5. **Customizability**: Without the constraints of a framework, we have complete control over the application's behavior and structure.

## Getting Started

To get started with the frontend module:

1. Clone the repository.
2. Navigate to the project directory.
3. Open `index.html` in a web browser to view the application.

## Contributing

Contributions to the frontend module are welcome. Please ensure that any new pages follow the existing structure with separate HTML and JavaScript files.

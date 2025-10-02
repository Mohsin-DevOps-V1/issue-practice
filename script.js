const toggleBtn = document.querySelector('.toggle-btn');
const body = document.body;

// Function to set the theme
function setTheme(isDark) {
    if (isDark) {
        body.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.remove('dark-mode');
        localStorage.setItem('theme', 'light');
    }
}

// Check for a saved theme preference on page load
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    setTheme(true);
} else {
    setTheme(false);
}

// Add event listener for the toggle button
toggleBtn.addEventListener('click', () => {
    // Determine the new theme and set it
    const currentThemeIsDark = body.classList.contains('dark-mode');
    setTheme(!currentThemeIsDark);
});


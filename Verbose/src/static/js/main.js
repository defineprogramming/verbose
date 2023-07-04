// Verbose main.js

document.addEventListener('DOMContentLoaded', (event) => {
    // DOM Elements
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const tweetForm = document.getElementById('tweet-form');
    const profileForm = document.getElementById('profile-form');
    const notificationForm = document.getElementById('notification-form');

    // Event Listeners
    if (loginForm) loginForm.addEventListener('submit', submitForm);
    if (registerForm) registerForm.addEventListener('submit', submitForm);
    if (tweetForm) tweetForm.addEventListener('submit', postTweet);
    if (profileForm) profileForm.addEventListener('submit', updateProfile);
    if (notificationForm) notificationForm.addEventListener('submit', receiveNotification);

    // Functions
    function submitForm(e) {
        e.preventDefault();
        const message = document.createElement('p');
        message.textContent = 'Form submitted successfully!';
        e.target.appendChild(message);
    }

    function postTweet(e) {
        e.preventDefault();
        const message = document.createElement('p');
        message.textContent = 'Tweet posted successfully!';
        e.target.appendChild(message);
    }

    function updateProfile(e) {
        e.preventDefault();
        const message = document.createElement('p');
        message.textContent = 'Profile updated successfully!';
        e.target.appendChild(message);
    }

    function receiveNotification(e) {
        e.preventDefault();
        const message = document.createElement('p');
        message.textContent = 'Notification received!';
        e.target.appendChild(message);
    }
});
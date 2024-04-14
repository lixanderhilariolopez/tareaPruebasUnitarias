const assert = require('assert');

describe('Simple Web App', () => {
    it('should display the correct welcome message', () => {
        const expectedMessage = 'Bienvenidos a mi página web!';
        const actualMessage = document.querySelector('h1').textContent;
        assert.strictEqual(actualMessage, expectedMessage);
    });
});
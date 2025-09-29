import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App'; // <-- CHANGED: Removed the .jsx extension
import './index.css';

// This is where React starts running your App component!
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

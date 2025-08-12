import React from 'react';
import Navbar from './components/Navbar.js';
import TradeForm from './components/TradeForm.js';
import TradeList from './components/TradeList.js';

const App = () => (
  <div>
    <Navbar />
    <TradeForm />
    <TradeList />
  </div>
);

export default App;

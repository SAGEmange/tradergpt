import React, { useState } from 'react';

const TradeForm = () => {
  const [symbol, setSymbol] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('submit', symbol);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        placeholder="Ticker symbol"
      />
      <button type="submit">Add Trade</button>
    </form>
  );
};

export default TradeForm;

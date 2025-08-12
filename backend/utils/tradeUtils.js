export const calculateProfit = (entry, exit, shares) => {
  return (exit - entry) * shares;
};

import express from 'express';
import cors from 'cors';
import tradeAnalysisRoute from './routes/tradeAnalysis.js';

const app = express();

app.use(cors());
app.use(express.json());

app.use('/trade-analysis', tradeAnalysisRoute);

const PORT = 4000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

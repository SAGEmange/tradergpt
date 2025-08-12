import { Router } from 'express';
import { analyzeTradeImage } from '../controllers/tradeAnalysisController.js';

const router = Router();

router.post('/image', analyzeTradeImage);

export default router;

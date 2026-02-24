import { Request, Response } from 'express';
import { Router } from 'express';

import AuthDataController from '../controllers/AuthDataController';
import validateEmailUpdate from '../middleware/validateEmailUpdate';

const router = Router();

router.put('/', validateEmailUpdate, (req: Request, res: Response ) => {AuthDataController.updateEmail(req, res)});

export default router;
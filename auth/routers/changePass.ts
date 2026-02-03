import { Request, Response } from 'express';
import { Router } from 'express';

import validateChangePass from '../middleware/validateChangePass';
import AuthDataController from '../controllers/AuthDataController';

const router = Router();

router.put('/', validateChangePass, (req: Request, res: Response ) => {AuthDataController.changePass(req, res)});

export default router;
import { Request, Response } from 'express';
import { Router } from 'express';

import validateGetUserInfo from '../middleware/validateGetUserInfo';
import UserInfoController from '../controllers/UserInfoController';

const router = Router();

router.post('/', validateGetUserInfo, (req: Request, res: Response ) => {UserInfoController.getUserInfo(req, res)});

export default router;
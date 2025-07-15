import { Router } from 'express';

import SignUpController from '../controllers/SignUpController';
import validateSignUp from '../middleware/validateSignUp';

const router = Router();

router.post('/', validateSignUp, SignUpController.signUp);

export default router;
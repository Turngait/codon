import { Router } from 'express';

import SignInController from '../controllers/SignInController';
import validateSignIn from '../middleware/validationSignIn';

const router = Router();

router.post('/', validateSignIn, SignInController.signIn);

export default router;
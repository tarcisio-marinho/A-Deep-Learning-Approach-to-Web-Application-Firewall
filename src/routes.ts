import {Router} from 'express';

import predict from './predict';
const routes = Router();

routes.use('/predict', predict);

export default routes;
import {Router} from 'express';

import predict from './Predict/predict-route';
const routes = Router();

routes.use('/predict', predict);

export default routes;
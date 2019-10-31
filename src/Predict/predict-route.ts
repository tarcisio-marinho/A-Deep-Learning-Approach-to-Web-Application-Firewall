import {Router} from 'express';
import PredictService from './predict-service';
import { exec } from 'child_process';
import { read } from 'fs';
const bodyParser = require('body-parser');

class PredictRouter{
    public router = Router();
    private PredictService: PredictService;

    constructor(){
        this.PredictService = new PredictService();
        this.getRoutes();
    }

    public getRoutes(){
        this.router.post('/', (req: any, res: any)=>{
            try{
                this.PredictService.predict(req.body, (response: any) => {
                    res.send(response);
                });
            }catch(err){
                res.status(400).send({error:'error: ${err}'})
            }
        });
    }
}

export default new PredictRouter().router;
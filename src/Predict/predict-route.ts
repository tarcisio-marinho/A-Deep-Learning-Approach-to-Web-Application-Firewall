import {Router} from 'express';
import PredictService from './predict-service';
import { exec } from 'child_process';
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
            var payload = req.body
            console.log(payload)
            try{
                this.PredictService.predict(payload, (response: any) => {
                    res.send(response);
                });
            }catch(err){
                res.status(400).send({error:'error: ${err}'})
            }
        });
    }
}

export default new PredictRouter().router;
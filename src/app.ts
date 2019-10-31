import * as express from 'express';
import * as cors from 'cors';
import routes from './routes';
import { environment } from './Environment/Environment';


class App {
    public app: express.Application;
    private consumer: any;
    private wsServer:any;
    
    public constructor(){
        this.app = express();
        this.cors();
        this.routes();
    }

    private routes(): void {
        this.app.use(routes);
    }
    
    private cors(){
        this.app.use(cors({origin: environment.CORS_ORIGIN, credentials: true}));
    }

}

export default new App();
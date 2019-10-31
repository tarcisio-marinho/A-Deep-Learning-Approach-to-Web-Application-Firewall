import * as express from 'express';
import * as cors from 'cors';
import routes from './routes';
import { environment } from './Environment/Environment';
const helmet = require('helmet')

class App {
    public app: express.Application;
    
    public constructor(){
        this.app = express();
        this.cors();
        this.helmet();
        this.routes();
    }

    private routes(): void {
        this.app.use(routes);
    }
    
    private cors(){
        this.app.use(cors({origin: environment.CORS_ORIGIN, credentials: true}));
    }

    private helmet(){
        this.app.use(helmet());
    }
}

export default new App();
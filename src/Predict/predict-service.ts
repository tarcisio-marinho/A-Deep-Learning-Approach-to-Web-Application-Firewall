import { environment } from "../Environment/Environment";
import { type } from "os";

const spawn = require("child_process").spawn;
const fs = require("fs");

class GroupsService {
    public constructor() { }

    public predict(payload: any, callback: any) {

        if (!payload['data']) {
            throw ("Invalid format, data field expected.")
        }

        var file = fs.createWriteStream(environment.PAYLOAD_FILE, {flags:'w'})

        if(! Array.isArray(payload['data'])){
            throw ("Data in wrong format, expected a array of payloads");
        }

        for(var element in payload['data']){
            file.write(payload['data'][element] + "\n");
        }

        file.end()
        
        this.runPython((res:any)=>{
            callback(res);
        });
    }

    private runPython(callback:any) {
        var process = spawn('python', [environment.PYTHON_SCRIPT,
         environment.MODEL_PATH, environment.PAYLOAD_FILE, environment.FASTTEXT_PATH]);

        process.stdout.on('data', (pythonResponse: any) => {
            console.log(pythonResponse.toString())
            callback({ data: JSON.parse(pythonResponse.toString().replace("\n", ""))});
        });
    }
}

export default GroupsService;
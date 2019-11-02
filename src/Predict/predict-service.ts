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

        fs.writeFile(environment.PAYLOAD_FILE, payload['data'], (err: any) => {
            if (err) {
                throw err;
            }
            this.runPython((res:any)=>{
                callback(res);
            });
        });
    }

    private runPython(callback:any) {
        var process = spawn('python', ["./knowledge/main.py",
         environment.MODEL_PATH, environment.PAYLOAD_FILE]);

        process.stdout.on('data', (pythonResponse: any) => {
            callback({ data: JSON.parse(pythonResponse.toString().replace("\n", ""))});
        });
    }
}

export default GroupsService;
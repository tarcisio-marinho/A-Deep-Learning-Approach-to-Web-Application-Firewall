import { environment } from "../Environment/Environment";
import { type } from "os";

const spawn = require("child_process").spawn;
const fs = require("fs");

class GroupsService {
    public constructor() {}

    public predict(payload: any, callback: any) {

        if(!payload['data']){
            throw("Invalid format, data field expected.")
        }

        fs.writeFile(environment.PAYLOAD_FILE, payload['data'], (err: any) => {
            if (err){
                throw err;
            }
        });

        var process = spawn('python', ["./knowledge/main.py", 
                                        environment.PAYLOAD_FILE]);
        
        process.stdout.on('data', (pythonResponse: any) => {
            callback({ data: pythonResponse.toString() });
        });
    }
}

export default GroupsService;
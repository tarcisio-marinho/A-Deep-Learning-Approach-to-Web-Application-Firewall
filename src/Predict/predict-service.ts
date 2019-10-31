import { environment } from "../Environment/Environment";

const spawn = require("child_process").spawn;
const fs = require("fs");

class GroupsService {
    public constructor() {

    }

    public predict(payload: string, callback: any) {

        fs.writeFile(environment.PAYLOAD_FILE, payload, (err: any) => {
            if (err){
                throw err;
            }

            var process = spawn('python', ["./knowledge/main.py", 
                                            environment.PAYLOAD_FILE]);

            process.stdout.on('data', (pythonResponse: any) => {
                callback({ data: pythonResponse.toString() });
            });
        });
    }
}

export default GroupsService;
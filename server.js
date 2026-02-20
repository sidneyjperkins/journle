import express from "express";
import bodyParser from "body-parser";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();

// serve frontend
app.use(express.static(path.join(__dirname, ".")));
app.use(bodyParser.json());

app.listen(3000);

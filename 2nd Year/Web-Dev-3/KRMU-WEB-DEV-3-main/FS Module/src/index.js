// src/index.js

const fs = require('fs'); // Import the file system module
 
function processStudent(student) {
    const marks = parseInt(student.split(' ')[1]);
    
    if (marks >= 40) {
        return 'PASS';
    } else {
        return 'FAIL';
    }
}
 
function writeReport(studentsFilePath, reportFilePath) { 
 
    fs.readFile(studentsFilePath, 'utf8', function(err, data) {
        if (err) {
            console.error('Error reading file:', err);
            return;
        }
         
        const students = data.split('\n');
         

        let reportContent = '';
 
        for (const student of students) {
            
            // Split the name and marks
            const [name, marks] = student.trim().split(/\s+/); 

            const result = processStudent(student);

            reportContent += `${name} - ${result}\n`;         
        }
         
        fs.writeFile(reportFilePath, reportContent, function(err) {
            if (err) {
                console.error('Error writing file:', err);
                return;
            }

            console.log(`Report written to '${reportFilePath}'`);
        });
    });   
}
const inputPath = path.join(__dirname, "students.txt");
const outputPath = path.join(__dirname, "report.txt");

writeReport(inputPath, outputPath);

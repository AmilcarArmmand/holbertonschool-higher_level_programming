#!/usr/bin/node
/* Write a script that concats 2 files
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fs = require('fs');

const textA = fs.readFileSync(fileA, 'utf-8');
const textB = fs.readFileSync(fileB, 'utf-8');

fs.writeFileSync(fileC, textA + textB);
/*
{ command1 ; command2 ; command3 ; } > outfile.txt

const { exec } = require('child_process');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
// require('child_process').execSync('cat *').toString('UTF-8')
exec('cat ' + fileA + ' ' + fileB + ' > ' + fileC);
*/

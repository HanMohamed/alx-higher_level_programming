#!/usr/bin/node

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const file = new File([fileA, fileB], fileC);

## Command


`bin/render.sh <input file> <content> <sort key>  <renderer>?`
 
No renderer means you just get JSON, and if you want the JSON coloured, pipe to `jq .`
 
- content: \[ books-only | all ] 
- sort key: \[ author | title ]
- renderer: \[ simple-md | title-and-author-only | title-only ] 



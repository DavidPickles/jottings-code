## Actions

### Render

`cat <input file> | bin/render.sh  <content> <sort key>  <renderer>?`
 
No renderer means you just get JSON, and if you want the JSON coloured, pipe to `jq .`
 
- content: \[ books-only | all ] 
- sort key: \[ author | title ]
- renderer: \[ simple-md | title-and-author-only | title-only ] 


### Publish

`cat <prepub file> | bin/publish.sh`

###  Render and Publish

`cat <input file> | bin/render.sh <args> | bin/publish.sh`

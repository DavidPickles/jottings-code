## Actions


### Render and Publish 

`cat ../../jottings/raw-book-club-record.md | bin/publish.sh rp`

- The last argument 'rp' means render and publish. 
- If the last arg is just r, you'll just render using the defaults, 
- if it's p, you'll just publish from prepub/book-club-record.md

### Render to StdOut

`cat <input file> | bin/render.sh  <content> <sort key>  <renderer>?`
 
No renderer means you just get JSON, and if you want the JSON coloured, pipe to `jq .`
 
- content: \[ books-only | all ] 
- sort key: \[ author | title ]
- renderer: \[ simple-md | title-and-author-only | title-only ] 


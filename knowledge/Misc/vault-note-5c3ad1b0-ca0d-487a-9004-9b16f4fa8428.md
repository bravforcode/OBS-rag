---
type: knowledge-item
category: vault_note
tags: []
created: '2026-04-25T23:10:04.993202+00:00'
---

# README

## Category
vault_note

## Content
## Quickstart

### Before you begin

1.  [Select or create a Cloud Platform project][projects].
1.  [Enable billing for your project][billing].
1.  [Enable the Google Cloud Storage API][enable_api].
1.  [Set up authentication][auth] so you can access the
    API from your local workstation.

### Installing the client library

```bash
npm install @google-cloud/storage
```

### Using the client library

```javascript
// Imports the Google Cloud client library
const {Storage} = require('@google-cloud/storage');

// For more information on ways to initialize Storage, please see
// https://googleapis.dev/nodejs/storage/latest/Storage.html

// Creates a client using Application Default Credentials
const storage = new Storage();

// Creates a client from a Google service account key
// const storage = new Storage({keyFilename: 'key.json'});

/**
 * TODO(developer): Uncomment these variables before running the sample.
 */
// The ID of your GCS bucket
// const bucketName = 'your-unique-bucket-name';

async function createBucket() {
  // Creates the new bucket
  await storage.createBucket(bucketName);
  console.log(`Bucket ${bucketName} created.`);
}

createBucket().catch(console.error);

```

## Tags
N/A

---

## Related
- [[Knowledge/Index|Knowledge Hub]]
- [[Knowledge/Misc/Index|Misc Knowledge]]

🔗 **Auto-Generated Links**
- [[latest]] - name_mentioned
- [[README]] - name_mentioned
- [[Work]] - name_mentioned
- [[README]] - name_mentioned
- [[Note]] - name_mentioned

ðŸ“… Auto-linked: 2026-04-28 18:32

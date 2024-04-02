---
type: python
description: Get transcript of youtube video and run extract_wisdom
expects:
  url: URL of YouTube video
---

```
ts = self.youtube_transcript(url=url)
result = self.extract_wisdom(query=ts)
```

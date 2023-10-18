#OPENAI_API_KEY = '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'
#OPENAI_API_KEY = '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'
OPENAI_API_KEY = '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'


curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
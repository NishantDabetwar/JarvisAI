import os
import openai
from config import apikey
#openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to inform you that I am resigning from my position as [Position] at [Company]. My last day of work will be [date].\n\nI have enjoyed my time at [Company] and the opportunities I have had to learn and grow professionally. I am grateful for the support and guidance you have provided me over the past [time period].\n\nI wish you and the company all the best in the future. Please let me know if there is anything I can do to assist with the transition.\n\nSincerely,\n\n[Your Name]"
    }
  ],
  "created": 1685014124,
  "id": "cmpl-7K3R6RJoLrnPSYsON2M6r57xq8Zwq",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 132,
    "prompt_tokens": 9,
    "total_tokens": 141
  }
}
'''
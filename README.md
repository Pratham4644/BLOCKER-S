# 🧩 CodeSahayak 
*By Prathamesh Shinde (Solo Developer)*  
*Hackathon Duration: 3 Days | Goal: ₹1,00,000 Prize + Internship*

---

## 🌅 Day 1 – The Foundation & The First Wall

**Morning – 9:00 AM**

Excited, nervous, and slightly overwhelmed.  
I started with what looked like a simple goal: *get the environment running.*  

Everything was supposed to be easy — clone repo, run setup, and get started.  
But within an hour, the terminal turned red with the classic Python import nightmare:

```
ModuleNotFoundError: No module named 'composio_langchain'
```

At first, I thought it was a typo. Then I realized — the dependency tree had changed in the latest version.

I went through `pip install`, `pip freeze`, `python -m pip install --upgrade`, even reinstalled my venv.  
Nothing.

Then I took a deep breath, went through the docs, and realized — the latest version used **`provider`** instead of the old **`toolset`** naming.  
So I replaced:
```python
from composio_langchain import ComposioToolSet
```
with:
```python
from composio_langchain.provider import LangchainProvider as ComposioToolSet
```
and finally saw it —  
✅ “Import success!”

That moment — one print statement — felt like a small win in a long marathon.

---

**Afternoon – 1:00 PM**

The next wall came with **Composio OAuth setup**.  
Redirect URLs weren’t matching, and authentication kept failing.  
I double-checked console logs, regenerated API keys, and even wrote to Composio’s Discord (no reply).  

Finally, after manually copying the callback from my local dev server into the Composio dashboard, the green tick appeared —  
> “Integration connected successfully.”

It felt magical. I noted it down instantly in my notebook:
> “Never copy blindly. Read your redirect URLs twice.”

---

**Evening – 5:00 PM**

I moved to the **voice agent** setup — my dream part of CodeSahayak.  
Combining Marathi and English voice commands was personal.  
But Whisper didn’t agree.

Marathi-English hybrid sentences confused the model:
> “Hello, मी Prathamesh आहे”  
came out as  
> “Hello, meet Prathamesh at?”

I laughed and nearly gave up, but then realized — I could preprocess the text and pass context.  
By adding a language hint and cleaning the transcripts before ElevenLabs TTS, it suddenly clicked.

The first time I heard my AI say,  
> “नमस्कार, मी तुझा कोड चेक करतो!”  
I froze for a second.  
That wasn’t just AI — it was my dream speaking back to me.

**✅ Day 1 Goal Achieved:**  
Core infrastructure working.  
Tools connected. Voice alive.  

But I was exhausted — both mentally and emotionally.  
Still, one line in my plan echoed in my mind:  
> “Working > perfect.”

---

## ⚙️ Day 2 – The Storm of Bugs

**Morning – 9:00 AM**

Started fresh, confident — but within an hour, chaos returned.  
My **code analyzer** wasn’t analyzing anything.

AST parsing was breaking with nested loops and recursion.  
I wrote this tiny buggy test:
```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i):  # Bug
            if arr[j] < arr[j+1]:    # Bug
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return ar  # Typo
```

Instead of catching the bugs, my analyzer crashed.  
Syntax trees were throwing errors because of missing edge-case handling.

I realized — I’d been trying to make the AI too smart, too soon.  
So I simplified the logic:  
1. Use AST for structure.  
2. Use rule-based checks for common mistakes.  
3. Generate English + Marathi feedback via prompt templates.

Finally, it worked.  
For the first time, CodeSahayak detected bugs and responded with:
> “तुझ्या कोडमध्ये एक छोटासा bug आहे — loop condition चुकीचा आहे!”

That line made the sleepless night worth it.

---

**Afternoon – 2:30 PM**

Then came **multi-tool orchestration**.  
Linking GitHub → Notion → Calendar → Gmail → Slack → WhatsApp.

Each one had its own API quirks.  
Gmail blocked less secure access, Slack needed tokens, WhatsApp API demanded approval.  
Everything was screaming “time waste” — but I couldn’t give up.

So I prioritized:
> Focus on the 4 that work reliably.  
> Mock the rest.

I created a dummy workflow:
```
GitHub → Analysis → Notion → Calendar → Gmail
```
And hardcoded sample data for Slack/WhatsApp to simulate success.

Lesson learned:
> “A working demo beats a broken perfection.”

---

**Evening – 7:00 PM**

By nightfall, my code was running… slowly.  
Every run took 15+ seconds.  
Debugging felt like chasing ghosts.

I found out — every tool call was blocking. So I refactored using async calls.  
Then, finally, the orchestration clicked.

My console printed the line I’d been waiting for:
```
✅ Workflow Complete: GitHub → Analysis → Notion → Calendar → Gmail
```

I leaned back, smiled, and said to myself:
> “We’re getting there, bro.”

---

## 🎥 Day 3 – The Final Push

**Morning – 8:30 AM**

My laptop fan was louder than me now.  
Screen recording, debugging, rendering — all happening at once.  
I was preparing the **demo video** — a 2-minute summary of three days of madness.

But every time I hit “record,” something crashed.  
Either the voice agent wouldn’t respond, or OBS lagged, or Notion API timed out.

I almost gave up.

Then I remembered what my senior teammate Claude wrote at the bottom of the action plan:  
> “Don’t perfectionism. Working > perfect.”

So I took a shortcut —  
recorded a stable run, added subtitles, and voice-dubbed Marathi-English lines manually.  
When I saw it stitched together, it looked… real.  
Authentic. Functional. Alive.

---

**Afternoon – 2:00 PM**

I wrote the final README, added all links, and started the last round of testing.  
That’s when I hit the **CORS wall** connecting my backend to the new HTML/JS UI.

Frontend `fetch()` was blocked.  
Browser screamed:  
```
Access to fetch at 'http://127.0.0.1:5000/api/analyze' from origin 'null' has been blocked by CORS policy.
```

At this point, I just sighed.  
Installed `flask-cors`, added:
```python
from flask_cors import CORS
CORS(app)
```
and like magic — it worked.

The UI sent requests, backend responded, and CodeSahayak spoke.

---

**Evening – 5:30 PM**

Final submission checklist.  
I reread my friction log, smiled at the chaos, and realized something:
> Every failure taught me something the docs never could.

---

## 💡 Reflections

- **Biggest Friction:** OAuth integrations and async orchestration  
- **Hardest Moment:** When Whisper misread Marathi-English commands  
- **Most Emotional Win:** Hearing my AI say “नमस्कार” for the first time  
- **Best Lesson:** “When in doubt, simplify the problem.”  
- **Realization:** Hackathons aren’t about code — they’re about patience, resilience, and tiny victories.

---

## 🏁 Final Thoughts

After three sleepless nights, crashes, and coffee refills,  
I didn’t just build an AI tool —  
I built a story, a voice, a small spark for Indian students who want to learn coding in their own language.

CodeSahayak isn’t just a project.  
It’s a promise —  
> That language should never be a barrier to learning.

And no error log, OAuth failure, or broken endpoint can take that away.

---

*— Prathamesh Shinde*  
*Solo Developer, CodeSahayak (Hackathon 2025)*


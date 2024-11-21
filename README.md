<h2>〽️ Deploy Me </h2> 

<details><summary>📌 Deploy to Render </summary>
  
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/CodeXBots/Auto-Approve-bot)

</details>
  
<details><summary>📌 Deploy to Heroku </summary>
  
<a href="https://heroku.com/deploy?template=https://github.com/CodeXBots/Auto-Approve-bot"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"></p></a>
</details>

<details><summary>📌 Deploy to Railway </summary>
  
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/w7jSPk)
</details>
  
<details><summary>📌 Deploy to Okteto </summary>
  
[![Deploy on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/CodeXBots/Auto-Approve-bot/)
</details>

<details><summary>📌 Deploy to VPS/Local </summary>


  ```ssh
  git clone https://github.com/CodeXBots/Auto-Approve-bot
  pip3 install -r requirements.txt
  # fill config.py vars
  python3 bot.py
  ```

</details>

## 🏷 Environment Variables #
  - `API_ID` - Your Telegram API ID.Get it [Here](my.telegram.org)
  - `API_HASH` - Your Telegram API HASH.Get it [Here](my.telegram.org)
  - `DB_URL` - Add MongoDB Database URI.
  - `DB_NAME` - Add Mongodb Database Name.
  - `BOT_USERNAME` - Add Bot Username.
  - `BOT_TOKEN` - Your Bot Token. Get it from [Here](https://t.me/BotFather)
  - `LOG_CHANNEL` - Bot Logs Sending Channel. If You Don't Need This To Remove This Variable In Your Server
  - `ADMIN` - bot owners Id/ ids ( for broadcast and stats cmds). for multiple use space.

  Available Commond:-
  ```
start - Check Bot Alive.
stats - Check Bot Status.
broadcast - Broadcast Massage Send All Users In Bot.
restart - Send Message All Users In Bot & Bot Restart & Re-Deploy Server.
```

 ## ❣️Thanks To
 
- Thanks To [RknDeveloper](https://github.com/RknDeveloper) who have edited and modified this repo as now it is. (It's me 😂)


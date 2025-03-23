# 🕊️ Weekly Verbal Code Email Bot

This project automatically generates a **weekly verbal code** (a random word or phrase) and sends it to a list of recipients via email — perfect for families, small teams, or secret societies 🕵️‍♂️. The code changes every week, is simple and verbal-friendly, and is sent out using GitHub Actions.

---

## ✨ Features

- ✅ Auto-generates a verbal code each week
- ✅ Sends email via secure SMTP
- ✅ Hosted and automated using GitHub Actions
- ✅ Easily configurable via GitHub Secrets
- ✅ Includes a keep-alive workflow to prevent GitHub from suspending scheduled runs

---

## 🛠️ How It Works

- A Python script (`generate.py`) runs every Monday at 6:20 AM Eastern Time.
- It generates a word or phrase based on the week number (deterministic but feels random).
- It sends that word to your list of recipients using email.
- The script uses SMTP with STARTTLS for secure delivery.
- All credentials and settings are stored securely in GitHub Secrets.

---

## 🚀 Setup Instructions

### 1. **Clone or Fork This Repository**

```bash
git clone https://github.com/yourusername/weekly-code-email.git
cd weekly-code-email
```

---

### 2. **Add Required Secrets in GitHub**

Go to your repository → **Settings** → **Secrets and Variables** → **Actions**, then add the following **secrets**:

| Secret Name        | Value (example)                     | Description                                 |
|--------------------|-------------------------------------|---------------------------------------------|
| `SMTP_SERVER`      | `smtp.gmail.com` or `mx.sdf.org`    | Your email provider’s SMTP server           |
| `SMTP_PORT`        | `587`                               | Usually 587 (STARTTLS)                      |
| `EMAIL_ADDRESS`    | `yourname@gmail.com` or `yourdomain@sdf.org` | Email to send from               |
| `EMAIL_PASSWORD`   | Your SMTP password or app password  | App-specific password for Gmail or SDF      |
| `FAMILY_EMAIL_1`   | `someone@example.com`               | Recipient 1                                 |
| `FAMILY_EMAIL_2`   | `someone2@example.com`              | Recipient 2                                 |
| `FAMILY_EMAIL_3`   | (optional)                          | Recipient 3                                 |
| `FAMILY_EMAIL_4`   | (optional)                          | Recipient 4                                 |

> ⚠️ If you're using Gmail:  
> You **must** [enable App Passwords](https://support.google.com/accounts/answer/185833) (2FA required).  
> If you're using SDF, use `mkvpm set secret SMTP_AUTH=yourpassword` and your email will be `yourdomain@sdf.org`.

---

### 3. **Configure GitHub Actions**

There are **two workflows**:

#### 📬 `weekly_email.yml`

- Runs every Monday at 6:20 AM Eastern (adjusted in UTC)
- Calls `generate.py` to send the weekly verbal code
- Trigger: `schedule` + optional manual trigger

#### 🛡️ `keepalive.yml`

- Runs on the 1st of each month to prevent GitHub from suspending the repo due to inactivity
- Optional manual trigger via UI

✅ Both are located in `.github/workflows/`.

---

### 4. **How to Customize**

- **Change the Time**: Edit the cron line in `.github/workflows/weekly_email.yml`
- **Add More Words**: Modify the `words = [...]` list in `generate.py`
- **Change Subject Format**: Edit the `subject = f"...` line in `send_email()` inside `generate.py`

---

## 📎 File Overview

```
generate.py                 # The main script to generate and send the code
.github/workflows/
  ├── weekly_email.yml      # Sends the email every Monday
  └── keepalive.yml         # Keeps the repo alive so workflows don't pause
README.md                   # You're reading it!
```

---

## 💡 Troubleshooting

### 🛑 Workflow isn't running?
- GitHub pauses scheduled workflows in **private repos** after 60 days of inactivity.  
- Solution: use `keepalive.yml` OR run a manual dispatch occasionally.

### 🔐 Authentication issues?
- Gmail: Use an [App Password](https://support.google.com/accounts/answer/185833) with 2FA enabled.
- SDF: Use `mkvpm set secret SMTP_AUTH=yourpassword` and set `EMAIL_PASSWORD` to that value.

### 📤 Multiple `To:` Headers error?
This happens if you're setting `msg['To']` inside a loop.  
✅ Fixed in `generate.py` using `", ".join()`.

---

## 🧙 Example Output

Subject:  
```
Code of Week 12 - March 2025
```

Body:
```
Hello Family,

This week's code is: Shimmering Stars

Stay safe!
```

---

## 🙌 Credits

Built with Python, SMTP, GitHub Actions, and caffeine ☕  
Inspired by families who like secret codes and staying connected 💌

---

## 📬 License

MIT — Use it, fork it, improve it, share it.

---

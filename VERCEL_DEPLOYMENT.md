# Deploying Maypo to Vercel

## Prerequisites
- Vercel CLI installed or connected GitHub account
- Python 3.11+
- All required API keys configured

## Deployment Steps

### Option 1: Via GitHub Integration (Recommended)
1. Go to https://vercel.com/dashboard
2. Click "Add New Project"
3. Import your GitHub repository: `juicedUPDev/juicedUP-repo`
4. Configure environment variables in Vercel settings
5. Click Deploy

### Option 2: Via Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy to production
vercel --prod
```

## Environment Variables Setup

In your Vercel project dashboard, add these environment variables. The repository's `.env.example` is the source of truth and should be mirrored here for a working deployment.

### Required for app startup
```env
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO
OPENAI_API_KEY=your_actual_key
OPENAI_MODEL=gpt-4
JWT_SECRET=your_super_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
```

### Optional, but commonly used in this project
```env
DATABASE_URL=postgresql://user:password@localhost:5432/maypo
REDIS_URL=redis://localhost:6379/0
FIREBASE_CREDENTIALS_PATH=/path/to/serviceAccountKey.json
MONTHLY_BUDGET_LIMIT=5000
COST_ALERT_THRESHOLD=0.80
ENABLE_ANALYTICS=true
ENABLE_VERSIONING=true
ENABLE_COST_OPTIMIZATION=true
ENABLE_CACHE=true
```

> If you are deploying to Vercel without a local database or Redis, set these values only if the app or route handlers use them in your environment. For production, prefer Vercel project env vars over hardcoded secrets.

## Verification

After deployment, verify the application is running:

```bash
# Check health endpoint
curl https://your-vercel-domain.vercel.app/health

# Expected response:
{
  "status": "healthy",
  "message": "Maypo AI Consulting Platform is running",
  "version": "1.0.0",
  "analytics": "Vercel Web Analytics enabled"
}
```

## API Endpoints

Once deployed, you can access:

- **Dashboard**: `https://your-domain.vercel.app/`
- **Health Check**: `https://your-domain.vercel.app/health`
- **Prompts API**: `https://your-domain.vercel.app/api/prompts`
- **Consulting API**: `https://your-domain.vercel.app/api/consulting`
- **Analytics API**: `https://your-domain.vercel.app/api/analytics/dashboard`

## Enable Web Analytics

1. Go to your Vercel project dashboard
2. Navigate to **Analytics** tab
3. Click **Enable Web Analytics**
4. Data will start collecting automatically

## Troubleshooting

### Build Fails
- ✅ Python version updated to 3.11
- ✅ Dependencies pinned in requirements.txt
- ✅ Check build logs in Vercel dashboard

### Routes Not Working
- Ensure route files exist in `backend/routes/`
- Check route imports in `backend/app.py`
- Verify CORS is enabled

### Analytics Not Showing
- Enable in Vercel dashboard
- Check browser console for script errors
- Verify `/_vercel/insights/script.js` loads

## Monitoring

- **Real-time Logs**: View in Vercel dashboard
- **Web Analytics**: Check Vercel Analytics tab
- **Performance**: Use Vercel Observability
- **Error Tracking**: Monitor health endpoint

## Rollback

If deployment has issues:
```bash
vercel rollback
```

## Next Steps

1. ✅ Fixed and pinned dependencies
2. ✅ Updated Python to 3.11
3. ✅ Created API route structure
4. ✅ Added environment configuration
5. 🔲 Deploy to Vercel (run the deployment steps above)
6. 🔲 Configure environment variables in Vercel dashboard
7. 🔲 Enable Web Analytics

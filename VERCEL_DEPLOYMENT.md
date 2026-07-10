# Deploying Maypo to Vercel

## Prerequisites
- Vercel CLI installed or connected GitHub account
- Python 3.11+
- All required API keys configured

## Deployment Steps

### 1. Prepare Environment Variables
Configure these in your Vercel project settings:

```
OPENAI_API_KEY=your_key
ENVIRONMENT=production
DEBUG=false
```

### 2. Deploy via CLI
```bash
vercel --prod
```

Or connect your GitHub repository to Vercel for automatic deployments.

### 3. Deploy via Vercel Dashboard
1. Go to https://vercel.com/dashboard
2. Import your GitHub repository
3. Configure environment variables
4. Click Deploy

## Verification

After deployment, verify the application:

```bash
curl https://your-domain.vercel.app/health
```

Expected response:
```json
{
  "status": "healthy",
  "message": "Maypo AI Consulting Platform is running",
  "version": "1.0.0",
  "analytics": "Vercel Web Analytics enabled"
}
```

## Troubleshooting

### Build Fails
- Check Python version in `vercel.json`
- Verify all dependencies in `requirements.txt`
- Check for missing route files

### Routes Not Working
- Ensure route files exist in `backend/routes/`
- Check CORS configuration
- Verify API endpoints in logs

### Analytics Not Showing
- Enable Web Analytics in Vercel dashboard
- Check browser console for errors
- Verify `/_vercel/insights/script.js` loads

## Monitoring

Monitor your deployment:
- **Logs**: View in Vercel dashboard
- **Analytics**: Check Vercel Web Analytics tab
- **Performance**: Use Vercel Analytics dashboard

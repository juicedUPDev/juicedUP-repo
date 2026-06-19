# Vercel Web Analytics Integration

This project has been configured with **Vercel Web Analytics** to track visitor engagement, page performance, and user behavior in real-time.

## What's Been Implemented

### 1. Analytics Script Integration
The Vercel Web Analytics script has been added to the main dashboard template (`backend/templates/index.html`):

```html
<!-- Vercel Web Analytics Script -->
<script>
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="/_vercel/insights/script.js"></script>
```

This follows the official Vercel documentation for HTML/Static site integration.

### 2. FastAPI Application Updates
The FastAPI backend (`backend/app.py`) has been updated to:
- Serve HTML templates using Jinja2
- Mount static file directories
- Provide a main dashboard route at `/` that includes analytics
- Include a health check endpoint at `/health` that reports analytics status

### 3. Project Dependencies
The following packages have been added to `requirements.txt`:
- `fastapi==0.128.8` - Web framework
- `uvicorn==0.39.0` - ASGI server
- `jinja2==3.1.6` - Template engine
- `python-multipart==0.0.20` - Form data support
- `aiofiles==25.1.0` - Async file operations

### 4. Vercel Configuration
A `vercel.json` file has been created to configure the deployment properly for Python/FastAPI applications.

## Enabling Analytics on Vercel Dashboard

To fully enable analytics, you need to activate it in your Vercel dashboard:

1. Go to your project on [Vercel Dashboard](https://vercel.com/dashboard)
2. Navigate to the **Analytics** tab in the sidebar
3. Click **Enable Web Analytics**
4. Deploy your application

Once enabled, analytics data will be collected at these routes:
- `/_vercel/insights/script.js` - Analytics script
- `/_vercel/insights/view` - Page view tracking endpoint

## What Gets Tracked

Vercel Web Analytics tracks:

- **Page Views**: Every page visit and navigation
- **Visitor Count**: Unique visitors based on hashed request data
- **Traffic Sources**: Where your visitors come from
- **Popular Pages**: Most visited pages on your platform
- **Geographic Data**: Where your users are located
- **Device & Browser Info**: User agent statistics
- **Performance Metrics**: Page load times and Core Web Vitals

## Viewing Analytics Data

After deploying to Vercel and enabling analytics:

1. Visit your Vercel project dashboard
2. Click on **Analytics** in the sidebar
3. View real-time and historical data including:
   - Total page views
   - Unique visitors
   - Top pages
   - Traffic sources
   - Geographic distribution
   - Browser/device statistics

## Privacy & Compliance

Vercel Web Analytics is privacy-friendly:
- ✅ **No cookies used**
- ✅ **GDPR compliant**
- ✅ **No personal data collection**
- ✅ **Visitor identification through hashed request fingerprints**

No cookie consent banners are required.

## Local Development

When running locally, analytics will be in **development mode** and won't send data to production. To test the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI application
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000` to see the dashboard with analytics integration.

## Custom Events (Optional)

For advanced analytics tracking, you can track custom events using the `track()` function. Since this is a Python backend, custom events would require:

1. Installing the `@vercel/analytics` npm package in a Node.js environment
2. Using the server-side track function from `@vercel/analytics/server`
3. Making HTTP requests from Python to a Node.js service

For Python-only implementations, you would need to use Vercel's Analytics API directly (available for Pro/Enterprise plans).

## Deployment

To deploy with analytics enabled:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel deploy --prod
```

Or connect your GitHub repository to Vercel for automatic deployments.

## Documentation References

- [Vercel Web Analytics Quickstart](https://vercel.com/docs/analytics/quickstart)
- [Vercel Analytics Package](https://vercel.com/docs/analytics/package)
- [Custom Events Tracking](https://vercel.com/docs/analytics/custom-events)
- [FastAPI Deployment on Vercel](https://vercel.com/docs/frameworks/backend/fastapi)

## Support

For issues or questions:
- Vercel Analytics: [Vercel Support](https://vercel.com/support)
- Project Issues: [GitHub Issues](https://github.com/juicedUPDev/maypo/issues)

---

**Note**: Vercel Web Analytics is available on all Vercel plans. Custom event tracking requires a Pro or Enterprise plan.

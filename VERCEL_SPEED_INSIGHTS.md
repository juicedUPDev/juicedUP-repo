# Vercel Speed Insights Integration

This project has been configured with **Vercel Speed Insights** to monitor real-time performance metrics and Core Web Vitals for your application.

## What's Been Implemented

### 1. Speed Insights Script Integration
The Vercel Speed Insights script has been added to the main dashboard template (`backend/templates/index.html`):

```html
<!-- Vercel Speed Insights Script -->
<script>
    window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
</script>
<script defer src="/_vercel/speed-insights/script.js"></script>
```

This follows the official Vercel documentation for HTML/Static site integration.

### 2. FastAPI Application Updates
The FastAPI backend (`backend/app.py`) health check endpoint has been updated to report Speed Insights status:

```python
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Maypo AI Consulting Platform is running",
        "version": "1.0.0",
        "analytics": "Vercel Web Analytics enabled",
        "speed_insights": "Vercel Speed Insights enabled"
    }
```

### 3. Integration with Existing Analytics
Speed Insights works alongside the existing Vercel Web Analytics implementation, providing complementary data:
- **Web Analytics**: Tracks visitor engagement, page views, and user behavior
- **Speed Insights**: Monitors performance metrics and Core Web Vitals

## Enabling Speed Insights on Vercel Dashboard

To fully enable Speed Insights, you need to activate it in your Vercel dashboard:

1. Go to your project on [Vercel Dashboard](https://vercel.com/dashboard)
2. Navigate to the **Speed Insights** tab in the sidebar
3. Click **Enable Speed Insights**
4. Deploy your application

Once enabled, performance data will be collected at these routes:
- `/_vercel/speed-insights/script.js` - Speed Insights script
- Performance metrics will be automatically tracked and sent to Vercel

## What Gets Tracked

Vercel Speed Insights monitors key performance metrics including:

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Measures loading performance (should be < 2.5s)
- **FID (First Input Delay)**: Measures interactivity (should be < 100ms)
- **CLS (Cumulative Layout Shift)**: Measures visual stability (should be < 0.1)
- **INP (Interaction to Next Paint)**: Measures overall responsiveness (replaces FID)
- **TTFB (Time to First Byte)**: Measures server response time
- **FCP (First Contentful Paint)**: Measures when first content appears

### Additional Metrics
- **Page load times**: Complete page load duration
- **Performance by route**: Metrics broken down by URL path
- **Device categories**: Performance comparison across desktop/mobile/tablet
- **Geographic data**: Performance by user location
- **Browser types**: Performance across different browsers

## Viewing Speed Insights Data

After deploying to Vercel and enabling Speed Insights:

1. Visit your Vercel project dashboard
2. Click on **Speed Insights** in the sidebar
3. View real-time and historical data including:
   - Core Web Vitals scores (Good/Needs Improvement/Poor)
   - Performance trends over time
   - Individual page performance
   - Performance by device type
   - Geographic performance breakdown
   - Real User Monitoring (RUM) data

### Understanding the Data

Speed Insights collects data from real users (Real User Monitoring):
- Data appears after your site receives traffic
- Metrics are calculated from actual user experiences
- Takes a few days to accumulate meaningful data
- Shows 75th percentile values (P75) for most metrics

## Performance Thresholds

Vercel uses Google's Core Web Vitals thresholds:

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP    | ≤ 2.5s | 2.5s - 4.0s | > 4.0s |
| FID/INP | ≤ 100ms | 100ms - 300ms | > 300ms |
| CLS    | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |
| TTFB   | ≤ 800ms | 800ms - 1800ms | > 1800ms |
| FCP    | ≤ 1.8s | 1.8s - 3.0s | > 3.0s |

## Privacy & Compliance

Vercel Speed Insights is privacy-friendly:
- ✅ **No personal data collection**
- ✅ **GDPR compliant**
- ✅ **No cookies used**
- ✅ **Anonymous performance metrics only**

No cookie consent banners are required.

## Local Development

When running locally, Speed Insights will be in **development mode**:
- Scripts load but don't send data to production
- No performance data is collected locally
- Testing requires deployment to Vercel

To test the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI application
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000` to see the dashboard with Speed Insights integration.

## Framework Compatibility

This implementation uses the **HTML/Static Site** approach, which is framework-agnostic and works with:
- ✅ FastAPI (current implementation)
- ✅ Flask
- ✅ Django
- ✅ Any Python web framework serving HTML
- ✅ Static HTML sites
- ✅ Server-rendered applications

For JavaScript frameworks (React, Next.js, Vue, etc.), Vercel provides dedicated npm packages with framework-specific components.

## Troubleshooting

### Speed Insights Not Showing Data
1. Ensure Speed Insights is enabled in Vercel dashboard
2. Deploy the application to Vercel (doesn't work locally)
3. Wait for user traffic (requires real visitors)
4. Allow a few days for data accumulation

### Script Loading Issues
- Verify the script tags are in the HTML before `</body>`
- Check browser console for errors
- Ensure deployment is on Vercel (scripts only work on Vercel infrastructure)

### Performance Issues Detected
If Speed Insights shows poor performance:
1. Optimize images (use WebP, proper sizing)
2. Minimize JavaScript bundles
3. Enable caching headers
4. Use CDN for static assets
5. Implement lazy loading
6. Review server response times

## Best Practices

1. **Monitor Regularly**: Check Speed Insights weekly to track trends
2. **Set Performance Budgets**: Define acceptable thresholds for your app
3. **Test Before Deploy**: Use Lighthouse or PageSpeed Insights during development
4. **Optimize Critical Path**: Focus on LCP and FCP improvements first
5. **Address CLS**: Ensure stable layouts during page load
6. **Server Optimization**: Reduce TTFB with efficient backend code

## Integration with CI/CD

Consider adding performance checks to your deployment pipeline:
- Use Vercel's Checks API to block deployments with poor performance
- Set up Lighthouse CI for pre-deployment testing
- Monitor performance regressions between deployments

## Deployment

To deploy with Speed Insights enabled:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel deploy --prod
```

Or connect your GitHub repository to Vercel for automatic deployments.

## Documentation References

- [Vercel Speed Insights Quickstart](https://vercel.com/docs/speed-insights/quickstart)
- [Core Web Vitals Explained](https://web.dev/vitals/)
- [Performance Optimization Guide](https://vercel.com/docs/concepts/performance)
- [FastAPI Deployment on Vercel](https://vercel.com/docs/frameworks/backend/fastapi)
- [Vercel Analytics vs Speed Insights](https://vercel.com/docs/analytics)

## Comparison: Web Analytics vs Speed Insights

| Feature | Web Analytics | Speed Insights |
|---------|---------------|----------------|
| **Purpose** | Track visitor behavior | Monitor performance |
| **Metrics** | Page views, visitors, sources | Core Web Vitals, load times |
| **Use Case** | Understand user engagement | Optimize user experience |
| **Data Type** | Behavioral analytics | Performance metrics |
| **Availability** | All Vercel plans | All Vercel plans |

Both tools complement each other to provide a complete picture of your application's health.

## Support

For issues or questions:
- Vercel Speed Insights: [Vercel Support](https://vercel.com/support)
- Project Issues: [GitHub Issues](https://github.com/juicedUPDev/maypo/issues)

---

**Note**: Speed Insights requires deployment to Vercel and real user traffic to generate data. Metrics typically appear within a few days of enabling the feature.

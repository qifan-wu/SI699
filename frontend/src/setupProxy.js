const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(
    '/data',
    createProxyMiddleware({
        target: 'http://100.27.2.225:5000',
        changeOrigin: true,
    })
    );
};

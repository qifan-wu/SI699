const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(
        '/data',
        createProxyMiddleware({
            target: 'http://0.0.0.0:5000',
            changeOrigin: true,
        })
    );
    app.use(
        '/submit-form',
        createProxyMiddleware({
            target: 'http://0.0.0.0:5000',
            changeOrigin: true,
        })
    );
    app.use(
        '/submit-newURL',
        createProxyMiddleware({
            target: 'http://0.0.0.0:5000',
            changeOrigin: true,
        })
    );
};

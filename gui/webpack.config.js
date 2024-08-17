const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        publicPath: '/',
        path: path.resolve(__dirname, 'dist'),
    },
    devServer: {
        static: {
            directory: path.join(__dirname, 'dist'),
        },
        compress: true,
        port: 9000,
        historyApiFallback: true,
        proxy: [
            {
                context: ['/images'],
                target: 'http://localhost:8000',
            },
        ],
    },
    plugins: [new HtmlWebpackPlugin()],
};
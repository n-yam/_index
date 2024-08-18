const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = (argv) => {
    const isProduction = argv.mode === "production";

    return {
        mode: isProduction ? 'production' : 'development',
        entry: './src/index.js',
        output: {
            filename: 'main.js',
            publicPath: '/static/',
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
        plugins: [
            new HtmlWebpackPlugin(),
            new webpack.DefinePlugin({
                'API_SERVER': JSON.stringify(isProduction ? 'http://192.168.11.100:8000' : 'http://localhost:8000'),
            }),
        ],
        module: {
            rules: [
                {
                    test: /\.css$/i,
                    use: ["style-loader", "css-loader"],
                },
            ],
        },
    };
};
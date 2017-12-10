var webpack = require('webpack');
var path = require('path');

var ExtractTextPlugin = require('extract-text-webpack-plugin');

var BASE_DIR = path.resolve(__dirname, './');
var SRC_DIR = path.join(BASE_DIR, './src');
var DIST_DIR = path.join(BASE_DIR, './dist');

module.exports = {
    entry: {
      main: path.join(SRC_DIR, './js/index.js'),
    },

    output: {
        path: path.join(__dirname, 'dist'),
        filename: 'js/[name].js',
        publicPath: '/'
    },

    module: {
        rules: [
            {
                test: /\.js?$/,
                exclude: /node_modules/,
                use: 'babel-loader'
            },
            {
                test: /\.vue$/, 
                loader: "vue-loader"
            },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    use: [
                      { loader: "css-loader?minimize" }, // css-loader?minimize
                      { loader: "postcss-loader",
                        options: { plugins() { return [require('autoprefixer')({
                            browsers: ['last 3 versions']
                          })]; }
                        }
                      },
                      { loader: "sass-loader" }
                    ],
                    fallback: "style-loader"
                }),
            },
            {
                test: /\.css$/,
                use: [
                  {
                    loader: 'style-loader'
                  },
                  {
                    loader: "css-loader"
                  }
                ],
            },
            {
                test: /\.(png|jpg|jpeg|gif|ico)$/,
                loader: 'file-loader',
                options: {
                  name: 'assets/[name].[ext]'
                },
            },
        ]
    },

    resolve: {
        alias: {
          vue: 'vue/dist/vue.js'
        }
    },

    plugins: [
        new ExtractTextPlugin({
          filename: "css/[name].css",
        }),
        // new UglifyJSPlugin()
    ],

};
import { defineConfig } from "vite";
import autoprefixer from "autoprefixer";
import cssnano from "cssnano";
import path from "path";

export default defineConfig(({ mode }) => {
    const isProduction = mode === "production";

    return {
        css: {
            postcss: {
                plugins: [
                    autoprefixer(),
                    isProduction && cssnano(),
                ].filter(Boolean),
            },
        },
        build: {
            outDir: "static",
            emptyOutDir: false,
            rollupOptions: {
                input: path.resolve(__dirname, "static/assets/scss/custom.scss"),
                output: {
                    assetFileNames: (assetInfo) => {
                        if (assetInfo.name === "custom.css") {
                            return "assets/css/custom.css";
                        }
                        return "assets/css/[name].[ext]";
                    },
                },
            },
        },
    };
});
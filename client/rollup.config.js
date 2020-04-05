import svelte from 'rollup-plugin-svelte';
import resolve from 'rollup-plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
import css from "rollup-plugin-css-only";
import svg from 'rollup-plugin-svg'

const production = !process.env.ROLLUP_WATCH;

export default {
	input: 'src/main.js',
	output: {
		sourcemap: !production,
		format: 'iife',
		name: 'app',
		file: 'public/assets/bundle.js'
	},
	plugins: [
		svg(),
		css({ output: "public/assets/extra.css" }),
		svelte({
			dev: !production,
			css: css => {
				css.write('public/assets/bundle.css', !production);
			}
		}),
		resolve({
			browser: true,
			dedupe: importee => importee === 'svelte' || importee.startsWith('svelte/')
		}),
		commonjs(), 
		!production && livereload('public'),
		production && terser()
	],
	watch: {
		clearScreen: false
	}
};
